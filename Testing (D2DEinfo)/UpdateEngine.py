#UpdateNew
import os 
CWD = os.getcwd()
BuildApp_Path = '''D:/Drago/Engine Deveploment/Drago2Dengine/__versions__/win32/'''
os.chdir(BuildApp_Path)
os.system('__init__.py')
print(os.curdir)
os.chdir('dist/build/lib.win-amd64-3.8/Drago2Dengine/__versions__/win32/dist/')
f = open('Drago2Dengine.cp38-win_amd64.pyd','rb') 
D_COPY = f.read() 
f.close()
os.chdir(CWD) 
f = open('Drago2Dengine.cp38-win_amd64.pyd','wb') 
f.write(D_COPY)
f.close()
