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
        
        if txtid not in self.textures and txtid != -1:
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
        if txtid not in self.textures and txtid != -1:
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
