from datetime import datetime, timezone, timedelta
from uuid import uuid4

def utc_now() -> datetime:
    return datetime.now().astimezone(tz=timezone.utc)
    #return datetime.now().replace(tzinfo=timezone.utc)


def utc_now_timestamp() -> float:
    return datetime.now().astimezone(tz=timezone.utc).timestamp()
    
def utc_future_days(n: int = 5) -> datetime:
    td = timedelta(days=n)
    # your calculated date
    dt = datetime.now(timezone.utc)
    de = dt + td
    return de.replace(tzinfo=timezone.utc)


def uuid():
    return str(uuid4())

def empty_list():
    return []

def empty_string():
    return ''

def empty_dict():
    return {}

def datetime_future_days(days:int) -> datetime:
    """
    @param: days: The days in the future
    Returns the UTC Datetime in the future, based on the
    number of days given starting from today
    """
    today = utc_now()
    return today + timedelta(days=days)