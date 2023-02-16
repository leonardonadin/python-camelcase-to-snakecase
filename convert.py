import sys
import re

string = sys.argv[1]

string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
string = re.sub('__([A-Z])', r'_\1', string)
string = re.sub('([a-z0-9])([A-Z])', r'\1_\2', string)

converted_string = string.lower()

print(converted_string)