from enum import Enum,auto
class color(Enum):
    red=auto()
    blue=auto()
    pink=auto()
for color in color:
    print(color.name,color.value)
    