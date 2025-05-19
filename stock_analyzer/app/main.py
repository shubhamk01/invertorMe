import uvicorn
from fastapi import FastAPI
from routes import stock_routes, news_routes

app = FastAPI()

app.include_router(stock_routes.router, prefix="/api", tags=["stocks"])
app.include_router(news_routes.router, prefix="/api", tags=["news"])

@app.get("/")
def read_root():
    return {"message": "Stock Analyzer API is running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)