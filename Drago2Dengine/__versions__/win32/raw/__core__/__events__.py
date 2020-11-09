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
        
    def edit_event(self,eventid,what):
        pass 
        
    def delete_event(self,event_id):
        # Deterimne event type ? (Event id [
        event_type = event_id[0]
        event_id = event_id[1:]
        
        if event_type == 'H':
            del self.hover_events[event_id] 
        elif event_type == 'R':
            del self.rclick_events[event_id] 
        elif event_type == 'L':
            del self.lclick_events[event_id] 
        elif event_type == 'M':
            del self.mclick_events[event_id]       
        elif event_type == 'K':
            del self.keypress_events[event_id] 
        
        

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
            return 'H'+str(len(self.hover_events)-1 )
        if dat == 'Button-1' or dat == 'MouseLC' or dat == 'LeftClick':
            event = [0]
            event.append(Cords)
            event.append(EventOn)
            event.append(EventOff)
            event.append(False)
            event.append(EventDelay)
            self.rclick_events.append(event)
            return 'R'+str(len(self.rclick_events)-1  )
        if dat == 'Button-2' or dat == 'MouseRC' or dat == 'RightClick':
            event = [0]
            event.append(Cords)
            event.append(EventOn)
            event.append(EventOff)
            event.append(False)
            event.append(EventDelay)
            self.lclick_events.append(event)
            return 'L'+str(len(self.lclick_events)-1)
        if dat == 'Button-3' or dat == 'MouseMC' or dat == 'MiddleClick':
            event = [0]
            event.append(Cords)
            event.append(EventOn)
            event.append(EventOff)
            event.append(False)
            event.append(EventDelay)
            self.mclick_events.append(event)
            return 'M'+str(len(self.mclick_events)-1)
        if dat == 'KeyPress':
            event = []
            event.append(EventOn)
            self.keypress_events.append(event)
            return 'K'+str(len(self.keypress_events)-1 )  
            
            
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