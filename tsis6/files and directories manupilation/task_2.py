import os
from string import ascii_uppercase

print('Path exists:', os.access(r'C:\', os.F_OK))
print('Path readable:', os.access(r'C:\', os.R_OK))
print('Path writable:', os.access(r'C:\', os.W_OK))
print('Path executable:', os.access(r'C:\', os.X_OK))
