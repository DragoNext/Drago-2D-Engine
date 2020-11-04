#Breshenham line algorithm
if __name__ == '__main__':
    import math
def naiveline(x1,y1,x2,y2):
    points = []
    rise = y2-y1 
    run =   x2-x1 
    if run == 0:
        if y2 < y1:
            y1, y2 = (y2, y1)
        for y in range(y1,y2+1):
            points.append([x1,y])
    else:
        m = float(rise)/run 
        b = y1 - m * x1 
        if m <= 1 and m >= -1:
            if x2 < x1:
                x1, x2 = (x2, x1 )
            for x in range(x1,x2+1):
                y = int(round(m*x+b))
                points.append([x,y])
        else:
            if y2 < y1:
                y1, y2 = (y2,y1)
            for y in range(y1,y2+1):
                x = int(round((y-b)/m))
                points.append([x,y])
                
                
                
    return points    
def bresenham(x1,y1,x2, y2):  #Line Drawing
    m_new = 2 * (y2 - y1)  
    slope_error_new = m_new - (x2 - x1) 
    y=y1 
    points = []
    for x in range(x1,x2+1):  
        points.append([x,y])
        slope_error_new+= m_new  
        if (slope_error_new >= 0):  
            y=y+1
            slope_error_new =slope_error_new - 2 * (x2 - x1)  
            
    return points 
class D2Draw: # <<<<<<<<< STATIC DRAW 
    def __init__(self,screen_res):
        self.size = screen_res
        self.newsize= (0,0)
        self.nx = 0
        self.ny = 0
        self.centre = (screen_res[0]/2,screen_res[1]/2) #x,y
        self.pix_rat_x = 2/(screen_res[0])
        self.pix_rat_y = 2/(screen_res[1])
        
    def _resize(self):
        self.nx = self.orgsize[0]-self.newsize[0]
        self.ny = self.orgsize[1]-self.newsize[1]
           
    def resize(self,newsize,orgsize):
        self.newsize = newsize
        self.orgsize = orgsize 
        self._resize()
            
    def _cords_to_ratio(self,x,y):
        xr = x*self.pix_rat_x
        yr = y*self.pix_rat_y
        if xr > 1:
            xr = xr-1 
        else:
            xr = xr-1    
        if yr > 1:
            yr = 1-yr
        else:
            yr = 1-yr
        return (xr,yr)
        
        
    def _texture_cords_to_ratio(self,x,y,size):
        xr = x*(2/size[0])
        yr = y*(2/size[1])
        if xr > 1:
            xr = xr-1 
        else:
            xr = -(1-xr)  
        if yr > 1:
            yr = (1-yr) 
        else:
            yr = -(yr-1)
        return (xr,yr)
        
        
        
    def _tex_arrayn_translate(self,n=[0,0],s=0,txs=[0,0]):
        ''' n = x,y  s = size  txs - texturesize  '''    
        x1 = (n[0]*s)-s
        y1 = (n[1]*s)-s
        x2 = (n[0]*s)
        y2 = (n[1]*s) 
        _c1 =self._texture_cords_to_ratio(x1,y1,txs)
        _c2 =self._texture_cords_to_ratio(x2,y2,txs)
            
            
        return _c1,_c2  
        
        
        
        
    def draw_quad(self,cords=[],color=(),rotate=None,alpha=1):
        GL.glBegin(GL.GL_QUADS)
        GL.glColor4f(color[0],color[1],color[2],alpha)
        tr1 = self._cords_to_ratio(cords[0],cords[1])
        tr2 = self._cords_to_ratio(cords[2]-self.nx,cords[3]-self.ny)
        
        GL.glVertex2f(tr1[0], tr1[1])
        GL.glVertex2f(tr1[0],tr2[1])
        GL.glVertex2f(tr2[0], tr2[1])
        GL.glVertex2f(tr2[0],tr1[1])
        GL.glEnd()
        
        
        
        
    def draw_quad_texture(self,cords=[],color=(),textr=None,NOENABLE=False):
        if NOENABLE is True:
            pass
        else:
            GL.glEnable(GL.GL_TEXTURE_2D)
            GL.glBindTexture(GL.GL_TEXTURE_2D, textr)
            GL.glColor3f(color[0],color[1],color[2]) 
            GL.glBegin(GL.GL_QUADS)     
            
        tr1 = self._cords_to_ratio(cords[0],cords[1])
        tr2 = self._cords_to_ratio(cords[2]-self.nx,cords[3]-self.ny)
      
            
        GL.glTexCoord2f(1, 1)
        GL.glVertex2f(tr2[0], tr2[1])
            
        GL.glTexCoord2f(0, 1)
        GL.glVertex2f(tr1[0],tr2[1])
            
        GL.glTexCoord2f(0, 0)
        GL.glVertex2f(tr1[0], tr1[1])
        GL.glTexCoord2f(1, 0)
        GL.glVertex2f(tr2[0],tr1[1])
         
         
         
        if NOENABLE is True:
            pass
        else:
            GL.glEnd()
            GL.glDisable(GL.GL_TEXTURE_2D)
        
        
    def draw_point(self,cords=(1,1),color=(255,255,255)):
        tr1 = self._cords_to_ratio(cords[0],cords[1])
        GL.glBegin(GL.GL_POINTS)
        GL.glColor3f(color[0],color[1],color[2])
        GL.glVertex2f(tr1[0],tr1[1])
        GL.glEnd()
    def draw_points():
        pass#DFPASS  
    def draw_line(self,cords=[],color=()):                                 # COMPLETE < Breneshman Done just Drawing LOGIC (CORDS translation)
        tr1 = bresenham(int(cords[0]),int(cords[1]),int(cords[2]),int(cords[3]))
        pixels = []
        x=0
        for i in tr1:
            pixels.append(self._cords_to_ratio(i[0],i[1]))
            x+=1
        GL.glBegin(GL.GL_POINTS)
        GL.glColor3f(color[0],color[1],color[2])
        for i in pixels:
            GL.glVertex2f(i[0],i[1])
        GL.glEnd()
    def draw_lines():
        pass#DFPASS 
        
    def draw_text(self,cords=[],color=(),font_texture=None,font_letters=[],text='abcdefgh',config=(256,256,8),font_config=('Spacing_add','size_x','size_y')):  
        color=color
        textr=font_texture
        GL.glEnable(GL.GL_TEXTURE_2D)
        GL.glBindTexture(GL.GL_TEXTURE_2D, textr)
        GL.glBegin(GL.GL_QUADS)
        GL.glColor3f(color[0],color[1],color[2])
        spacing = 0
        spacing_addx=10
        spacing_addy=16
        size_x = 16
        size_y = 16
        r=0
        y=0
        spacing_y=0
        add_boldnext=0
        for i in text:
            yr=0
            x=0
            l=i 
            if i == '/' or r == 1:
                r=1 
                if i == 'n':
                    spacing_y+=spacing_addy
                    spacing=0
                    r=0
                if i == 'b':
                    add_boldnext = 1
                    r=0
                else:pass
            else:
                if add_boldnext == 1:
                    l='[b]'+l
                    add_boldnext=0
                for ls in font_letters:
                    try:
                        x = font_letters[yr].index(l)
                        y = yr
                    except:pass 
                    yr+=1
                x=-x
                y=-y-1
                spacing+=spacing_addx
                cords_=[cords[0]+spacing,cords[1]+spacing_y,cords[0]+size_x+spacing,cords[1]+size_y+spacing_y]
                textn=([x,y],config[2],(config[0],config[1]))
                tr1 = self._cords_to_ratio(cords_[0],cords_[1])
                tr2 = self._cords_to_ratio(cords_[2]-self.nx,cords_[3]-self.ny)
                txn = self._tex_arrayn_translate(textn[0],textn[1],textn[2])
                
                GL.glTexCoord2f(txn[0][0], txn[1][1])
                GL.glVertex2f(tr2[0],tr1[1])
                GL.glTexCoord2f(txn[0][0], txn[0][1])
                GL.glVertex2f(tr2[0], tr2[1])
                GL.glTexCoord2f(txn[1][0], txn[0][1])
                GL.glVertex2f(tr1[0],tr2[1])
                GL.glTexCoord2f(txn[1][0], txn[1][1])
                GL.glVertex2f(tr1[0], tr1[1])
                    
        GL.glEnd()
    
    def draw_quad_texture_array(self,cords=[],color=(),textr=None,textn=([0,0],32,[0,0])): #-------------------TO do logic of dividing textures -1 -1 to 1 1 
        '''textn - Texture split > [x , y [AS N] , [SizeOfOneSpirit], [texturesize x,y] '''
        #
        # textn > x  , y
        #
        GL.glEnable(GL.GL_TEXTURE_2D)
        GL.glBindTexture(GL.GL_TEXTURE_2D, textr)
        GL.glBegin(GL.GL_QUADS)
        GL.glColor3f(color[0],color[1],color[2])
        tr1 = self._cords_to_ratio(cords[0],cords[1])
        tr2 = self._cords_to_ratio(cords[2]-self.nx,cords[3]-self.ny)
            
        txn = self._tex_arrayn_translate(textn[0],textn[1],textn[2])
       
        #GL.glTexCoord2f(1,0)
        GL.glTexCoord2f(txn[0][0], txn[1][1])
        GL.glVertex2f(tr2[0],tr1[1])
        #GL.glTexCoord2f(1,1)
        GL.glTexCoord2f(txn[0][0], txn[0][1])
        GL.glVertex2f(tr2[0], tr2[1])
        #GL.glTexCoord2f(0,1)
        GL.glTexCoord2f(txn[1][0], txn[0][1])
        GL.glVertex2f(tr1[0],tr2[1])
        #GL.glTexCoord2f(0,0)
        GL.glTexCoord2f(txn[1][0], txn[1][1])
        GL.glVertex2f(tr1[0], tr1[1])
            
            
        GL.glEnd()
    
        
    def add_animation():
        pass#DFPASS 
    def update_animation():
        pass#DFPASS  
    def del_animation():
        pass#DFPASS 
#__init__ file.
#Some usefull animation events 
# pre pepared (animation etc) 
def change_color(object,from_,to_):
    pass 
   
