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