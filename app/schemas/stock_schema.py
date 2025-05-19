from pydantic import BaseModel

class StockBase(BaseModel):
    symbol: str
    name: str

class StockCreate(StockBase):
    pass

class StockResponse(StockBase):
    id: int

    class Config:
        orm_mode = True
