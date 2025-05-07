from sqlalchemy import TINYINT, SMALLINT, Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    user_email = Column(String(150), nullable=False)
    user_password = Column(String(50), nullable=False)
    user_mobile = Column(Integer, nullable=False)
    user_birth = Column(String(20), nullable=False)
    user_code = Column(SMALLINT, nullable=False)
    user_approve = Column(TINYINT, nullable=False, default=0)
    user_gender = Column(String(10), nullable=False)
