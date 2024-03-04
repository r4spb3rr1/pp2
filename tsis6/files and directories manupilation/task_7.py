import os
from string import ascii_uppercase

with open('demofile.txt', 'r') as file1, open('demofile3.txt', 'a') as file2:
    for line in file1:
        file2.write(line)
