import os
from string import ascii_uppercase

mylist = ['A', 'B', 'C', 'D']
with open(r'C:\demofile2.txt', 'w') as file:
    for i in mylist:
        file.write(i + '\n')
file.close()