class D2DEvents:
    def __init__(self,cvroot):
        '''
        Event_Type - 
            {0:'Button-1':'MouseLC'}
            {1:'Button-2':'MouseRC'}
            {2:'Button-3':'MouseMC'}
            {3:'Motion':'MouseHover'}
            {4:'KeyPress',:'OnKey'} 
        Event Action Start/End - 
            if None def _pas
            Assing function
        CORDS_NEEDED -
            [FromX1,FromY1,
            ToX2,ToY2]'''
        self.evt = {0:'Button-1',0:'MouseLC',
               1:'Button-3',0:'MouseRC',
               2:'Button-2',0:'MouseMC',
               3:'Motion',0:'MouseHover',
               4:'KeyPress',0:'OnKey'}
        self.master = cvroot 
        
        self.hover_events    = []
        self.rclick_events   = []
        self.lclick_events   = []
        self.mclick_events   = []
        self.keypress_events = []
        
        self.master.bind('<Motion>',self.checkmotion)
        self.master.bind('<Button-1>',self.checkrclick)
        self.master.bind('<Button-3>',self.checklclick)
        self.master.bind('<Button-2>',self.checkmclick)
        self.master.bind('<KeyPress>',self.checkkeypress)
    def clear_events(self):
        self.hover_events    = [];self.rclick_events   = [];self.lclick_events   = [];self.mclick_events   = [];self.keypress_events = []
    def checkkeypress(self,ev):
        for i in self.keypress_events:
            i[0](ev)
    def checkmclick(self,ev):
        c=0
        t = False 
        for event in self.mclick_events:
            x = ev.x 
            y = ev.y 
            cords = event[1]
            launchev = event[2]
            previoev = event[3]
            state = event[4]
            delay = event[5]
            if x >= cords[0]:
                if y >= cords[1]:
                    if x <= cords[2]:
                        if y <= cords[3]:
                            if state != True:
                                if type(launchev) != tuple:
                                    launchev()
                                else:launchev[0](launchev[1:]) 
                            self.mclick_events[c][4] = True 
            self.mclick_events[c][4] = False 
            if type(previoev) != tuple:
                self.master.after(delay,previoev)   
            else:self.master.after(delay,previoev[0],previoev[1:])   
          
            c+=1 
    def checklclick(self,ev):
        c=0
        t = False 
        for event in self.lclick_events:
            x = ev.x 
            y = ev.y 
            cords = event[1]
            launchev = event[2]
            previoev = event[3]
            state = event[4]
            delay = event[5]
            if x >= cords[0]:
                if y >= cords[1]:
                    if x <= cords[2]:
                        if y <= cords[3]:
                            if state != True:
                                if type(launchev) != tuple:
                                    launchev()
                                else:launchev[0](launchev[1:]) 
                            self.lclick_events[c][4] = True 
            self.lclick_events[c][4] = False 
            if type(previoev) != tuple:
                self.master.after(delay,previoev)   
            else:self.master.after(delay,previoev[0],previoev[1:])   
            c+=1 
    def checkrclick(self,ev):
        c=0
        t = False 
        for event in self.rclick_events:
            x = ev.x 
            y = ev.y 
            cords = event[1]
            launchev = event[2]
            previoev = event[3]
            state = event[4]
            delay = event[5]
            if x >= cords[0]:
                if y >= cords[1]:
                    if x <= cords[2]:
                        if y <= cords[3]:
                            if state != True:
                                if type(launchev) != tuple:
                                    launchev()
                                else:launchev[0](launchev[1:]) 
                            self.rclick_events[c][4] = True 
            self.rclick_events[c][4] = False 
            if type(previoev) != tuple:
                self.master.after(delay,previoev)   
            else:self.master.after(delay,previoev[0],previoev[1:])    
            c+=1 
            
     
    def checkmotion(self,ev):
        c=0
        
        for event in self.hover_events:
            t = False 
            x = ev.x 
            y = ev.y 
            cords = event[1]
            launchev = event[2]
            previoev = event[3]
            state = event[4]
            delay = event[5]
            if x >= cords[0]:
                if y >= cords[1]:
                    if x <= cords[2]:
                        if y <= cords[3]:
                            if type(launchev) != tuple:
                                launchev()
                            else:launchev[0](launchev[1:]) 
                            self.hover_events[c][4] = True 
                        else:t = True 
                    else:t = True 
                else:t = True 
            else:t = True 
            if t == True:
                if state == True:
                    self.hover_events[c][4] = False 
                    if type(previoev) != tuple:
                        self.master.after(delay,previoev)   
                    else:
                        self.master.after(delay,previoev[0],previoev[1:])   
                    
            c+=1 
        
        
    def add_event(self,EventType=None,Cords=None,EventOn=None,EventOff=None,EventDelay=None):
        if type(EventType) is int:
            dat = self.evt.get(EventType) 
        else:dat = EventType
        if dat == 'Motion' or dat == 'Hover' or dat == 'MouseHover':
            event = [0]
            event.append(Cords)
            event.append(EventOn)
            event.append(EventOff)
            event.append(False)
            event.append(EventDelay)
            self.hover_events.append(event)
            return True 
        if dat == 'Button-1' or dat == 'MouseLC' or dat == 'LeftClick':
            event = [0]
            event.append(Cords)
            event.append(EventOn)
            event.append(EventOff)
            event.append(False)
            event.append(EventDelay)
            self.rclick_events.append(event)
            return True 
        if dat == 'Button-2' or dat == 'MouseRC' or dat == 'RightClick':
            event = [0]
            event.append(Cords)
            event.append(EventOn)
            event.append(EventOff)
            event.append(False)
            event.append(EventDelay)
            self.lclick_events.append(event)
            return True 
        if dat == 'Button-3' or dat == 'MouseMC' or dat == 'MiddleClick':
            event = [0]
            event.append(Cords)
            event.append(EventOn)
            event.append(EventOff)
            event.append(False)
            event.append(EventDelay)
            self.mclick_events.append(event)
            return True 
        if dat == 'KeyPress':
            event = []
            event.append(EventOn)
            self.keypress_events.append(event)
            return True 
            
            
    def check(self,ev,lfg,lfm,lfe):
        if ev.x <= self.crd[0]:
            if ev.y <= self.crd[1]:
                if ev.x >= self.crd[2]:
                    if ev.y >= self.crd[3]:
                        launch_function_beg()
                        launch_function_mid()
                        launch_function_end()
    def _pas(self):
        pass#DFPASS  #._.
#__init__ file.
## TK opgl Window:
# An opengl frame for pyopengl-tkinter based on ctypes (no togl compilation)
#
# Collected together by Jon Wright, Jan 2018.
#
# Based on the work of others:
# C + Tcl/Tk
# http://github.com/codeplea/opengl-tcltk/
# (zlib license)
# Article at:
#   https://codeplea.com/opengl-with-c-and-tcl-tk
# Python + Tkinter (no pyopengl)
# http://github.com/arcanosam/pytkogl/
# (The Code Project Open License)
# Article at 
#  http://www.codeproject.com/Articles/1073475/OpenGL-in-Python-with-TKinter
# Large parts copied from pyopengl/Tk/__init__.py
# Edited by drago 
#  fo Drago2dengine private project 
import sys, math, time, random
from OpenGL import GL, GLU
from OpenGL import GL, GLUT
from OpenGL.GL import *
import _thread as th
if sys.version_info[0] < 3:
    import Tkinter as tk
    import Dialog as dialog
else:
    import tkinter as tk
    from tkinter import dialog as dialog
__all__ = [  'OpenGLFrame', 'RawOpengl', 'Opengl', 
        'v3distsq' ]
class baseOpenGLFrame(tk.Frame):
    """ Common code for windows/x11 """
    ## On cords 
    def check_all_b1_events(self,event):
        for i in self.events_B1:
            c = i[0]
            if event.x > c[0]:
                if event.x < c[2]:
                    if event.y > c[1]:
                        if event.y < c[3]:
                            i[1]()
    def check_all_brelase_events(self,event):
        for i in self.events_BR:
            c = i[0]
            if event.x > c[0]:
                if event.x < c[2]:
                    if event.y > c[1]:
                        if event.y < c[3]:
                            i[1]()                        
    def check_all_bpress_events(self,event):
        for i in self.events_BP:
            c = i[0]
            if event.x > c[0]:
                if event.x < c[2]:
                    if event.y > c[1]:
                        if event.y < c[3]:
                            i[1]()  
    def create_event(self,cords,launch_func,event_type):
        if event_type is self.ev_type[0]:
           self.events_B1.append([cords, launch_func]) 
        if event_type is self.ev_type[1]:
           self.events_B2.append([cords, launch_func])  
        if event_type is self.ev_type[2]:
           self.events_B3.append([cords, launch_func]) 
        if event_type is self.ev_type[3]:
           self.events_MN.append([cords, launch_func]) 
        if event_type is self.ev_type[4]:
           self.events_BR.append([cords, launch_func]) 
        if event_type is self.ev_type[5]:
           self.events_BP.append([cords, launch_func]) 
    def check_event_button_1(self,event,c,func):
        if event.x > c[0]:
            if c[2] > event.x:
                if event.y > c[1]:
                    if c[2] > event.y:
                        func()
            
    def __init__(self, *args, **kw):
        # Set background to empty string to avoid 
        # flickering overdraw by Tk
        kw['bg'] ="" 
        tk.Frame.__init__( self, *args, **kw )
        self.bind('<Map>', self.tkMap )
        self.bind('<Configure>', self.tkResize )
        self.bind('<Expose>', self.tkExpose )
        self.bind('<Button-1>',self.check_all_b1_events)
        
        #self.bind('<ButtonPress>',self.check_all_bpress_events)
        #self.bind('<ButtonRelease>',self.check_all_brelase_events)
        
        self.animate = 0
        self.cb = None
        self.freecalc_update = 1
        self.ev_list = []
        self.events_B1 = [] 
        self.events_B2 = [] 
        self.events_B3 = []
        self.events_MN = []
        self.events_BR = []   
        self.events_BP = []         
        self.ev_type = ['B1','B2','B3','MN','BR','BP'] # B - button MN - Motion
        
        # MeasurIng Performance Logic 
        self.dump_to_log = False ## Should be dumped to log ;l 
        self.PrintContext_performance = 0 
        self.redraw_perfomance = 0 
        
    def tkMap( self, evt ):
        """" Called when frame goes onto the screen """
        self._wid = self.winfo_id()
        self.tkCreateContext( )
        self.initgl()
    def printContext(self, extns=False):
        """ For debugging """
        st = time.time()
        exts = GL.glGetString(GL.GL_EXTENSIONS)
        if extns:
            print("Extension list:")        
            for e in sorted(exts.split()):
                print(  "\t", e )
        else:
            print("Number of extensions:",len(exts.split()))
        print( "GL_VENDOR  :",GL.glGetString(GL.GL_VENDOR))
        print( "GL_RENDERER:",GL.glGetString(GL.GL_RENDERER))
        print( "GL_VERSION :",GL.glGetString(GL.GL_VERSION))
        try:
            print(" GL_MAJOR_VERSION:", GL.glGetIntegerv( GL.GL_MAJOR_VERSION ))
            print(" GL_MINOR_VERSION:", GL.glGetIntegerv( GL.GL_MINOR_VERSION ))
            print(" GL_SHADING_LANGUAGE_VERSION :", 
                    GL.glGetString(GL.GL_SHADING_LANGUAGE_VERSION))
            msk = GL.glGetIntegerv(GL.GL_CONTEXT_PROFILE_MASK)
            print(" GL_CONTEXT_CORE_PROFILE_BIT :",
                   bool( msk & GL.GL_CONTEXT_CORE_PROFILE_BIT) )
            print(" GL_CONTEXT_COMPATIBILITY_PROFILE_BIT :",
                   bool( msk & GL.GL_CONTEXT_COMPATIBILITY_PROFILE_BIT) )
        except:
            print("Old context errors arose")
            # raise
        self.PrintContext_performance = time.time()-st 
    def tkCreateContext( self ):
        # Platform dependent part
        raise NotImplementedError
    def tkMakeCurrent( self ):
        # Platform dependent part
        raise NotImplementedError
    def tkSwapBuffers( self ): 
        # Platform dependent part
        raise NotImplementedError
    def tkExpose( self, evt):
        if self.cb:
            self.after_cancel(self.cb)
        self._display()
    def tkResize( self, evt ):
        """
        Things to do on window resize:
        Adjust viewport:
            glViewPort(0,0, width, height)
        Adjust projection matrix:
            glFrustum(left * ratio, right * ratio, bottom, top, nearClip,farClip)
        or
            glOrtho(left * ratio, right * ratio, bottom, top, nearClip,farClip)
        or
            gluOrtho2D(left * ratio, right * ratio, bottom, top)
        (assuming that left, right, bottom and top are all equal and
         ratio=width/height)
        """
        self.width, self.height = evt.width, evt.height
        if self.winfo_ismapped():
            GL.glViewport( 0, 0, self.width, self.height )
            self.initgl()
            
    def _display(self):
        if self.freecalc_update is 1:
            self.freecalc_update=0
            th.start_new_thread(self.freecalc,())
        self.update_idletasks()
        self.tkMakeCurrent()
        st = time.time()
        self.redraw()
        self.redraw_perfomance = time.time()-st 
        if self.animate >= 0:
            self.cb = self.after(self.animate, self._display )
        
    def initgl(self): 
        # For the user code
        raise NotImplementedError
    def freecalc(self):
        #for user code 2 
        raise NotImplementedError 
    def redraw(self):
        # For the user code
        raise NotImplementedError
    def wait(self,t):
        time.sleep(t)
    def free_calc_update(self):
        self.freecalc_update = 1
