from enum import Enum
class Color(Enum):
    RED = "R"
    GREEN = "G"
    ORANGE = "O"
for color in Color:
    print(color.name,color.value)
