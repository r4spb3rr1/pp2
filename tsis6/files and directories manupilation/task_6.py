import os
from string import ascii_uppercase

for char in ascii_uppercase:
    file = open(r'C:\week6\{fchar}.txt'.format(fchar = char), 'x')
    file.close()
