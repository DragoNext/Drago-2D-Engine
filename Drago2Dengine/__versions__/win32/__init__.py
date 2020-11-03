import os, time 
try:
    dir_path = os.path.dirname(os.path.realpath(__file__))+'\\raw\\__build__.py'
    fr = open(dir_path,'r')
    exec(fr.read())
    fr.close() 
    time.sleep(1) # Wait for compiliation 
except Exception as e:print(e) 
try:
    from dist import *
except:
    from __versions__.win32.dist.__init__ import * 