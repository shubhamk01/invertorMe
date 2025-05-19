from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from invertorMe.app.services.user_service import create_user, update_user_budget
from invertorMe.stock_analyzer.database.db_connection import get_db

# from app.services.user_service import create_user, update_user_budget
# from app.database.db_connection import get_db

router = APIRouter()

@router.post("/create-user")
def create_new_user(username: str, email: str, budget: float, db: Session = Depends(get_db)):
    """
    Create a new user.
    :param username: Username of the user.
    :param email: Email address.
    :param budget: Investment budget.
    :param db: Database session.
    :return: Created user details.
    """
    try:
        user = create_user(db, username, email, budget)
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/update-budget/{user_id}")
def update_budget(user_id: int, budget: float, db: Session = Depends(get_db)):
    """
    Update a user's budget.
    :param user_id: ID of the user.
    :param budget: New budget.
    :param db: Database session.
    :return: Updated user details.
    """
    try:
        user = update_user_budget(db, user_id, budget)
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
