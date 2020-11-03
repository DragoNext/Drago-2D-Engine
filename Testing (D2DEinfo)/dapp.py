import sys,traceback
print(sys.argv)
f = open(sys.argv[1],'r+')

try:
    exec(f.read())
    print('executed')
except Exception as e:print(e);traceback.print_exc(file=sys.stdout)
    
input()