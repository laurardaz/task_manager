from enum import Enum

class Priority(str, Enum):
    MINOR = "Высокий"
    MEDIUM = "Средний"
    MAJOR = "Низкий"