
# LIBRARY IMPORTS
import logging
from typing import List
import motor
from beanie import init_beanie
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorGridFSBucket


# LOCAL IMPORTS
log = logging.getLogger(__name__)

class MongodbConfig(BaseModel):
    uri: str
    name: str
    filesystem:str

class Mongodb:
    
    @staticmethod
    async def initialize(config:MongodbConfig,models:List):
        log.debug('Connecting to the database')
        db_client = motor.motor_asyncio.AsyncIOMotorClient(config.uri)
        database = db_client[config.name]
        await init_beanie(database=database, document_models=models, recreate_views=True)
        fs =AsyncIOMotorGridFSBucket(database,config.filesystem)  # Async GridFS
        log.debug('Connected to the database')
        return database, fs
        
    
    
    