###############################################################################
# Windows specific code here:
if sys.platform.startswith( 'win32' ):
    from ctypes import WinDLL, c_void_p, sizeof
    from ctypes.wintypes import HDC, BOOL
    from OpenGL.WGL import PIXELFORMATDESCRIPTOR, ChoosePixelFormat, \
            SetPixelFormat, SwapBuffers, wglCreateContext, wglMakeCurrent
    _user32 = WinDLL('user32')
    GetDC = _user32.GetDC
    GetDC.restype = HDC
    GetDC.argtypes = [c_void_p]
    pfd = PIXELFORMATDESCRIPTOR()
    PFD_TYPE_RGBA =         0
    PFD_MAIN_PLANE =        0
    PFD_DOUBLEBUFFER =      0x00000001
    PFD_DRAW_TO_WINDOW =    0x00000004
    PFD_SUPPORT_OPENGL =    0x00000020
    pfd.dwFlags = PFD_DRAW_TO_WINDOW | PFD_SUPPORT_OPENGL | PFD_DOUBLEBUFFER
    pfd.iPixelType = PFD_TYPE_RGBA
    pfd.cColorBits = 24
    pfd.cDepthBits = 16
    pfd.iLayerType = PFD_MAIN_PLANE
    # Inherits the base and fills in the 3 platform dependent functions
    class OpenGLFrame( baseOpenGLFrame ):
        
        def tkCreateContext( self ):
            self.__window = GetDC(self.winfo_id())
            pixelformat = ChoosePixelFormat(self.__window, pfd)
            SetPixelFormat(self.__window, pixelformat, pfd)
            self.__context = wglCreateContext(self.__window)
            wglMakeCurrent(self.__window, self.__context)
           
        def tkMakeCurrent( self ):
            if self.winfo_ismapped():
                wglMakeCurrent( self.__window, self.__context)
    
        def tkSwapBuffers( self ):
            if self.winfo_ismapped():
                SwapBuffers(self.__window) 
# END Windows specific code
###############################################################################
# Linux/X11 specific code here:  
if sys.platform.startswith( 'linux' ):
    from ctypes import c_int, c_char_p, c_void_p, cdll, POINTER, util, \
        pointer, CFUNCTYPE, c_bool
    from OpenGL import GLX
    try:
        from OpenGL.raw._GLX import Display
    except:
        from OpenGL.raw.GLX._types import Display
    
    _x11lib = cdll.LoadLibrary(util.find_library( "X11" ) )
    XOpenDisplay = _x11lib.XOpenDisplay
    XOpenDisplay.argtypes = [c_char_p]
    XOpenDisplay.restype = POINTER(Display)
    
    Colormap = c_void_p
    # Attributes for old style creation
    att = [     GLX.GLX_RGBA, GLX.GLX_DOUBLEBUFFER,
                GLX.GLX_RED_SIZE,   4,
                GLX.GLX_GREEN_SIZE, 4,
                GLX.GLX_BLUE_SIZE,  4,
                GLX.GLX_DEPTH_SIZE, 16,
                0,
            ]
    # Attributes for newer style creations
    fbatt = [     GLX.GLX_X_RENDERABLE     , 1,
                  GLX.GLX_DRAWABLE_TYPE    , GLX.GLX_WINDOW_BIT,
                  GLX.GLX_RENDER_TYPE      , GLX.GLX_RGBA_BIT,
                  GLX.GLX_RED_SIZE         , 1,
                  GLX.GLX_GREEN_SIZE       , 1,
                  GLX.GLX_BLUE_SIZE        , 1,
                  GLX.GLX_DOUBLEBUFFER     , 1,
                  0,
            ]
    # Inherits the base and fills in the 3 platform dependent functions
    class OpenGLFrame( baseOpenGLFrame ):
        def tkCreateContext( self ):
            self.__window = XOpenDisplay( self.winfo_screen().encode('utf-8'))
            # Check glx version:
            major = c_int(0)
            minor = c_int(0)
            GLX.glXQueryVersion( self.__window, major, minor )
            print("GLX version: %d.%d"%(major.value,minor.value))
            if major.value == 1 and minor.value < 3: # e.g. 1.2 and down
                visual = GLX.glXChooseVisual( self.__window, 0, 
                                              (GL.GLint * len(att))(* att) )
                if not visual:
                    pass
                self.__context = GLX.glXCreateContext(self.__window,
                                                      visual,
                                                      None,
                                                      GL.GL_TRUE)
                GLX.glXMakeCurrent(self.__window, self._wid, self.__context)
                return # OUT HERE FOR 1.2 and less
            else:
                XDefaultScreen = _x11lib.XDefaultScreen
                XDefaultScreen.argtypes = [POINTER(Display)]
                XDefaultScreen.restype = c_int
                screen = XDefaultScreen( self.__window )
                print("Screen is ",screen)
                # Look at framebuffer configs 
                ncfg  = GL.GLint(0)
                cfgs = GLX.glXChooseFBConfig( self.__window,
                                             screen,
                                             (GL.GLint * len(fbatt))(* fbatt),
                                             ncfg )
                print( "Number of FBconfigs",ncfg.value )
                #
                # Try to match to the current window
                # ... might also be possible to set this for the frame
                # ... but for now we just take what Tk gave us
                ideal = int(self.winfo_visualid(), 16) # convert from hex
                best = -1
                for i in range(ncfg.value):
                    vis = GLX.glXGetVisualFromFBConfig(self.__window,  cfgs[i])
                    if ideal == vis.contents.visualid:
                        best = i
                        print("Got a matching visual: index %d %d xid %s"%(
                            best,vis.contents.visualid,hex(ideal) ))
                if best < 0:
                    print("oh dear - visual does not match" )
                    # Take the first in the list (should be another I guess)
                    best=0
                # Here we insist on RGBA - but didn't check earlier
                self.__context = GLX.glXCreateNewContext(self.__window,
                                                         cfgs[best],
                                                         GLX.GLX_RGBA_TYPE,
                                                         None, # share list
                                                         GL.GL_TRUE) # direct
                print("Is Direct?: ", GLX.glXIsDirect( self.__window, self.__context ))
                # Not creating another window ... some tutorials do
#                print("wid: ",self._wid)
#                self._wid = GLX.glXCreateWindow( self.__window, cfgs[best], self._wid, None)
#                print("wid: ",self._wid)
                GLX.glXMakeContextCurrent( self.__window, self._wid, self._wid,
                                           self.__context )
                print("Done making a first context")
                extensions = GLX.glXQueryExtensionsString(self.__window, screen)
                # Here we quit - getting a modern context needs further work below
                return
                if "GLX_ARB_create_context" in extensions:
                    # We can try to upgrade it ??
                    print("Trying to upgrade context")
                    s =  "glXCreateContextAttribsARB"
                    p = GLX.glXGetProcAddress( c_char_p( s ) )
                    
                    print(p)
                    if not p:
                        p = GLX.glXGetProcAddressARB( ( GL.GLubyte * len(s)).from_buffer_copy(s) )
                    print(p)
                    if p:
                        print(" p is true")
                    p.restype = GLX.GLXContext
                    p.argtypes = [POINTER(Display),
                                  GLX.GLXFBConfig,
                                  GLX.GLXContext,
                                  c_bool,
                                  POINTER(c_int)]
                    arb_attrs =   fbatt[:-1] + [ ]
                    #    GLX.GLX_CONTEXT_MAJOR_VERSION_ARB , 3  
                    #    GLX.GLX_CONTEXT_MINOR_VERSION_ARB , 1,
                    #    0 ]
                    #
                    #    GLX.GLX_CONTEXT_FLAGS_ARB
                    #    GLX.GLX_CONTEXT_PROFILE_MASK_ARB
                    #]
#                    import pdb
#                    pdb.set_trace()
                    self.__context = p( self.__window, cfgs[best], None, GL.GL_TRUE,
                                        (GL.GLint * len(arb_attrs))(* arb_attrs) )
                
        def tkMakeCurrent( self ):
            if self.winfo_ismapped():
                GLX.glXMakeCurrent(self.__window, self._wid, self.__context)
        def tkSwapBuffers( self ):
            if self.winfo_ismapped():
                GLX.glXSwapBuffers( self.__window, self._wid)
# Linux/X11 specific code ends  
###############################################################################

# Code copied from pyopengl/Tk/__init__.py for compatibility
# Modified so it does not import *
#
#
# A class that creates an opengl widget.
# Mike Hartshorn
# Department of Chemistry
# University of York, UK

def v3distsq(a,b):
    d = ( a[0] - b[0], a[1] - b[1], a[2] - b[2] )
    return d[0]*d[0] + d[1]*d[1] + d[2]*d[2]

class RawOpengl( OpenGLFrame ):
    """Widget without any sophisticated bindings\
    by Tom Schwaller"""
    def __init__(self, master=None, cnf={}, **kw):
        OpenGLFrame.__init__(*(self, master, cnf), **kw)
    # replaces our _display method
    def tkRedraw(self, *dummy):
        # This must be outside of a pushmatrix, since a resize event
        # will call redraw recursively. 
        self.update_idletasks()
        self.tkMakeCurrent()
        _mode = GL.glGetDoublev(GL.GL_MATRIX_MODE)

