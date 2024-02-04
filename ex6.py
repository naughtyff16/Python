import re

str1="LOCKDOWN IS GOING TO RELEASED SHORTLY IN MANY PARTS OF THE WORLD AS PER SITUATIONS"

mat1=re.findall("GO",str1)

mat11=re.findall("WORLD",str1)

mat12=re.findall("SCHOOL",str1)

print(mat1)
print(mat11)
print(mat12)
