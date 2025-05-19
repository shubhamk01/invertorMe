from pydantic import BaseModel

class NewsBase(BaseModel):
    title: str
    content: str

class NewsCreate(NewsBase):
    pass

class NewsResponse(NewsBase):
    id: int

    class Config:
        orm_mode = True
