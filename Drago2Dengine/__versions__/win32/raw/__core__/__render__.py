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
        
        
        
        
        
        
        
        
        
        
        
        