class Opengl(RawOpengl):
    """
    Tkinter bindings for an Opengl widget.
    Mike Hartshorn
    Department of Chemistry
    University of York, UK
    http://www.yorvic.york.ac.uk/~mjh/
    """
    def __init__(self, master=None, cnf={}, **kw):
        """\
        Create an opengl widget.
        Arrange for redraws when the window is exposed or when
        it changes size."""
        #Widget.__init__(self, master, 'togl', cnf, kw)
        RawOpengl.__init__(*(self, master, cnf), **kw)
        self.initialised = 0
        # Current coordinates of the mouse.
        self.xmouse = 0
        self.ymouse = 0
        # Where we are centering.
        self.xcenter = 0.0
        self.ycenter = 0.0
        self.zcenter = 0.0
        # The _back color
        self.r_back = 1.
        self.g_back = 0.
        self.b_back = 1.
        # Where the eye is
        self.distance = 10.0
        # Field of view in y direction
        self.fovy = 30.0
        # Position of clipping planes.
        self.near = 0.1
        self.far = 1000.0
        # Is the widget allowed to autospin?
        self.autospin_allowed = 0
        # Is the widget currently autospinning?
        self.autospin = 0
        # Basic bindings for the virtual trackball
        self.bind('<Shift-Button-1>', self.tkHandlePick)
        #self.bind('<Button-1><ButtonRelease-1>', self.tkHandlePick)
        self.bind('<Button-1>', self.tkRecordMouse)
        self.bind('<B1-Motion>', self.tkTranslate)
        self.bind('<Button-2>', self.StartRotate)
        self.bind('<B2-Motion>', self.tkRotate)
        self.bind('<ButtonRelease-2>', self.tkAutoSpin)
        self.bind('<Button-3>', self.tkRecordMouse)
        self.bind('<B3-Motion>', self.tkScale)

    def help(self):
        """Help for the widget."""
        d = dialog.Dialog(None, {
            'title': 'Viewer help',
            'text': 'Button-1: Translate\n'
                    'Button-2: Rotate\n'
                    'Button-3: Zoom\n'
                    'Reset: Resets transformation to identity\n',
            'bitmap': 'questhead',
            'default': 0,
            'strings': ('Done', 'Ok')})
        assert d
    def activate(self):
        """Cause this Opengl widget to be the current destination for drawing."""
        self.tkMakeCurrent()

    # This should almost certainly be part of some derived class.
    # But I have put it here for convenience.
    def basic_lighting(self):
        """\
        Set up some basic lighting (single infinite light source).
        Also switch on the depth buffer."""
   
        self.activate()
        light_position = (1, 1, 1, 0)
        GL.glLightfv(GL.GL_LIGHT0, GL.GL_POSITION, light_position)
        GL.glEnable(GL.GL_LIGHTING)
        GL.glEnable(GL.GL_LIGHT0)
        GL.glDepthFunc(GL.GL_LESS)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glLoadIdentity()
    def initgl(self):
        self.basic_lighting()
    def set_background(self, r, g, b):
        """Change the background colour of the widget."""
        self.r_back = r
        self.g_back = g
        self.b_back = b
        self.tkRedraw()

    def set_centerpoint(self, x, y, z):
        """Set the new center point for the model.
        This is where we are looking."""
        self.xcenter = x
        self.ycenter = y
        self.zcenter = z
        self.tkRedraw()

    def set_eyepoint(self, distance):
        """Set how far the eye is from the position we are looking."""
        self.distance = distance
        self.tkRedraw()

    def reset(self):
        """Reset rotation matrix for this widget."""
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glLoadIdentity()
        self.tkRedraw()

    def tkHandlePick(self, event):
        """Handle a pick on the scene."""
        if hasattr(self, 'pick'):
            # here we need to use glu.UnProject
            # Tk and X have their origin top left, 
            # while Opengl has its origin bottom left.
            # So we need to subtract y from the window height to get
            # the proper pick position for Opengl
            realy = self.winfo_height() - event.y
            p1 = GLU.gluUnProject(event.x, realy, 0.)
            p2 = GLU.gluUnProject(event.x, realy, 1.)
            if self.pick(self, p1, p2):
                """If the pick method returns true we redraw the scene."""
                self.tkRedraw()

    def tkRecordMouse(self, event):
        """Record the current mouse position."""
        self.xmouse = event.x
        self.ymouse = event.y
        print(event.x,event.y)

    def StartRotate(self, event):
        # Switch off any autospinning if it was happening
        self.autospin = 0
        self.tkRecordMouse(event)

    def tkScale(self, event):
        """Scale the scene.  Achieved by moving the eye position.
        Dragging up zooms in, while dragging down zooms out
        """
        scale = 1 - 0.01 * (event.y - self.ymouse)
        # do some sanity checks, scale no more than
        # 1:1000 on any given click+drag
        if scale < 0.001:
            scale = 0.001
        elif scale > 1000:
            scale = 1000
        self.distance = self.distance * scale
        self.tkRedraw()
        self.tkRecordMouse(event)

    def do_AutoSpin(self):
        self.activate()
        glRotateScene(0.5, self.xcenter, self.ycenter, self.zcenter, 
                self.yspin, self.xspin, 0, 0)
        self.tkRedraw()
        if self.autospin:
            self.after(10, self.do_AutoSpin)

    def tkAutoSpin(self, event):
        """Perform autospin of scene."""
        self.after(4)
        self.update_idletasks()
        # This could be done with one call to pointerxy but I'm not sure
        # it would any quicker as we would have to split up the resulting
        # string and then conv
        x = self.tk.getint(self.tk.call('winfo', 'pointerx', self._w))
        y = self.tk.getint(self.tk.call('winfo', 'pointery', self._w))
        if self.autospin_allowed:
            if x != event.x_root and y != event.y_root:
                self.autospin = 1
        self.yspin = x - event.x_root
        self.xspin = y - event.y_root
        self.after(10, self.do_AutoSpin)

    def tkRotate(self, event):
        """Perform rotation of scene."""
        self.activate()
        glRotateScene(0.5, self.xcenter, self.ycenter, self.zcenter, 
                event.x, event.y, self.xmouse, self.ymouse)
        self.tkRedraw()
        self.tkRecordMouse(event)

    def tkTranslate(self, event):
        """Perform translation of scene."""
        self.activate()
        # Scale mouse translations to object viewplane so object tracks with mouse
        win_height = max( 1,self.winfo_height() )
        obj_c = ( self.xcenter, self.ycenter, self.zcenter )
        win = GLU.gluProject( obj_c[0], obj_c[1], obj_c[2])
        obj = GLU.gluUnProject( win[0], win[1] + 0.5 * win_height, win[2])
        dist = math.sqrt( v3distsq( obj, obj_c ) )
        scale = abs( dist / ( 0.5 * win_height ) )
        glTranslateScene(scale, event.x, event.y, self.xmouse, self.ymouse)
        self.tkRedraw()
        self.tkRecordMouse(event)

    def tkRedraw(self, *dummy):
        """Cause the opengl widget to redraw itself."""
        self.freecalc(self)
        if not self.initialised: return
        self.activate()
        self.update_idletasks()
        self.activate()
        w = self.winfo_width()
        h = self.winfo_height()
        GL.glViewport(0, 0, w, h)
        # Clear the background and depth buffer.
        #GL.glClearColor(self.r_back, self.g_back, self.b_back, 0.)
        #GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GLU.gluPerspective(self.fovy, float(w)/float(h), self.near, self.far)
        if 0:
            # Now translate the scene origin away from the world origin
            glMatrixMode(GL_MODELVIEW)
            mat = glGetDoublev(GL_MODELVIEW_MATRIX)
            glLoadIdentity()
            glTranslatef(-self.xcenter, -self.ycenter, -(
                self.zcenter+self.distance))
            glMultMatrixd(mat)
        else:
            GLU.gluLookAt(self.xcenter, self.ycenter, self.zcenter+self.distance,
                self.xcenter, self.ycenter, self.zcenter,
                0., 1., 0.)
            GL.glMatrixMode(GL.GL_MODELVIEW)
    
        # Call objects redraw method.
        self.redraw(self)
    def freecalc( self, *args, **named ):
        """Prevent access errors if user doesn't set redraw fast enough"""
    def redraw( self, *args, **named ):
        """Prevent access errors if user doesn't set redraw fast enough"""

    def tkExpose(self, *dummy):
        """Redraw the widget.
        Make it active, update tk events, call redraw procedure and
        swap the buffers.  Note: swapbuffers is clever enough to
        only swap double buffered visuals."""
        self.activate()
        if not self.initialised:
            self.basic_lighting()
            self.initialised = 1
        self.tkRedraw()

    def tkPrint(self, file):
        """Turn the current scene into PostScript via the feedback buffer."""
        self.activate()
