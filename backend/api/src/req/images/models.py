from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, TIMESTAMP
from src.database import Base
from src.req.auth.models import User, user


metadata = MetaData()

image = Table(
    "image",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
	Column("file_type", String),
	Column("user", Integer, ForeignKey(user.c.id)),
    Column("create_date", TIMESTAMP, default=datetime.utcnow),
	Column("last_update_date", TIMESTAMP, default=datetime.utcnow, nullable=True),
    Column("type", String, default='images')
)

class Image(Base):
    __tablename__='image'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    user = Column(Integer, ForeignKey(User.id), nullable=False)
    create_date = Column(TIMESTAMP, default=datetime.utcnow)
    last_update_date = Column(TIMESTAMP, default=datetime.utcnow, nullable=True)
    type = Column(String, default='images')
