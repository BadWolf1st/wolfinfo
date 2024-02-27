from fastapi import APIRouter, Depends, UploadFile, HTTPException, Response
from starlette import status
from src.req.auth.base_config import fastapi_users
from src.req.auth.models import User, Role
from src.req.images.models import Image
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from sqlalchemy import select, update
from src.req.images.controller import Controller
from datetime import datetime

cntl = Controller()

router = APIRouter(
	prefix="/image",
	tags=["Images"]
)

current_user = fastapi_users.current_user()

@router.get("/name/{image_name}", status_code=status.HTTP_200_OK)
async def get_image_by_name(image_name: str, session: AsyncSession = Depends(get_async_session)) -> Response:
	result = await session.execute(select(Image).where(Image.name == image_name))
	image = result.scalars().first()
	return Response(
		cntl.read(image_name),
		media_type=Controller.get_file_type_from_name(image_name),
		headers={"Cache-Control": "no-cache", "name": image.name, "file-type": image.file_type, "type": image.type},
		status_code=status.HTTP_200_OK
	)

@router.get("/id/{image_id}", status_code=status.HTTP_200_OK)
async def get_image_by_name(image_id: int, session: AsyncSession = Depends(get_async_session)) -> Response:
	result = await session.execute(select(Image).where(Image.id == image_id))
	image = result.scalars().first()
	return Response(
		cntl.read(image.name),
		media_type=Controller.get_file_type_from_name(image.name),
		headers={"Cache-Control": "no-cache", "name": image.name, "file-type": image.file_type, "type": image.type},
		status_code=status.HTTP_200_OK
	)

@router.put("/name/{image_name}")
async def update_image(image_name: str, file: UploadFile, user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
	result = await session.execute(select(Image).where(Image.name == image_name))
	image = result.scalars().first()
	if not image:
		raise HTTPException(status.HTTP_404_NOT_FOUND)
	if user.role_id not in [1, 2, 3]:
		raise HTTPException(status.HTTP_403_FORBIDDEN)
	if file.content_type not in ['image/jpeg', 'image/png']:
		raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
							detail="Only .jpeg, .jpg or .png  files allowed")
	cntl.write(file, file.filename, no_check=True)
	await session.execute(update(Image).values(last_update_date=datetime.utcnow()).where(Image.name == image_name))

@router.put("/id/{image_id}")
async def update_image(image_id: int, file: UploadFile, user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
	result = await session.execute(select(Image).where(Image.id == image_id))
	image = result.scalars().first()
	if not image:
		raise HTTPException(status.HTTP_404_NOT_FOUND)
	if user.role_id not in [1, 2, 3]:
		raise HTTPException(status.HTTP_403_FORBIDDEN)
	if file.content_type not in ['image/jpeg', 'image/png']:
		raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
							detail="Only .jpeg, .jpg or .png  files allowed")
	cntl.write(file, image.name, no_check=True)
	await session.execute(update(Image).values(last_update_date=datetime.utcnow()).where(Image.id == image_id))

	"""
	>>> with engine.begin() as conn:
...     result = conn.execute(
...         update(user_table)
...         .values(fullname="Patrick McStar")
...         .where(user_table.c.name == "patrick")
...     )
...     print(result.rowcount)
	"""

@router.post("/", status_code=status.HTTP_200_OK)
async def post(file: UploadFile, user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
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
