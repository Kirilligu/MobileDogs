from pydantic import BaseModel
from typing import Optional

class CollarCreate(BaseModel):
    unique_number: str
    characteristics: str

class DogCreate(BaseModel):
    name: str
    description: str

class DogResponse(BaseModel):
    id: int
    name: str
    description: str
    collar_id: Optional[int] = None  # Обновление: сделать это поле необязательным

    class Config:
        from_attributes = True

class CollarResponse(BaseModel):
    id: int
    unique_number: str
    characteristics: str

    class Config:
        from_attributes = True
