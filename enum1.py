from enum import Enum
class color(Enum):
    RED = 1
    BLUE = 2
    BLACK = 3

for color in color:
    print(color.name,color.value)
    