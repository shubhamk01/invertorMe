from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from stock_analyzer.app.models.stock import Stock
from stock_analyzer.database.db_connection import get_db


router = APIRouter()

@router.get("/stocks")
def get_stocks(db: Session = Depends(get_db)):
    """
    Fetch all stocks from the database.
    """
    return db.query(Stock).all()

