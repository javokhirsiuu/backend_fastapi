from sqlalchemy import Column,Integer,String,ForeignKey
from db import Base

from sqlalchemy.orm import relationship




class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True)
    username = Column(String,unique=True,nullable=False)
    password = Column(String,nullable=False)
    email = Column(String)



class COMMENTS(Base):
    __tablename__ = "comments"
    id = Column(Integer,primary_key=True)
    comments = Column(String,nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'),nullable=False)
    user_rel = relationship(User,backref="users")
