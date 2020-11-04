#__init__.py
#Drago2DTest.py
import cProfile
import sys, math, time, ctypes, os, numpy, random, _thread
from colorama import init
from colorama import Back,Fore,Style
from OpenGL import GL, GLU, GLUT
from OpenGL.GL import *
from OpenGL.arrays import vbo
from freetype import *
import OpenGL.GL.shaders
from OpenGL.GL import shaders
import OpenGL.WGL as WGL 
from array import array
import traceback
if sys.version_info[0] < 3 :
    from Tkinter import Tk, YES, BOTH, ttk
    import Tkinter as tk
else:
    from tkinter import Tk, YES, BOTH, ttk
    import tkinter as tk

from Drago2Dengine import D2DEvents, D2DRENDER, OpenGLFrame, D2Dprerender, D2Draw, DragoObject, create_font, load_texture, load_texture_sub   # Enigne Logic
try:
    from Drago2Dengine import D2DWidgets
except:pass 
def config_get(from_,what_):
    """ Returns value what_ from_ """ 
    from_=from_.replace(' ','') 
    d = from_[from_.index(what_+'=')+1+len(what_):].split('\n')[0]
    return d 
f = open('d2dengine.config','r') 
d2de_config = f.read() 
f.close()
config_get(d2de_config,'Error')
VSYNC_V = 144 





