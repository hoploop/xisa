# PYTHON IMPORTS
 
# LIBRAY IMPORTS
from pydantic import BaseModel

# LOCAL IMPORTS

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    name: str = ""
