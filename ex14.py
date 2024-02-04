import json

x={
    "name": "madan",
    "age": 27,
    "married": True,
    "divorced": False,
    "children": ("harika,shivani"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg":24.1}
    ]
}

print(json.dumps(x,indent=4,separators=(".","=")))