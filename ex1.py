

import re

str="welcome to python demo regular expressions python example"

matches= re.findall ("python",str)

matchesnew= re.findall("welcome",str)

print(matches)

print("the python occurance",matches)

print(matchesnew)