def __main__():
    class TRACE_MEMORYALLOCATION:
        def start():
            import tracemalloc
            tracemalloc.start()
        def end():
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics('lineno')

            f = open("Malloc.log",'w+')
            total_malloc_size = 0
            for stat in top_stats:
                total_malloc_size+=stat.size
                f.write(str(stat))
                f.write('\n\r')
            f.close()
    def scan_fonts():
        if sys.platform == 'win32':
            FONTS_PATH = "C:/Windows/winsxs/";TRUETYPE = 'truetype';TRUE_TYPE_NAMES = [];TRUE_TYPE_FILES = [];TRUE_TYPE_FIL_NAME = [];TRUE_TYPE_FONTS_DIR = [];subfolders = [f.path for f in os.scandir(FONTS_PATH) if f.is_dir() ]
            for i in subfolders:
                if TRUETYPE in i:
                    TRUE_TYPE_FONTS_DIR.append(i);TRUE_TYPE_NAMES.append(''.join(i.split(TRUETYPE+'-')[1]).split('_')[0]);d = [];r = []
                    for f in os.scandir(i):
                        d.append(f.name);r.append(f.path)
                    TRUE_TYPE_FIL_NAME.append(d);TRUE_TYPE_FILES.append(r)
                else:pass
            return TRUE_TYPE_NAMES,TRUE_TYPE_FIL_NAME,TRUE_TYPE_FILES,TRUE_TYPE_FONTS_DIR
        else:
            raise OSError("Sys Not Supported")

    init();__version__ = '057'
    def draw_text(RENDER,D2Draw,cords,color,text,font,texid,spacingaddx,spacingaddy):
        x=0;y=0
        for letter in text:
            if letter != '\r':RENDER.render_letter(D2Draw,[cords[0]+x,cords[1]+y,cords[2]+x,cords[3]+y],color,letter,font,texid);x+=spacingaddx
            else:y+=spacingaddy;x=0
    def exec_():
        print('tset')
        

    
    class AppOgl(OpenGLFrame):
        def motion_(self,ev):
            self.mouse_x = ev.x
            self.mouse_y = ev.y

        def update_motion(self,now):
            self.update_render()
        def dragbox_start(self):
            pass
        def update_render(self):
            self.render_objects = [self.background]


        def initgl(self,width=None,height=None,shift=[0,0]):
            self.x_shift = shift[0];self.y_shift = shift[1];self.camera_x = 0;self.camera_y = 0;self.prev = [0,0];self.changing = False;self.prevx = [0,0];self.win32fonts = scan_fonts();self.config(cursor='none')
            if __name__ == '__main__':
                GL.glViewport( 0, 0 , self.width, self.height);GL.glClearColor(1.0,1.0,1.0,0.0);GL.glColor3f(255.0,0.0, 0.0);GL.glPointSize(1.0);GL.glMatrixMode(GL.GL_MODELVIEW);GL.glLoadIdentity();GL.glEnable(GL.GL_BLEND);GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA);GLU.gluOrtho2D(-1.0,1.0,-1.0,1.0)
            else:
                self.width = width
                self.height = height
            self.render = D2DRENDER
            self.prerender = D2Dprerender
            self.debug_tooltip = True
            self.mouse_x = 0
            self.mouse_y = 0
            self.count_10 = 0
            self.debug_update = 0
            
            self.win32fonts = scan_fonts()
            FONT = self.win32fonts[2][32][0]
            self.fontsize = 16
            self.switch = 1
            self.mode = 0
            self.state = 0
            FONT = """./VeraMono.ttf"""
            self.gallery_boxes_overlay_data = []
            self.gallery_boxes_overlay = [] 

            self.systemfont = create_font( FONT, self.fontsize,0,1 )
            
            self.menubackground_texture = load_texture('titlescreen.png',6)

            # Total Texture units 160 
            
            # 42 - Total boxes (prepare render 2 down) 
            # 13 - Other Overlay (prepare) 
            # 5 - load  gallery
            
            # 60 total  100-60 memory managment :D
            
           
            

            
            
            
            self.manager_events = D2DEvents(root)


            ###########################################################################################################################
            self.count_10 = 0

            self.make_update = 1
            self.buff = DragoObject(800,600)
            self.widgets = D2DWidgets(self.buff,self.manager_events)
            self.menu_buff = self.buff.add_buffer()
            self.FPS = 0
            self.TOTAL_FPS = 0
            self.C_FPS = 0
            self.FP = '1000'
          
            self.letters_ = []
            self.letters_2= []
            self.letters_3= []
            self.letters_4= []
            x=0
            self.mpadx = 0
            self.mpady = -50

            self.menubg_object = self.buff.create_quad([0,0],[800,600],[0,0,0,0],self.menubackground_texture)
            
            def test(bt):
                print('Button Pressed')
            self.widgets.create_button(BUTTON_XY=[32, 34],BUTTON_SIZE=[246 ,70],BUTTON_COLOR=[0.6,0.6,0.6,1],ON_CLICK=test,TEXT='Button Widget')
            self.widgets.create_dropbox(DROP_XY=[33,130],  DROP_SIZE=[246 ,58], DROP_COLOR=[0.6,0.6,0.6,1],ENTRIES=['test','test2','test3'])
            

            if self.debug_tooltip is True:
                for i in 'fps 0000':
                    self.lett = self.buff.create_letter([0,0,0,0],self.systemfont,i,[0,1,0,0],1)
                    self.letters_.append(self.lett)
                for i in 'x ----':
                    lett = self.buff.create_letter([0,0,0,0],self.systemfont,i,[0,1,0,0],1)
                    self.letters_2.append(lett)
                for i in 'y ----':
                    lett = self.buff.create_letter([0,0,0,0],self.systemfont,i,[0,1,0,0],1)
                    self.letters_3.append(lett)
                for i in 'u ----':
                    lett = self.buff.create_letter([0,0,0,0],self.systemfont,i,[0,1,0,0],1)
                    self.letters_4.append(lett)


            self.cursor_obj = self.buff.create_quad([self.mouse_x-3,self.mouse_y-3],[6,6],[1,0,1,1])
            
            
       
            
            self.FP = '000'
            self.gl_once = 0 
            #self.buff.create_text(cords=[100,100],color=(1,0,0),text='DragoTestVbo',font=self.systemfont,texid=3,screensize=[640,400])
            self.debug_update = time.time()

            self.buff.compile()
            self.delay_frame = 0
            self.shader = self.buff.get_shader()
        
            GL.glDisable(GL.GL_DEPTH_TEST)

            self.manager_events.add_event(EventType='KeyPress',EventOn=self.KeyPressEvent)

            # 119/70
        #InitglEnd
        def KeyPressEvent(self,ev):
            if ev.char == 'q':
                try:
                    self.buff.set_mode(0)
                except Exception as e:
                    print(e)
            if ev.char =='w':
                try:
                    self.buff.set_mode(1)
                except Exception as e:
                    print(e)
        
        def freecalc(self):
            #Dosent affect main perfomance :)
            self.free_calc_update()
            
        #FreecalcEnd

       
        def update_fps_display(self):
            if time.time()-self.debug_update > 0.3:
                self.debug_update = time.time()
                xd=0
                self.buff.edit_letter(self.letters_[-4],self.systemfont,str(self.FP)[0])
                self.buff.edit_letter(self.letters_[-3],self.systemfont,str(self.FP)[1])
                self.buff.edit_letter(self.letters_[-2],self.systemfont,str(self.FP)[2])
                self.buff.edit_letter(self.letters_[-1],self.systemfont,str(self.FP)[3])
                msx = str(self.mouse_x).zfill(4)
                self.buff.edit_letter(self.letters_2[-4],self.systemfont,str(msx)[0])
                self.buff.edit_letter(self.letters_2[-3],self.systemfont,str(msx)[1])
                self.buff.edit_letter(self.letters_2[-2],self.systemfont,str(msx)[2])
                self.buff.edit_letter(self.letters_2[-1],self.systemfont,str(msx)[3])
                msx = str(self.mouse_y).zfill(4)
                self.buff.edit_letter(self.letters_3[-4],self.systemfont,str(msx)[0])
                self.buff.edit_letter(self.letters_3[-3],self.systemfont,str(msx)[1])
                self.buff.edit_letter(self.letters_3[-2],self.systemfont,str(msx)[2])
                self.buff.edit_letter(self.letters_3[-1],self.systemfont,str(msx)[3])
                msx = str(self.buff.total_updates).zfill(4)
                self.buff.edit_letter(self.letters_4[-4],self.systemfont,str(msx)[0])
                self.buff.edit_letter(self.letters_4[-3],self.systemfont,str(msx)[1])
                self.buff.edit_letter(self.letters_4[-2],self.systemfont,str(msx)[2])
                self.buff.edit_letter(self.letters_4[-1],self.systemfont,str(msx)[3])
            xd=0
            for i in self.letters_:
               self.buff.edit_pos(i,[self.mouse_x+24+xd,self.mouse_y-24],[16,16],letter=True)
               xd+=10
            xd=0
            for i in self.letters_2:
               self.buff.edit_pos(i,[self.mouse_x+24+xd,self.mouse_y-10],[16,16],letter=True)
               xd+=10
            xd=0
            for i in self.letters_3:
               self.buff.edit_pos(i,[self.mouse_x+24+xd,self.mouse_y+2],[16,16],letter=True)
               xd+=10
            xd=0
            for i in self.letters_4:
               self.buff.edit_pos(i,[self.mouse_x+24+xd,self.mouse_y+14],[16,16],letter=True)
               xd+=10
               
        def _pass(self):
            pass
        def redraw(self):
            self.update_fps_display()
            if self.debug_tooltip is True:
                if self.make_update is 1:
                    shaders.glUseProgram(self.shader)
                    self.make_update = 0
    

                    if self.switch == 1:
                            self.switch = 0
                            self.buff.set_mode(self.mode)
                    for i in range(0,2):
                        GL.glClearColor(0,0,0,1)
                        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
                        self.buff.draw()
                        xd=0
                        self.buff.edit_pos(self.cursor_obj,[self.mouse_x-3,self.mouse_y-3],[6,6])

                        self.buff.update()
                        self.tkSwapBuffers( )

                    shaders.glUseProgram(0)
                self.make_update = 1


       
       
       
            if self.C_FPS != 0:
                self.FP = str(self.TOTAL_FPS/self.C_FPS)
        
            self.FP = self.FP.zfill(4)
            self.C_FPS+=1
            self.FPS = self.redraw_perfomance
            if self.FPS != 0:
                self.TOTAL_FPS+=1/self.FPS
          


           


            
        
            
        #RedrawEnd
    language = 'pol'
    if __name__ == '__main__':

        root = Tk()
        root.resizable(0,0)
      
        app = AppOgl(root, width=800, height=600, highlightthickness=0, relief='ridge')
        app.pack(fill=BOTH, expand=YES)
        app.animate=0
        app.bind('<Motion>',app.motion_)
        app.after(100, app.printContext) #Context not needed
        #app.mainloop() 


if __name__ == "__main__":
    print(os.getcwd()) 
    __main__()
    input('Press Enter to end')

