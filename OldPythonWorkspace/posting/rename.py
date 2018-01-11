import os
from os import listdir
fnames = listdir('.')
for names in fnames:
    if names.startswith('_'):
        os.rename(names, names[1:])