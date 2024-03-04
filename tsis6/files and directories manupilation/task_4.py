import os
from string import ascii_uppercase

with open(r'C:\demofile.txt', 'r') as file:
    x = len(file.readlines())
    print("Number of lines:", x)
