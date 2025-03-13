import base64
from datetime import datetime
from datetime import timezone
import json
import base64
from beanie import Document, PydanticObjectId
from bson import ObjectId
from pydantic import BaseModel

from common.rpc.base_pb2 import Serialized
from common.utils.reflection import Reflection
from google.protobuf.json_format import Parse
from google.protobuf.struct_pb2 import Struct


class Conversions:
    def utc_to_timestamp(source:datetime) -> float:
        return source.timestamp()
    
    def utc_from_timestamp(source:float) -> datetime:
        return datetime.fromtimestamp(source).astimezone(tz=timezone.utc)
        
        
    def json_serial(obj):
        """JSON serializer for objects not serializable by default json code"""

        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj,bytes):
            return base64.b64encode(obj).decode('utf-8')
        return obj
    
    
    def dump(source: BaseModel | Document) -> str:
        data = source.model_dump(by_alias=True)
        for key in data:
            if isinstance(data[key],ObjectId) or isinstance(data[key],PydanticObjectId):
                data[key] = str(data[key])
        s = json.dumps(data, default=Conversions.json_serial,ensure_ascii=False)
        return s
    
    def load(source:str) -> dict:
        return json.loads(source)
    
    def serialize(source: BaseModel | Document) -> Serialized:
        signature = '{0}.{1}'.format(source.__module__,source.__class__.__name__)
        s = Conversions.dump(source)
        return Serialized(signature=signature,data=s)
    
    def deserialize(source:Serialized) -> BaseModel | Document:
        signature = source.signature
        data = json.loads(source.data)
        clazz = Reflection.load(signature)
        instance = clazz.model_validate(data)
        return instance
    
    

    def b64encode(s:str) -> str:
        return base64.b64encode(s.encode()).decode()


    def b64decode(s:str) -> str:
        return base64.b64decode(s).decode()