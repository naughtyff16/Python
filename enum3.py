from enum import Enum, unique
@unique
class color(Enum):
    RED="R"
    BROWN="B"
    WHITE="W"
for color in color:
    print(color.name,color.value)
    