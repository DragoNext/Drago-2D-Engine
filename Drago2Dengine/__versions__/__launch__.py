#__launch__.py
import sys, os
version = sys.platform
print(version)
sys.path.insert(0,os.path.realpath(__file__))
if version == 'win32':
    from win32 import * 
    print('done')