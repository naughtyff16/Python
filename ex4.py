import re

str1="ENTIRE WORLD IS IN PANIC"

mat1= re.split("\s",str1)
print(mat1)

mat11=re.split("\s",str1,1)
print(mat11)

mat12= re.split("\s",str1,2)
print(mat12)
