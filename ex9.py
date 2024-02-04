import re

str1= "01234567 DOWN STREET"

mat1=re.findall("[01234]",str1)

print(mat1)

if mat1:
    print("yes the numbers are available")

else:
    print("No matching records found")
    