import re

str5= "WE ARE INTRO NEW ERA OF PYTHON LEARNING"

mat1= re.search("NEW",str5)

print(type(mat1))

print(mat1.span())

print(mat1)
