import sys, os
import asyncio, contextlib, random
from sqlalchemy import select, insert
from fastapi_users.exceptions import UserAlreadyExists

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.database import get_async_session, engine
from src.req.auth.utils import get_user_db
from src.req.auth.models import Role
from src.req.auth.manager import get_user_manager
from src.req.auth.schemas import UserCreate

get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'

length = 20

use_for = lower_case + upper_case + number

def passGen(length):
	try:
		if length == '':
			length_pass = 8
		else:
			length_pass = int(length)
		return ''.join(random.sample(use_for, length_pass))
	except:
		return 1

async def create_user(email: str, password: str, username: str, role_id: int, is_superuser: bool = False):
	try:
		async with get_async_session_context() as session:
			async with get_user_db_context(session) as user_db:
				async with get_user_manager_context(user_db) as user_manager:
					# BUG: in bcrypt  version = _bcrypt.__about__.__version__ module 'bcrypt' has no attribute '__about__'
					user = await user_manager.create(
						UserCreate(
							email=email, password=password, username=username, role_id=role_id
						),
						role_id=role_id
					)
					print(f"Created: User - {username}, password - {password}")
	except UserAlreadyExists:
		print(f"User {email} already exists")

async def init_role():
	async with engine.begin() as conn:
		result = await conn.execute(select(Role))
		roles = result.scalars().all()
		if roles == []:
			await conn.execute(insert(Role).values(id = 1, name='root', value=10000))
			await conn.execute(insert(Role).values(id = 2, name='admin', value=1000))
			await conn.execute(insert(Role).values(id = 3, name='moderator', value=100))
			await conn.execute(insert(Role).values(id = 4, name='user', value=10))

async def main():
	passwd = passGen(length)
	await init_role()
	await create_user(email = "no@mail.yet", password = passwd, username="root", role_id=1, is_superuser=True)

if __name__ == "__main__":
	asyncio.run(main())