class D2Dprerender: # <<<<<<<<<<< Pre Render Static Draw (Creates Object Able to be rendered) [Faster than D2Draw - On Run Rendering]
    def __init__(self,screen_res):
        pass#DFPASS 
        
    def prerender_quad(self_,cords,color):
        ''' Pre render quad '''
        tr1 = self_._cords_to_ratio(cords[0],cords[1])
        tr2 = self_._cords_to_ratio(cords[2]-self_.nx,cords[3]-self_.ny)
        data = ['quad',tr1,tr2,color]
        return data 
        
        
        
        
        
    def prerender_texturequad(self_,cords,color,texture):
        ''' Pre render Texture quad ''' 
        tr1 = self_._cords_to_ratio(cords[0],cords[1])
        tr2 = self_._cords_to_ratio(cords[2]-self_.nx,cords[3]-self_.ny)
        data = ['tquad',tr1,tr2,color,texture]
        return data
        
        
        
        
        
        
        
        
    def create_font(filename, size,base,texid):
        face = Face(filename)
        face.set_char_size( size*64 )
        if not face.is_fixed_width:
            pass#raise 'Font is not monotype'
        width, height, ascender, descender = 0, 0, 0, 0
        for c in range(32,128):
            face.load_char( chr(c), FT_LOAD_RENDER | FT_LOAD_FORCE_AUTOHINT )
            bitmap    = face.glyph.bitmap
            width     = max( width, bitmap.width )
            ascender  = max( ascender, face.glyph.bitmap_top )
            descender = max( descender, bitmap.rows-face.glyph.bitmap_top )
        height = ascender+descender
        Z = numpy.zeros((height*6, width*16), dtype=numpy.ubyte)
        for j in range(6):
            for i in range(16):
                face.load_char(chr(32+j*16+i), FT_LOAD_RENDER | FT_LOAD_FORCE_AUTOHINT )
                bitmap = face.glyph.bitmap
                x = i*width  + face.glyph.bitmap_left
                y = j*height + ascender - face.glyph.bitmap_top
                Z[y:y+bitmap.rows,x:x+bitmap.width].flat = bitmap.buffer
        # Bound texture
        GL.glEnable(GL.GL_TEXTURE_2D)
        print('Before >',texid)
        GL.glPixelStorei(GL.GL_UNPACK_ALIGNMENT,1)
        GL.glGenTextures(1, texid)
        GL.glBindTexture( GL.GL_TEXTURE_2D, texid)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_NEAREST  )
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST )
        
        GL.glTexImage2D( GL.GL_TEXTURE_2D, 0, GL.GL_ALPHA, Z.shape[1], Z.shape[0], 0,
                         GL.GL_ALPHA, GL.GL_UNSIGNED_BYTE, Z )
        font = []
        print('Create >',texid)
        # Generate display lists
        dx, dy = width/float(Z.shape[1]), height/float(Z.shape[0])
        for i in range(8*16):
            c = chr(i)
            x = i%16
            y = i//16-2
            if (c == '\n'):
                #GL.glTranslatef( 0, -height, 0 )
                font.append(['NEWLINE'])
            elif (c == '\t'):
                #GL.glTranslatef( 4*width, 0, 0 )
                font.append(['TAB'])
            elif (i >= 32):
                cords1 = ( (x  )*dx, (y+1)*dy ); texcords1 = ( 0,     -height )
                cords2 = ( (x  )*dx, (y  )*dy ); texcords2 = ( 0,     0 )
                cords3 = ( (x+1)*dx, (y  )*dy ); texcords3 = ( width, 0 )
                cords4 = ( (x+1)*dx, (y+1)*dy ); texcords4 = ( width, -height )
                #GL.glTranslatef( width, 0, 0 )
                font.append([[cords1,texcords1],[cords2,texcords2],[cords3,texcords3],[cords4,texcords4],width,height])
            else:
                font.append([None])
        return font  
        
        
        
        
        
        
        
    def prerender_text(self_,cords,text,font_letters,spacing_addx,spacing_addy,color,font_texture):
        ''' Pre render Text '''
        config=(256,256,8)
        data_type = ['text']
        data_length = 0
        data_txn = []
        data_tr1 = []
        data_tr2 = []
        spacing = 0
        size_x = 16
        size_y = 16
        r=0;y=0
        spacing_y=0
        add_boldnext=0
        for i in text:
            yr=0
            x=0
            l=i 
            if i == '/' or r == 1:
                r=1 
                if i == 'n':
                    spacing_y+=spacing_addy
                    spacing=0
                    r=0
                if i == 'b':
                    add_boldnext = 1
                    r=0
                else:pass
            else:
                if add_boldnext == 1:
                    l='[b]'+l
                    add_boldnext=0
                for ls in font_letters:
                    try:
                        x = font_letters[yr].index(l)
                        y = yr
                    except:pass 
                    yr+=1
                x=-x
                y=-y-1
                spacing+=spacing_addx
                cords_=[cords[0]+spacing,cords[1]+spacing_y,cords[0]+size_x+spacing,cords[1]+size_y+spacing_y]
                textn=([x,y],config[2],(config[0],config[1]))
                tr1 = self_._cords_to_ratio(cords_[0],cords_[1])
                tr2 = self_._cords_to_ratio(cords_[2]-self_.nx,cords_[3]-self_.ny)
                txn = self_._tex_arrayn_translate(textn[0],textn[1],textn[2])
                    
                data_txn.append(txn)
                data_tr1.append(tr1)
                data_tr2.append(tr2)
                data_length+=1 
        data = [data_type,data_length,data_txn,data_tr1,data_tr2,color,font_texture]
        return data
class D2DRENDER: # Renders Pre Rendered object.  
    def render(prerenderedobj):
        if prerenderedobj[0] is 'text':
            D2DRENDER.render_text(prerenderedobj)
        if prerenderedobj[0] is 'quad':
            D2DRENDER.render_quad(prerender_quad)
            
            
            
            
            
    def render_letter(D2Draw,cords,color,letter,font,texid):  
        ct = int(ord(letter))
        self = D2Draw 
        width, height= (font[ct][4],font[ct][5])
        t1=font[ct][0][0];c1=font[ct][0][1]
        t2=font[ct][1][0];c2=font[ct][1][1]
        t3=font[ct][2][0];c3=font[ct][2][1]
        t4=font[ct][3][0];c4=font[ct][3][1]
        GL.glEnable(GL.GL_TEXTURE_2D)
        GL.glBindTexture(GL.GL_TEXTURE_2D, texid)
        GL.glBegin(GL.GL_QUADS)
        GL.glColor3f(color[0],color[1],color[2])
        tr1 = self._cords_to_ratio(cords[0],cords[1]-height)
        tr2 = self._cords_to_ratio(cords[2]-self.nx+width,cords[3]-self.ny)
        GL.glTexCoord2f(t1[0], t1[1]);GL.glVertex2f(tr1[0],tr2[1]);
        GL.glTexCoord2f(t2[0], t2[1]);GL.glVertex2f(tr1[0],tr1[1]);
        GL.glTexCoord2f(t3[0], t3[1]);GL.glVertex2f(tr2[0],tr1[1]);
        GL.glTexCoord2f(t4[0], t4[1]);GL.glVertex2f(tr2[0], tr2[1]); 
        GL.glEnd()
        GL.glDisable(GL.GL_TEXTURE_2D)
        return width, height 
        
        
        
        
        
    def render_text(pretext):
        ''' pretext - prerendered text '''  # Working :)
        GL.glEnable(GL.GL_TEXTURE_2D)
        GL.glBindTexture(GL.GL_TEXTURE_2D, pretext[6])
        GL.glBegin(GL.GL_QUADS)
        GL.glColor3f(pretext[5][0],pretext[5][1],pretext[5][2])
        for i in range(0,pretext[1]):
            txn = pretext[2][i] 
            tr1 = pretext[3][i]
            tr2 = pretext[4][i]
            GL.glTexCoord2f(txn[0][0], txn[1][1])
            GL.glVertex2f(tr2[0],tr1[1])
            GL.glTexCoord2f(txn[0][0], txn[0][1])
            GL.glVertex2f(tr2[0], tr2[1])
            GL.glTexCoord2f(txn[1][0], txn[0][1])
            GL.glVertex2f(tr1[0],tr2[1])
            GL.glTexCoord2f(txn[1][0], txn[1][1])
            GL.glVertex2f(tr1[0], tr1[1])
        GL.glEnd()
        
        
        
        
    def render_quad(prequad):
        GL.glBegin(GL.GL_QUADS)
        GL.glColor3f(prequad[3][0],prequad[3][1],prequad[3][2])
        tr1 = prequad[1]
        tr2 = prequad[2]
        GL.glVertex2f(tr1[0], tr1[1])
        GL.glVertex2f(tr1[0],tr2[1])
        GL.glVertex2f(tr2[0], tr2[1])
        GL.glVertex2f(tr2[0],tr1[1])
        GL.glEnd()
        
        
        
        
    def render_texture_quad(pretextquad=None,texsize=0,usecords=True):
        GL.glEnable(GL.GL_TEXTURE_2D)
        GL.glBindTexture(GL.GL_TEXTURE_2D, pretextquad[4])
        GL.glBegin(GL.GL_QUADS)
        tr1 = pretextquad[1]
        tr2 = pretextquad[2]
        
        GL.glColor3f(pretextquad[3][0],pretextquad[3][1],pretextquad[3][2])
        if usecords is True:
            GL.glTexCoord2f(1, 1)
            GL.glVertex2f(tr2[0], tr2[1])
            GL.glTexCoord2f(0-texsize, 1)
            GL.glVertex2f(tr1[0],tr2[1])
            GL.glTexCoord2f(0-texsize, 0-texsize)
            GL.glVertex2f(tr1[0], tr1[1])
            GL.glTexCoord2f(1, 0-texsize)
            GL.glVertex2f(tr2[0],tr1[1])
        else:
            GL.glTexCoord2f(1, 1)
            GL.glVertex2f(10, 10)
            GL.glTexCoord2f(0-texsize, 1)
            GL.glVertex2f(-10,10)
            GL.glTexCoord2f(0-texsize, 0-texsize)
            GL.glVertex2f(-10, -10)
            GL.glTexCoord2f(1, 0-texsize)
            GL.glVertex2f(10,-10)
        
        GL.glEnd()
        
        
        
        
        
        
        
        
        
        
        
        
#dp_load_texture
from OpenGL import GL
from PIL import Image
import numpy
import mmap, os 
import ctypes 
import random as rnd 
import time
from freetype import * 
vipshome = 'D:/vips-dev-8.9/bin'
os.environ['PATH'] = vipshome + ';' + os.environ['PATH']
import pyvips 
global TEXTURE_DISPLAY_METHOD
TEXTURE_DISPLAY_METHOD = GL.GL_NEAREST
def load_texture_dp(dp_data,n,alpha=False):
    ''' Alpha - True Or False, False- RGB 3bytes , True- RGBA 4Bytes'''
    global TEXTURE_DISPLAY_METHOD
    texture_data  = dp_data[1] 
    realdata = []
    for i in texture_data:
        realdata.append(int(i))
    
    textr = GL.glGenTextures(n)
    GL.glPixelStorei(GL.GL_UNPACK_ALIGNMENT,1)
    
    GL.glBindTexture(GL.GL_TEXTURE_2D, textr)
    GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, TEXTURE_DISPLAY_METHOD )
    GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, TEXTURE_DISPLAY_METHOD )
    
    if alpha is True:GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGBA, int(dp_data[0][0]), int(dp_data[0][1]), 0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, realdata)
    else:GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGB, int(dp_data[0][0]), int(dp_data[0][1]), 0, GL.GL_RGB, GL.GL_UNSIGNED_BYTE, realdata)
    return textr 
  
def load_texture_repeat(texture_=None,n=None):
    global TEXTURE_DISPLAY_METHOD
    texture = Image.open(texture_,'r') 
    texture_data  = numpy.array(list(texture.getdata()), numpy.uint8)
    textr = GL.glGenTextures(n)
    GL.glPixelStorei(GL.GL_UNPACK_ALIGNMENT,1)
    
    
    GL.glBindTexture(GL.GL_TEXTURE_2D, textr)
    GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGB, texture.size[0], texture.size[1], 0, GL.GL_RGB, GL.GL_UNSIGNED_BYTE, texture_data)
    
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, TEXTURE_DISPLAY_METHOD )
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, TEXTURE_DISPLAY_METHOD )
    
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT )
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT )
    
    return textr 
    
    
    
    
def usingVIPSandShrink(f): 
    image = pyvips.Image.new_from_file(f, access="sequential", shrink=2) 
    mem_img = image.write_to_memory() 
    imgnp=np.frombuffer(mem_img, dtype=np.uint8).reshape(image.height, image.width, 3)  
    return imgnp 
    
def pure_pil_alpha_to_color_v2(image, color=(255, 255, 255)):
    image.load()  # needed for split()
    background = Image.new('RGB', image.size, color)
    background.paste(image, mask=image.split()[3])  # 3 is the alpha channel
    return background
def rgba2rgb(x):
    x = x[::4]
    return x
    
