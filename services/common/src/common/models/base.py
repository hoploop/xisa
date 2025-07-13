from pydantic import BaseModel


class Position(BaseModel):
    x: float 
    y: float
    
class Box(BaseModel):
    x: float
    y: float
    w: float
    h: float    