from sqlalchemy import Column, Integer, String, Float, DateTime

from stock_analyzer.database.db_connection import Base

class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(10), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
