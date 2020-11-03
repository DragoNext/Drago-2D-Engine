#Experiment Tool
#       - Build Tool 
#What it does ?
#IT unpacks Drago2Dengine and software file into the single file 
# (IT is universal can unpack any file into another) 


class BuildTool:
    def get_data(f):
        r = open(f,'r');dat = r.read();r.close();return dat
    def build(file,to):
        file_data = BuildTool.get_data(file)
        to_data = BuildTool.get_data(to) 
        
        fl = Analyze(file_data) 
        dt = Analyze(to_data)
        
        
        
        
class Analyze:
    def __init__(self,data):
        self.DATA = data 

        self.IMPORTS = [] 
        self.DEFS = [] 
        self.DEFS_DATA = []
        self.CLASS = [] 
        self.CLASS_DEF_POINTERS = []
        self.get_imports()
        
    def get_imports(self):
        self.TEMP = self.DATA
        while True:
            try:idx = self.TEMP.index('import')
            except:break 
            try:
                idy = self.TEMP.index('from')
                self.IMPORTS.append(self.TEMP[idy:].split('\n')[0])
                self.TEMP = self.TEMP.replace('from','trom',1) 
            except:
                self.IMPORTS.append(self.TEMP[idx:].split('\n')[0])
                self.TEMP = self.TEMP.replace('import','usedport',1) 
           
        
      
        
BuildTool.build('D2DEinfo.py','Drago2Dengine.py')

input()