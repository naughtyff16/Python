import re

str="karthi welcome you to python class "

matches= re.search ("you",str)

print(matches.span())

print(matches.group())

print(matches.string)
