
from beanie import Document


class FileMetadata(Document):
    filename: str
    content_type: Optional[str] = None
    length: Optional[int] = None
