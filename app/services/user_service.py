from sqlalchemy.orm import Session
from app.models.user import User

def create_user(db: Session, username: str, email: str, budget: float):
    """
    Create a new user.
    :param db: SQLAlchemy session.
    :param username: Username of the user.
    :param email: Email address of the user.
    :param budget: Investment budget for the user.
    :return: User instance.
    """
    user = User(username=username, email=email, budget=budget)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user_budget(db: Session, user_id: int, budget: float):
    """
    Update the budget for a user.
    :param db: SQLAlchemy session.
    :param user_id: ID of the user.
    :param budget: New budget.
    :return: Updated user instance.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise Exception("User not found")
    user.budget = budget
    db.commit()
    db.refresh(user)
    return user
