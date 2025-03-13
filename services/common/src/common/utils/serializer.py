from datetime import datetime, timedelta
from typing import List
from uuid import uuid4

from pydantic import BaseModel

from common.utils.reflection import Reflection


class Serializer:
    
    

    @staticmethod
    def basemodel_list_to_dict_list(source: List[BaseModel]) -> List[dict]:
        """
        Converts a list of BaseModel to a list of dicts
        :param source:
        :return: A list of serialized BaseModel dictionaries
        """
        ret = []
        if source is None: return ret
        for el in source:
            ret.append(el.dict())
        return ret

    @staticmethod
    def deserialize(klass, source: dict) -> BaseModel:
        """
        Loads a BaseModel from a source dictionary
        :rtype: object
        :param klass: The target BaseModel class to be deserialized
        :param source: The source dictionary
        :return: The deserialized BaseModel class instance
        """
        return klass.parse_obj(source)

    @staticmethod
    def unmarshall(source:dict) -> BaseModel:
        """
        Loads a source dictionary containing type and data keys
        The Type should be a full signature of a BaseModel python
        class, while the data should be the serialized baseModel instance
        :param source: The dictionary to be used to load the BaseModel
        :return: The deserialized BaseModel instance
        """
        klass = Reflection.load(source['type'])
        return Serializer.deserialize(klass, source['data'])

    @staticmethod
    def serialize(source: BaseModel, by_alias: bool = True) -> dict:
        """
        Serializes a Basemodel to a dictionary
        :param source: The BaseModel to be serialized
        :param by_alias: If alias should be used as keys
        :return: The serialized dictionary
        """
        return source.dict(by_alias=by_alias)

    @staticmethod
    def marshall(source: BaseModel, by_alias: bool = True) -> dict:
        """
        Returns a dictionary of type and data, where type is the full
        python signature including the module and data is the serialized
        basemodel object
        :param source: The basemodel source
        :param by_alias: If serializatio should happen with alias
        :return: The marshalled dictionary
        """
        return {"type": Reflection.signature(source.__class__),
                "data": Serializer.serialize(source, by_alias)}

    @staticmethod
    def datetime_default() -> datetime:
        """
        Returns the current UTC datetime
        """
        today = datetime.utcnow()
        # today = pytz.UTC.localize(today)
        return today

    @staticmethod
    def datetime_today() -> datetime:
        """
        Returns the current UTC datetime
        """
        today = datetime.utcnow()
        # today = pytz.UTC.localize(today)
        return today

    @staticmethod
    def datetime_tomorrow() -> datetime:
        """
        Returns the UTC Datetime of tomorrow
        """
        today = datetime.utcnow()
        return today + timedelta(days=1)

    @staticmethod
    def datetime_future_days(days:int) -> datetime:
        """
        @param: days: The days in the future
        Returns the UTC Datetime in the future, based on the
        number of days given starting from today
        """
        today = datetime.utcnow()
        return today + timedelta(days=days)


    @staticmethod
    def uuid4_default() -> str:
        """
        Generates a uin uuid in v4 form
        """
        return str(uuid4())

    @staticmethod
    def list_default()-> list:
        return []

    @staticmethod
    def datetime_from_timestamp(value:float)-> datetime:
        return datetime.fromtimestamp(value, tz=None)

    @staticmethod
    def datetime_to_timestamp(value:datetime=datetime.utcnow())-> float:
        timestamp = datetime.timestamp(value)
        return timestamp
