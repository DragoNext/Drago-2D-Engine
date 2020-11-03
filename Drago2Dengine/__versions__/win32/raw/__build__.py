#__build__.py 
import os 
FILES = ['__algorithms__','__draw__','__events__','__openglwindow__','__prerender__','__render__','__textureload__','__vbo__','__widgets__']
__COMMAND__ = '''python setup.py build_ext --inplace'''

CWD = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))+'\\raw'


data = ''
for f in FILES:
    d = open(dir_path+'\\__core__\\'+f+'.py','r')
    dr= d.read()
    data+=dr+'\n'
    d.close() 
data = data.replace('\t','    ')
os.chdir(os.path.dirname(os.path.realpath(__file__))+'\\dist')

data = data.replace('\n\n','\n') 

f = open('__init__.py','w')
f.write(data)
f.close()

f = open('Drago2Dengine.py','w')
f.write(data)
f.close()
##  --compiler=bcpp     Borland C++ Compiler
##  --compiler=cygwin   Cygwin port of GNU C Compiler for Win32
##  --compiler=mingw32  Mingw32 port of GNU C Compiler for Win32
##  --compiler=msvc     Microsoft Visual C++
##  --compiler=unix     standard UNIX-style compiler

os.system('''python setup.py build ''')
print('Build Updated')
