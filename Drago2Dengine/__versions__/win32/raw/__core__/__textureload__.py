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
    