def create_font(filename, size,base,texid):
    
    face = Face(filename)
    face.set_char_size( size*64 )
    if not face.is_fixed_width:
        pass#raise 'Font is not monotype'
    width, height, ascender, descender = 0, 0, 0, 0
    for c in range(32,128):
        face.load_char( chr(c), FT_LOAD_RENDER | FT_LOAD_FORCE_AUTOHINT )
        bitmap    = face.glyph.bitmap
        width     = max( width, bitmap.width )
        ascender  = max( ascender, face.glyph.bitmap_top )
        descender = max( descender, bitmap.rows-face.glyph.bitmap_top )
    height = ascender+descender
    Z = numpy.zeros((height*6, width*16), dtype=numpy.ubyte)
    for j in range(6):
        for i in range(16):
            face.load_char(chr(32+j*16+i), FT_LOAD_RENDER | FT_LOAD_FORCE_AUTOHINT )
            bitmap = face.glyph.bitmap
            x = i*width  + face.glyph.bitmap_left
            y = j*height + ascender - face.glyph.bitmap_top
            Z[y:y+bitmap.rows,x:x+bitmap.width].flat = bitmap.buffer
    # Bound texture
    GL.glGenTextures(1, texid)
    GL.glPixelStorei(GL.GL_UNPACK_ALIGNMENT,1)
    GL.glBindTexture( GL.GL_TEXTURE_2D, texid)
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR  )
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR  )
    GL.glTexImage2D( GL.GL_TEXTURE_2D, 0, GL.GL_ALPHA, Z.shape[1], Z.shape[0], 0,
                     GL.GL_ALPHA, GL.GL_UNSIGNED_BYTE, Z )
                     
    font = []
    # Generate display lists
    dx, dy = width/float(Z.shape[1]), height/float(Z.shape[0])
    for i in range(8*16):
        c = chr(i)
        x = i%16
        y = i//16-2
        if (c == '\n'):
            #GL.glTranslatef( 0, -height, 0 )
            font.append(['NEWLINE'])
        elif (c == '\t'):
            #GL.glTranslatef( 4*width, 0, 0 )
            font.append(['TAB'])
        elif (i >= 32):
            cords1 = ( (x  )*dx, (y+1)*dy ); texcords1 = ( 0,     -height )
            cords2 = ( (x  )*dx, (y  )*dy ); texcords2 = ( 0,     0 )
            cords3 = ( (x+1)*dx, (y  )*dy ); texcords3 = ( width, 0 )
            cords4 = ( (x+1)*dx, (y+1)*dy ); texcords4 = ( width, -height )
            #GL.glTranslatef( width, 0, 0 )
            font.append([[cords1,texcords1],[cords2,texcords2],[cords3,texcords3],[cords4,texcords4],width,height])
        else:
            font.append([None])
        
    return font  
def load_texture_sub(Texture_unit=0,New_Texture=None,Offests=(0,0),size=(1920,1080),buffmanager=None ):
    image = pyvips.Image.new_from_file(New_Texture, access="sequential") 
    scaley = (size[0]/image.height)
    scalex = (size[1]/image.width)
    height = image.height
    width = image.width
   
    image = image.thumbnail_image(1920,height=1080)
    mem_img = image.write_to_memory() 
    Offests = [(1920-image.width)/2,1080-image.height] 
 
    
    
    if image.bands == 3:
        imgnp=numpy.frombuffer(mem_img, dtype=numpy.uint8).reshape(image.height, image.width, 3)  
    else:
        imgnp=numpy.frombuffer(mem_img, dtype=numpy.uint8)
        
  
    try:
        texture_data  = imgnp
        if image.bands == 3:
            buffmanager.add_textureupdate(Texture_unit,imgnp,image.width,image.height,texture_data,False,Offests) 
        if image.bands == 4:
            buffmanager.add_textureupdate(Texture_unit,imgnp,image.width,image.height,texture_data,True,Offests) 
        
    except Exception  as e:print(e,'wtf')
    
    return imgnp     
    
    
def load_texture(texture_=None,nr=None,repeat=False,RAW_DATA=[1920,1080],Alpha=False):
    try:
        image = pyvips.Image.new_from_file(texture_, access="sequential") 
        mem_img = image.write_to_memory() 
        if image.bands == 3:
            imgnp=numpy.frombuffer(mem_img, dtype=numpy.uint8).reshape(image.height, image.width, 3)  
        else:
            imgnp=numpy.frombuffer(mem_img, dtype=numpy.uint8)
    except:
        imgnp=texture_ 
        class image(object):
            def __init__(self):
                self.bands = 0 
                self.width = 0
                self.height = 0
        image = image()
        if Alpha is True:
            image.bands = 4
        else:
            image.bands = 3
        image.width = RAW_DATA[0] 
        image.height = RAW_DATA[1]
    try:
        texture_data  = imgnp
        textr = GL.glGenTextures(1, nr)
        GL.glPixelStorei(GL.GL_UNPACK_ALIGNMENT,1)
   
        GL.glBindTexture(GL.GL_TEXTURE_2D, nr)
     
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_NEAREST  )
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST )
        
        if image.bands == 3:
            GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGB, image.width, image.height, 0, GL.GL_RGB, GL.GL_UNSIGNED_BYTE, texture_data)
        if image.bands == 4:
            GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGBA, image.width, image.height, 0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, texture_data)
        
    except Exception  as e:print(e,'wtf')
    return nr     
    
#__init__ file.
import OpenGL.GL.shaders
from OpenGL.GL import *
from OpenGL import GL
import ctypes, os
import numpy
from array import array
class SHADER:
    def __init__(self):
        pass
# Vbo v0.1 Vertex Buffer <Memory Buffer> <Vertex - Points>
#
#
#
def getsize(x): #Getsize of 1 type
    return ctypes.sizeof(x)
def cfloat(x=None): #x is none for no arg
    if x != None:
        cf = ctypes.c_float(x)
    else:cf=ctypes.c_float()
    return cf
def cfloat_array(list):
    return (ctypes.c_float * len(list))(*list)
class VBO_OBJ:
    def __init__():
        pass
class VBO: # Not Recommended just opengl :l
    def __init__(self,shaderprogram=None):
        pass
class RENDER_VBO:
    def __init__(self,OBJECT):
        pass
class PRERENDER_VBO:
    def __init__(self):
        bufferid = int(id)
        buffer1 = GL.glGenBuffers(1,bufferid)

def _tex_arrayn_translate(n=[0,0],s=0,txs=[0,0]):
    ''' n = x,y  s = size  txs - texturesize  '''
    x1 = (n[0]*s)-s
    y1 = (n[1]*s)-s
    x2 = (n[0]*s)
    y2 = (n[1]*s)
    _c1 =_texture_cords_to_ratio(x1,y1,txs)
    _c2 =_texture_cords_to_ratio(x2,y2,txs)

    return _c1,_c2
def _cords_to_ratio(x,y,screenx,screeny):
    xr = x*(2/screenx)
    yr = y*(2/screeny)
    if xr > 1:
        xr = xr-1
    else:
        xr = xr-1
    if yr > 1:
        yr = 1-yr
    else:
        yr = 1-yr
    return xr,yr
def _texture_cords_to_ratio(x,y,size):
    xr = x*(2/size[0])
    yr = y*(2/size[1])
    if xr > 1:
        xr = xr-1
    else:
        xr = -(1-xr)
    if yr > 1:
        yr = (1-yr)
    else:
        yr = -(yr-1)
    return xr,yr


