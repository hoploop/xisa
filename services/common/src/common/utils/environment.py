import json
import os
from typing import Optional

from dotenv import load_dotenv, find_dotenv
from pathlib import Path


class Environment:

    def __init__(self,path:str):
        self.path = path
        self.init()
    
    def json_expandvars(self,o):
        """
        Returns the argument with environment variables expanded.
        Substrings of the form $name or ${name} are replaced by the value of environment variable name.
        Malformed variable names and references to non-existing variables are left unchanged.
        """
        if isinstance(o, dict):
            return {self.json_expandvars(k): self.json_expandvars(v) for k, v in o.items()}
        elif isinstance(o, list):
            return [self.json_expandvars(v) for v in o]
        elif isinstance(o, str):
            if o.startswith('i$'):
                return int(os.path.expandvars(o[1:]))
            elif o.startswith('b$'):
                return bool(os.path.expandvars(o[1:]))
            elif o.startswith('jsonfile@'):
                path = o[9:]
                value = ''
                with open(path,'r') as f:
                    data = json.load(f)
                return {self.json_expandvars(k): self.json_expandvars(v) for k, v in data.items()}
            elif o.startswith('f$'):
                path = os.path.expandvars(o[1:])
                value = ''
                with open(path,'r') as f:
                    value = f.read()
                return value
            else:
                return os.path.expandvars(o)
        else:
            return o

    
    def init(self):
        """
        Searches for .env files and loads in the current
        runtime process
        :return: None
        """


        if self.path is not None:
            dotenv_path = Path(self.path)
            load_dotenv(dotenv_path=dotenv_path)
        else:
            load_dotenv(find_dotenv())

    
    def get(self,name: str, failover: str = None) -> Optional[str]:
        """
        Loads a value from the current environment variables
        :param name: The key of the value to be loaded
        :param failover: A default failover value
        :return: A string value or None
        """
        return os.getenv(name) or failover
