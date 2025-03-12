# PYTHON IMPORTS
from typing import Self
import json
import logging

# LIBRARY IMPORTS
from pydantic import BaseModel

# LOCAL IMPORTS
from api.utils.environment import Environment

# INITIALIZATION
log = logging.getLogger(__name__)

class Config(BaseModel):
    """
    The basic pydantic model that can be loaded and validated from json
    """
        
    @classmethod
    def factory(cls,filename:str,env:Environment) -> Self:
        try:
            f = open(filename)
            config = cls.model_validate(env.json_expandvars(json.load(f)))
            return config
        except Exception as e:
            log.error('Error while initializing the configuration: {0}'.format(str(e))) 
