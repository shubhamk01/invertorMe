# InvertorMe

A FastAPI-based investment management platform.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run database migrations:
   ```
   alembic upgrade head
   ```
3. Run the app:
   ```
   uvicorn main:app --reload
   ```

## Features

- User management (create user, update budget)
- Stock and news management
- Portfolio and recommendations
- Database migrations with Alembic
