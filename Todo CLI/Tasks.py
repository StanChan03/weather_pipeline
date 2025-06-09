from dataclass import dataclass
from datetime import datetime

@dataclass
class Task:
    id: int
    description: str
    created_on: datetime = datetime.utcnow()
    finished: bool


    