# PYTHON IMPORTS
from datetime import datetime
from typing import List, Optional



# LIBRARY IMPORTS
from pydantic import BaseModel

# LOCAL IMPORTS
from common.models.workspace import Project



class ProjectListResponse(BaseModel):
    projects: List[Project]
    total: int
    