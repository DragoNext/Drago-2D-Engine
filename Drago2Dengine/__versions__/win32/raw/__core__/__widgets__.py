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