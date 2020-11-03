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