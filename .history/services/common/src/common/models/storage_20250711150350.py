
from typing import Optional
from beanie import Document


class File(Document):
    filename: str
    content_type: Optional[str] = None
    length: Optional[int] = None
    folder: str  # Bucket name this file is stored in
