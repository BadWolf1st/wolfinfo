from fastapi import APIRouter, Depends, UploadFile, HTTPException
from starlette import status
from src.req.auth.base_config import fastapi_users
from src.req.auth.models import User, Role
from src.req.images.models import Image
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from sqlalchemy import select, insert
from src.req.images.controller import Controller

cntl = Controller()

router = APIRouter(
	prefix="/image",
	tags=["Images"]
)

curent_user = fastapi_users.current_user()

@router.get("/{image_id}")
async def get():
	...

@router.post("/", status_code=status.HTTP_200_OK)
async def post(file: UploadFile, user: User = Depends(curent_user), session: AsyncSession = Depends(get_async_session)):
	result = await session.execute(select(Role).where(Role.id == user.role_id))
	# unrow untuple role
	role = result.scalars().first()
	if role.value < 10:
		raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
	if file.content_type not in ['image/jpeg', 'image/png']:
		raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
			detail="Only .jpeg, .jpg or .png files allowed")
	cntl.write(file, file.filename)
	image = Image(name=file.filename, file_type=file.content_type, user=user.id, type='images')
	try:
		session.add(image)
		await session.commit()
	except Exception as e:
		# TODO: Add log about error by loguru if debug_mode
		raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
	return status.HTTP_200_OK
