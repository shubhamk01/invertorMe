from fastapi import FastAPI
import uvicorn

app = FastAPI()

from routes.user_routes import router as user_router

app.include_router(user_router, prefix="/users")

@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)