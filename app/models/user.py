from sqlalchemy import Column, Integer, String, Float

from invertorMe.stock_analyzer.database.db_connection import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    budget = Column(Float, default=0.0)