class DragoObject:
    def get_shader(self):
        return self.basicshader
    def __docs__(self):
        self.__doc__ = """
        Uniform/Layout/Matrix manipulation

        1. Create object
        2. Draw Object
        3. Move/Transform/Morph object
        """


    def serialize_to_obj(self,unload=False,eventmanager=None):
        ''' Serialize scene (current objects and eventss) ''' 
        self.serialization = True 
        self.serialization_current_object  = 'Do something to create this object' 
        return self.serialization_current_object 
        
    def _load_scene(self,serialized_obj=None,overlay=False):
        ''' If overlay is false unload previous scene ''' 
        pass 
        
    def _is_serialized(self):
        return self.serialization 
    def create_quad(self,BOX_START=[0,0],BOX_SIZE=[0,0],COLOR=[1,0,0,1],TEXTUREID=0):
        if TEXTUREID not in self.textures:
            glBindTextureUnit(TEXTUREID, TEXTUREID)
        cords = [
        [BOX_START[0],
        BOX_START[1]],
        [BOX_START[0]+BOX_SIZE[0],
        BOX_START[1]],
        [BOX_START[0]+BOX_SIZE[0],
        BOX_START[1]+BOX_SIZE[1]],
        [BOX_START[0],
        BOX_START[1]+BOX_SIZE[1]]
        ,]
        TXC = [[0.0,0.0],[1.0,0.0],[1.0,1.0],[0.0,1.0]]
        c=0
        for i in cords:
            (xr,yr) = _cords_to_ratio(i[0],i[1],self.sx,self.sy)
            self.vertices.append(xr) # 1
            self.vertices.append(yr) # 2 
            self.vertices.append(0) # 3 
            self.vertices.extend(COLOR) # 7
            self.vertices.append(TEXTUREID) # 8
            if c == 4:
                c=0
            self.vertices.extend([TXC[c][0],TXC[c][1]]) # 10 
            c+=1
        self.object_count += 1
        self.object_indexes.append(self.object_count-1)
        self.vns = len(self.vertices)
        self.textured = True
    
        self.textures.append(TEXTUREID)
        return self.object_count-1
    def get_objectindexes(self):
        return self.object_indexes
    def move(self,x,y,object):
        cords = _cords_to_ratio(x,y,self.sx,self.sy)
        #glBindBuffer(GL_ARRAY_BUFFER, self.vbo, self.vertices)
    def use_texture(self,txtid):
        self.textured = True
        self.textures.append(txtid)
    def create_letter(self,cords,font,letter,color,texid):
        if texid not in self.textures:
            glBindTextureUnit(texid, texid)
        ct = int(ord(letter))
        width, height= (font[ct][4],font[ct][5])
        t1=font[ct][0][0];c1=font[ct][0][1]
        t2=font[ct][1][0];c2=font[ct][1][1]
        t3=font[ct][2][0];c3=font[ct][2][1]
        t4=font[ct][3][0];c4=font[ct][3][1]

        tr1 = _cords_to_ratio(cords[0],cords[1]-height,self.sx,self.sy)
        tr2 = _cords_to_ratio(cords[2]+width,cords[3],self.sx,self.sy)
        z = 0.1
        self.vertices.append(tr1[0])
        self.vertices.append(tr2[1])
        self.vertices.append(z)
        self.vertices.extend(color)
        self.vertices.append(texid)
        self.vertices.extend([t1[0], t1[1]])

        self.vertices.append(tr1[0])
        self.vertices.append(tr1[1])
        self.vertices.append(z)
        self.vertices.extend(color)
        self.vertices.append(texid)
        self.vertices.extend([t2[0], t2[1]])
        self.vertices.append(tr2[0])
        self.vertices.append(tr1[1])
        self.vertices.append(z)
        self.vertices.extend(color)
        self.vertices.append(texid)
        self.vertices.extend([t3[0], t3[1]])
        self.vertices.append(tr2[0])
        self.vertices.append(tr2[1])
        self.vertices.append(z)
        self.vertices.extend(color)
        self.vertices.append(texid)
        self.vertices.extend([t4[0], t4[1]])

        self.object_count+=1
        self.object_indexes.append(self.object_count-1)
        self.vns = len(self.vertices)
        self.textured = True
        if texid not in self.textures:
            self.textures.append(texid)
        return self.object_count-1
    def draw_text(self):
        pass
    def move_up(self,object):
        ''' Move Object To front - Finally working ;-;'''
        real_value = self.object_indexes[object]
        real_index = self.object_indexes.index(real_value)
        for i in range(real_value,len(self.object_indexes)):
            self.object_indexes[self.object_indexes.index(i)] -=1 
        self.object_indexes[real_index] = len(self.object_indexes)-1
        x=0
        idx = nd = (0+((real_value*4)*10))
        sav_vert = self.vertices[idx:idx+40]
        for i in range(0,40):
            self.vertices.pop(idx)
        self.vertices.extend(sav_vert) 
        x+=1 
        return object
    def move_down(self,object):
        ''' Move Object To Back - Finally working ;-;'''
        real_value = self.object_indexes[object]
        real_index = self.object_indexes.index(real_value)
        for i in range(0,real_index):
            self.object_indexes[self.object_indexes.index(i)] -=1 
        self.object_indexes[real_index] = 0
        x=0
        idx = nd = (0+((real_value*4)*10))
        sav_vert = self.vertices[idx:idx+40]
        for i in range(0,40):
            self.vertices.pop(idx)
        self.vertices.insert(0,sav_vert) 
        x+=1 
        return object
            
        
        
    def get_vertices(self):
        return self.vertices
    def add_textureupdate(self,Texture_unit,Imagenumpy,width,height,texture_data,alpha,offset):
        if alpha:
            self.update_list.append(['tua',Texture_unit,Imagenumpy,width,height,texture_data,offset]) 
        else:
            self.update_list.append(['tu',Texture_unit,Imagenumpy,width,height,texture_data,offset]) 
    def update(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo )
        updates = 0
        for il in self.update_list:
            if il[0] == 'tu':
                GL.glBindTexture(GL.GL_TEXTURE_2D, il[1])
                GL.glTexSubImage2D(GL.GL_TEXTURE_2D, 0, il[6][0], il[6][1], il[3], il[4], GL.GL_RGB, GL.GL_UNSIGNED_BYTE, il[5]) 
            elif il[0] == 'tua':
                GL.glBindTexture(GL.GL_TEXTURE_2D, il[1])
                GL.glTexSubImage2D(GL.GL_TEXTURE_2D, 0, il[6][0], il[6][1], il[3], il[4], GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, il[5]) 
            elif il[0] == 'del': # Temporary way to delete (change latter)
                self.edit_pos(il[1],[0,0],[0,0])
            elif il[0] == 'dmd': #Set draw mode 
                self.DRAWMODELOC = glGetUniformLocation(self.basicshader, 'DRAW_MODE')
                glUniform1iv(self.DRAWMODELOC, 1 , il[1])
                
            else:
                glBufferSubData(GL_ARRAY_BUFFER,il[0]*4,4,ctypes.c_float(il[1]))
            updates+=1
        glBindBuffer(GL_ARRAY_BUFFER, 0 )
        self.update_list = []
        self.total_updates = updates
    def clear(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo )
        glBufferSubData(GL_ARRAY_BUFFER,0,12,ctypes.c_void_p(0))
        glBindBuffer(GL_ARRAY_BUFFER, 0)
    def get_pos(self,object):
        """Gets positions (x,y,x2,y2) inside memory """
        nd = (0+((self.object_indexes[object]*4)*10))
        x1 = self.vertices[nd]
        x2 = self.vertices[nd+20]
        y1 = self.vertices[nd+1]
        y2 = self.vertices[nd+21]
        return [x1,x2,y1,y2]
    def get_color(self,object):
        """ Gets colors (r, g, b, a) inside memory """ 
        nd = (0+((self.object_indexes[object]*4)*10))
        r_val = self.vertices[nd+3]
        g_val = self.vertices[nd+4]
        b_val = self.vertices[nd+5]
        a_val = self.vertices[nd+6]
        return r_val, g_val, b_val, a_val 
    def get_texid(self,object):
        """ Gets texture id inside memory """ 
        nd = (0+((self.object_indexes[object]*4)*10))
        textid = self.vertices[nd+7]
        return textid 
        
    def edit_letter(self,object,font,letter):
        ct = int(ord(letter))
        t1=font[ct][0][0];c1=font[ct][0][1]
        t2=font[ct][1][0];c2=font[ct][1][1]
        t3=font[ct][2][0];c3=font[ct][2][1]
        t4=font[ct][3][0];c4=font[ct][3][1]

        tlist = [t1[0], t1[1], t2[0], t2[1], t3[0], t3[1], t4[0], t4[1]]

        self.edit_tpos(object, tlist)
    def edit_tpos(self,object=None,newtpos=[]):
        nd = 0+((self.object_indexes[object]*4)*10)
        
        ou = []
        ou.append([nd+8, newtpos[0]])
        ou.append([nd+9, newtpos[1]])

        ou.append([nd+18, newtpos[2]])
        ou.append([nd+19, newtpos[3]])
        ou.append([nd+28, newtpos[4]])
        ou.append([nd+29, newtpos[5]])
        ou.append([nd+38, newtpos[6]])
        ou.append([nd+39, newtpos[7]])


        self.update_list.extend(ou)
    def edit_color(self,object=None,newcolor=[]):
        nd = (0+((self.object_indexes[object]*4)*10))
        ou = []
        ou.append([nd+3,newcolor[0]])
        ou.append([nd+4,newcolor[1]])
        ou.append([nd+5,newcolor[2]])
        ou.append([nd+6,newcolor[3]])
        ou.append([nd+13,newcolor[0]])
        ou.append([nd+14,newcolor[1]])
        ou.append([nd+15,newcolor[2]])
        ou.append([nd+16,newcolor[3]])
        ou.append([nd+23,newcolor[0]])
        ou.append([nd+24,newcolor[1]])
        ou.append([nd+25,newcolor[2]])
        ou.append([nd+26,newcolor[3]])
        ou.append([nd+33,newcolor[0]])
        ou.append([nd+34,newcolor[1]])
        ou.append([nd+35,newcolor[2]])
        ou.append([nd+36,newcolor[3]])

        self.update_list.extend(ou)
    def delete_obj(self,obj):
        nd = (0+((self.object_indexes[obj]*4)*10))
        self.update_list.append(['del',obj])
        
    def edit_pos(self,object=None,newpos=[],size=None,letter=False):
   
        nd = (0+((self.object_indexes[object]*4)*10))
       
        curpos = self.get_pos(self.object_indexes[object])
        if size == None:
            sizey = self.vertices[nd+1] +self.vertices[nd+11]
            sizex = self.vertices[nd+10]-self.vertices[nd]
        else:
            sizex, sizey = _cords_to_ratio(size[0],size[1],self.sx,self.sy)
            sizex = 1+sizex
            sizey = 1-sizey
        newpos = _cords_to_ratio(newpos[0],newpos[1],self.sx,self.sy)


        ou = []
        if letter is True:
            ou.append([nd+20,   newpos[0]])                # x1
            ou.append([nd+21, newpos[1]])                # y1
            ou.append([nd+10 ,newpos[0]-sizex])         # x2
            ou.append([nd+11 ,newpos[1]])               # y2
            ou.append([nd+0 ,newpos[0]-sizex])         # x3
            ou.append([nd+1 ,newpos[1]-sizey] )        # y3
            ou.append([nd+30 ,newpos[0]])               # x4
            ou.append([nd+31 ,newpos[1]-sizey ])        # y4
        else:
            ou.append([nd+0,   newpos[0]])                # x1
            ou.append([nd+1, newpos[1]])                # y1
            ou.append([nd+10 ,newpos[0]+sizex])         # x2
            ou.append([nd+11 ,newpos[1]])               # y2
            ou.append([nd+20 ,newpos[0]+sizex])         # x3
            ou.append([nd+21 ,newpos[1]-sizey] )        # y3
            ou.append([nd+30 ,newpos[0]])               # x4
            ou.append([nd+31 ,newpos[1]-sizey ])        # y4

        self.update_list.extend(ou)
    def edit_texture(self,object=None,txtid=0):
        
        if txtid not in self.textures:
            glBindBuffer(GL_ARRAY_BUFFER, self.vbo )
            glBindTextureUnit(txtid, txtid)
        nd = (0+((self.object_indexes[object]*4)*10))
        ou = []
        
        
        
        ou.append([nd+7,float(txtid)])
        self.vertices[nd+7] = txtid 
        ou.append([nd+17,float(txtid)])
        self.vertices[nd+17] = txtid 
        ou.append([nd+27,float(txtid)])
        self.vertices[nd+27] = txtid 
        ou.append([nd+37,float(txtid)])
        self.vertices[nd+37] = txtid 
        self.update_list.extend(ou)
        if txtid not in self.textures:
            self.textures.append(txtid)
            glBindBuffer(GL_ARRAY_BUFFER, 0)
    def get_buffer(self):
        return self.vertices
    def bind_buffer(self):
        glUseProgram(self.basicshader)
    def switch(self,vbo):

        try:
            self.vertices = self.vert_lists[vbo]
            self.object_count = self.object_counts[vbo]
        except:
            self.vert_lists.append(self.vertices)
            self.object_counts.append(self.object_count)
            self.vertices = []
            self.update_list = []
        self.object_count=0
        self.vbo = self.vbos[vbo]
    def add_buffer(self):
        self.vbo = glGenBuffers(1)
        self.vbos.append(self.vbo)
        self.vb_count+=1

    def compile(self):
        for vbo in self.vbos:
            glBindBuffer(GL_ARRAY_BUFFER, vbo )

            glBufferData(GL_ARRAY_BUFFER, len(self.vertices)*4, (ctypes.c_float*len(self.vertices))(*self.vertices), GL_DYNAMIC_DRAW)

            glEnableVertexAttribArray(0)
            glVertexAttribPointer(0, 3 ,GL_FLOAT, GL_FALSE, sizeof(cfloat())*10, ctypes.c_void_p(0)) # 3 pos
            glEnableVertexAttribArray(1)
            glVertexAttribPointer(1, 4 ,GL_FLOAT, GL_FALSE, sizeof(cfloat())*10,  ctypes.c_void_p(12)) # 4 color
            glEnableVertexAttribArray(2)
            glVertexAttribPointer(2, 1 ,GL_FLOAT, GL_FALSE, sizeof(cfloat())*10,  ctypes.c_void_p(28)) # 4
            glEnableVertexAttribArray(3)
            glVertexAttribPointer(3, 3 ,GL_FLOAT, GL_FALSE, sizeof(cfloat())*10,  ctypes.c_void_p(32)) # 2
            glBindBuffer(GL_ARRAY_BUFFER, 0 )
    def queue_check():
        """check and execute queue """
    def queue():
        """
        (Input list ?, +delay)
        
        Feature - [Looping queue ?] - as bool - loop = true 
        
        Mandatory - 
            [Queue pointer ?] 
            [Queue list] - self.update_list_queued    < List of queued objects 
                Structure - 
                    [[EVENTS1,EVENTS2],delay,[CONFIG]] 
                    CONFIG -  
                        loop,loopreverse,delete < bools 
                        loop_delay, delete_delay < int 
                        
                    delay - 
                        single if list check if length is the same as events if it is applicate to each end. 
                    
                    events (Function list to be executed) 
                        
        """
    def __init__(self,screenx,screeny):
        glEnableClientState(GL_VERTEX_ARRAY)
        self.sx =  screenx
        self.sy =   screeny
        self.serialization = False 
        self.serialization_current_object = None 
        self.textured = False
        self.texture_data = []
        self.textures = []
        self.total_updates = 0
        self.vertices = []
        self.vbo = 0
        self.vbos = []
        self.vb_count = 0
        self.object_count = 0
        self.vns = 0
        self.oj = 0
        self.vert_lists = []
        self.object_counts = []
        self.update_list = []
        self.object_moved = []

        self.object_indexes = []

        vxshader = '''
#version 330 core 
layout(location = 0) in vec4 position;
layout(location = 1) in vec4 color;
layout(location = 2) in float TXTID;
layout(location = 3) in vec2 TXTC; 
out vec4 v_Color;
out int in_TXTID; 
out vec2 in_TXTC; 
uniform int DRAW_MODE; 
void main() {
    in_TXTC = TXTC;
    in_TXTID = int(TXTID);
    v_Color = color;
    gl_Position = gl_ModelViewProjectionMatrix*position  ;
    
}
        
        '''
        fgshader = '''
#version 330 core
layout(location = 0) out vec4 out_color;
in vec4 v_Color;
in flat int in_TXTID; 
in vec2 in_TXTC;   
uniform int DRAW_MODE; 
uniform sampler2D TXTARRAY[160];       
   
void main() {
    if(DRAW_MODE == 0){
        if(in_TXTID != 0) {
            for(int i = 0; i <= 160; i++){
                if(in_TXTID == i){out_color = texture(TXTARRAY[int(in_TXTID)], in_TXTC);break;}}
                out_color.r+= v_Color[0];
                out_color.g+= v_Color[1];
                out_color.b+= v_Color[2];
                out_color.a+= v_Color[3];
            }
        else {
            out_color = v_Color;
            }
    }
    
    else if(DRAW_MODE == 1){
        if(in_TXTID != 0) {
            out_color = vec4(in_TXTC, 0 ,  1);
            }
        else {
            out_color = v_Color;
            }
        }
        
        
        
}'''
        VERTEX_SHADER = shaders.compileShader(vxshader, GL_VERTEX_SHADER)
        #texture(TXTARRAY[index], in_TXTC)
        FRAGMENT_SHADER = shaders.compileShader(fgshader, GL_FRAGMENT_SHADER)
        self.basicshader = shaders.compileProgram(VERTEX_SHADER,FRAGMENT_SHADER)


        # 160 texture units
        self.texture_slots = []
        for i in range(0,160):
            self.texture_slots.append(i)
        glUseProgram(self.basicshader)
        self.DRAWMODELOC = glGetUniformLocation(self.basicshader, 'DRAW_MODE')
        self.TXTARRAY = glGetUniformLocation(self.basicshader, 'TXTARRAY')
        glUniform1iv(self.TXTARRAY, len(self.texture_slots) ,self.texture_slots)
        glUniform1iv(self.DRAWMODELOC, 1 , 0)
        glUseProgram(0)
    def set_mode(self,mode):
        self.update_list.extend([['dmd',mode]])

    def draw(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo )
        if self.textured is False:
            glDrawArrays(GL_QUADS, 0, int(self.vns))
        else:
            glDrawArrays(GL_QUADS, 0, int(self.vns))
        glBindBuffer(GL_ARRAY_BUFFER, 0 )
