import base64
from datetime import datetime
from datetime import timezone
import json
import base64
from typing import List, Type
from beanie import Document, PydanticObjectId
from bson import ObjectId
from pydantic import BaseModel

from common.rpc.base_pb2 import Serialized
from common.utils.reflection import Reflection
from google.protobuf.json_format import Parse
from google.protobuf.struct_pb2 import Struct
from pydantic import BaseModel
from beanie import Document
from google.protobuf.message import Message
from google.protobuf.descriptor import FieldDescriptor
from typing import Type, Any

class Conversions:
    def utc_to_timestamp(source:datetime) -> float:
        return source.timestamp()
    
    from typing import List

    def grpc_to_beanie(grpc_cls: Type[Message]) -> Type[Document]:
        fields = {}
        for field in grpc_cls.DESCRIPTOR.fields:
            if field.type == 11:  # Nested Message
                nested_cls = Conversions.grpc_to_beanie(field.message_type._concrete_class)
                fields[field.name] = (nested_cls, ...)
            elif field.label == 3:  # REPEATED
                fields[field.name] = (List[Any], ...)
            elif field.type == 9:  # STRING
                fields[field.name] = (str, ...)
            elif field.type == 5:  # INT32
                fields[field.name] = (int, ...)
            elif field.type == 1:  # DOUBLE
                fields[field.name] = (float, ...)
            elif field.type == 8:  # BOOL
                fields[field.name] = (bool, ...)
            else:
                fields[field.name] = (Any, ...)

        model_name = grpc_cls.__name__ + "Document"
        return type(model_name, (Document,), fields)
    
        
    
    def grpc_to_pydantic(grpc_cls: Type[Message]) -> Type[BaseModel]:
        """
        Convert a gRPC message class to a Pydantic model, supporting nested messages.
        """
        fields = {}
        for field in grpc_cls.DESCRIPTOR.fields:
            if field.type == 11:  # MESSAGE (nested)
                nested_cls = Conversions.grpc_to_pydantic(field.message_type._concrete_class)
                fields[field.name] = (nested_cls, None)
            elif field.type == 9:  # STRING
                fields[field.name] = (str, None)
            elif field.type == 5:  # INT32
                fields[field.name] = (int, None)
            elif field.type == 1:  # DOUBLE
                fields[field.name] = (float, None)
            elif field.type == 8:  # BOOL
                fields[field.name] = (bool, None)

        return type(grpc_cls.__name__ + "Model", (BaseModel,), fields)
    
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
        s = source.model_dump_json(by_alias=True)
        #for key in data:
        #    if isinstance(data[key],ObjectId) or isinstance(data[key],PydanticObjectId):
        #        data[key] = str(data[key])
        #s = json.dumps(data, default=Conversions.json_serial,ensure_ascii=False)
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