class D2DWidgets:
    def __init__(self,D2DOBJ,EVMANAGER):
        """Widgets :D"""
        self.D2D = D2DOBJ 
        self.EVENT_MANAGER = EVMANAGER
        self.WIDGETS = [] 
        
        
 
    # _std standard events for widgets :3 
    def _std_x(self,*ALL_VARIABLESIN):
        ''' Example 
        ARGS = [but, BUTTON_XY, BUTTON_SIZE, BUTTON_COLOR, BUTTON_TEXTUREID, ON_HOVER,ON_HOVER_RETRACT, HOVER_DELAY, ON_CLICK, ON_CLICK_RETRACT, CLICK_DELAY, COMMAND]
        
        '''
    
    def _std_darken(self,widget):
        widget = widget[0]
        self.D2D.edit_color(widget[0],
        [max(0,widget[3][0]-0.1), max(0,widget[3][1]-0.1),
        max(0,widget[3][2]-0.1), max(0,widget[3][3])])
        
    def _std_lighten(self,widget):
        widget = widget[0]
        self.D2D.edit_color(widget[0],
        [max(1,widget[3][0]+0.1), max(1,widget[3][1]+0.1),
        max(1,widget[3][2]+0.1), max(1,widget[3][3])])
        
        
    def _std_out(self,widget):
        pass
        
    def _std_hoverback_color(self,widget):
        widget = widget[0]
        self.D2D.edit_color(widget[0], [ widget[3][0], widget[3][1], widget[3][2], widget[3][3]]) 
    def _std_clickback_color(self,widget):
        widget = widget[0]
        self.D2D.edit_color(widget[0], [ widget[3][0], widget[3][1], widget[3][2], widget[3][3]])
        widget[-1](widget) 
    
    
    
    def _hover_dropbox(self,widget):
        main_widget = widget[0][0]
        xy = main_widget[1] 
        size = main_widget[2] 
        sub_widgets = [] 
        for i in widget[0][1:]:
            sub_widgets.append(i[0]) 
            
        r = 0 
        for i in sub_widgets:
            self.D2D.edit_pos(i,[xy[0],xy[1]+size[1]+r],size)
            r+=+size[1]
 
    def _inv_hover_dropbox(self,widget):
        main_widget = widget[0][0]
        xy = main_widget[1] 
        size = main_widget[2] 
        sub_widgets = [] 
        for i in widget[0][1:]:
            sub_widgets.append(i[0]) 
            
        for i in sub_widgets:
            self.D2D.edit_pos(i,[0,0],[0,0]) 
        
    def create_dropbox(self,DROP_XY=[0,0],DROP_SIZE=[0,0],DROP_COLOR=[1,0,0,1],DROP_FONT=None,DROP_TEXTUREID=0,
    DROPSHOW_HOVER=True,
    ENTRIES = [],
    ON_HOVER=None,ON_HOVER_RETRACT=None,HOVER_DELAY=100,
    ON_CLICK=None,ON_CLICK_RETRACT=None,CLICK_DELAY=100,
    COMMAND=None):
        
        
        drp = self.D2D.create_quad(DROP_XY,DROP_SIZE,DROP_COLOR,DROP_TEXTUREID)
        
        self.WIDGETS.append([drp,DROP_XY,DROP_SIZE,DROP_COLOR]) 
        
        ARGS = [[drp,DROP_XY,DROP_SIZE],]
        
        if len(ENTRIES) > 1:
            for i in ENTRIES:
                aew = self.D2D.create_quad([0,0],[0,0],DROP_COLOR,DROP_TEXTUREID)
                ARGS.append([aew]) 
        else:
            pass 
            
        
        if DROPSHOW_HOVER == True:
            pass # Show it 
            self.EVENT_MANAGER.add_event('Motion',[DROP_XY[0],DROP_XY[1],DROP_XY[0]+DROP_SIZE[0],DROP_XY[1]+DROP_SIZE[1]],
        (self._hover_dropbox,ARGS),
        (self._inv_hover_dropbox,ARGS)
        ,HOVER_DELAY)
            
            
        else:
            pass # show it when clicked 
        
    
    
    
    def create_button(self,BUTTON_XY=[0,0],BUTTON_SIZE=[0,0],BUTTON_COLOR=[1,0,0,1],BUTTON_TEXTUREID=0,
    ON_HOVER=None,ON_HOVER_RETRACT=None,HOVER_DELAY=100,
    ON_CLICK=None,ON_CLICK_RETRACT=None,CLICK_DELAY=100,
    COMMAND=None,
    TEXT=None,TEXT_FONT=None):
        but = self.D2D.create_quad(BUTTON_XY,BUTTON_SIZE,BUTTON_COLOR,BUTTON_TEXTUREID)
        if TEXT != None:
            if TEXT_FONT != None:
                pass
            else:print('Text is specified "'+TEXT+'" But TEXT_FONT is None? Please specify font.')
        self.WIDGETS.append([but,BUTTON_XY,BUTTON_SIZE,BUTTON_COLOR]) 
        
        if ON_CLICK == None:
            ON_CLICK = self._std_darken
        elif ON_CLICK == 'light':
            ON_CLICK = self._std_lighten
        elif ON_CLICK == 'darken':
            ON_CLICK = self._std_darken
        else:pass #OnClick is specified (If not properly it will raise error cannot call variable or something. 
        
        if ON_HOVER == None:
            ON_HOVER = self._std_darken
        elif ON_HOVER == 'light':
            ON_HOVER = self._std_lighten
        elif ON_HOVER == 'darken':
            ON_HOVER = self._std_darken
        else:pass 
        
        
        
        if ON_CLICK_RETRACT == None:
            ON_CLICK_RETRACT = self._std_clickback_color
            
        if ON_HOVER_RETRACT == None:
            ON_HOVER_RETRACT = self._std_hoverback_color
            
        if COMMAND == None:
            COMMAND = self._std_out
        
        
        ARGS = [but, BUTTON_XY, BUTTON_SIZE, BUTTON_COLOR, BUTTON_TEXTUREID, ON_HOVER,ON_HOVER_RETRACT, HOVER_DELAY, ON_CLICK, ON_CLICK_RETRACT, CLICK_DELAY, COMMAND]
        
        
        # Hover 
        self.EVENT_MANAGER.add_event('Motion',[BUTTON_XY[0],BUTTON_XY[1],BUTTON_XY[0]+BUTTON_SIZE[0],BUTTON_XY[1]+BUTTON_SIZE[1]],
        (ON_HOVER,ARGS),
        (ON_HOVER_RETRACT,ARGS)
        ,HOVER_DELAY)
        
        # Click 
        self.EVENT_MANAGER.add_event('LeftClick',[BUTTON_XY[0],BUTTON_XY[1],BUTTON_XY[0]+BUTTON_SIZE[0],BUTTON_XY[1]+BUTTON_SIZE[1]],
        (ON_CLICK,ARGS),
        (ON_CLICK_RETRACT,ARGS)
        ,CLICK_DELAY)
        
        # Command 
