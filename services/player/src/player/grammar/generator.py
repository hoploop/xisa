from typing import List, Tuple
from uuid import uuid4
from common.models.recorder import Action, Event, KeyPressEvent, KeyReleaseEvent, MouseButton, MouseClickEvent, MouseDoubleClickEvent, MousePressEvent, MouseReleaseEvent, MouseScrollEvent


class GrammarGenerator:
    
    def generateFromAction(self,action:Action, event: Event,declarative:bool=True,starterId:int=0)->Tuple[List[str],List[str],int]:
        if action.by_label is not None and action.by_label.strip()!='':
            return self.generateFromLabelAction(action,event,declarative,starterId)
        elif action.by_text is not None and action.by_text.strip()!='':
            return self.generateFromTextAction(action,event,declarative,starterId)
        elif action.by_regex is not None and action.by_regex.strip()!='':
            return self.generateFromRegexAction(action,event,declarative,starterId)
        elif action.by_position is not None:
            return self.generateFromPositionAction(action,event,declarative,starterId)
        
    def getNextId(self,starterId:int=0,prefix='ID_') -> Tuple[int,str]:
        return starterId+1, '{0}{1}'.format(prefix,starterId+1)
            
    def generateFromLabelAction(self,action:Action, event: Event,declarative:bool=True,starterId:int=0)->Tuple[List[str],List[str],int]:
        order = ''
        if len(action.by_order) > 0:
            for el in action.by_order:
                order += ',{0}'.format(el)
        selector = 'label("{0}"{1})'.format(action.by_label,order)
        
        if declarative:
            
            # Selector area
            starterId, selector_id = self.getNextId(starterId)
            
            selector_dec = '{0} = {1}'.format(selector_id,selector) # id = label(...)
            
            # Action area
            starterId, action_id = self.getNextId(starterId)
            action_text = self.generateFromEvent(event,selector_id)
            action_dec = '{0} = {1}'.format(action_id,action_text)
            
            # Finalization area
            decs = [selector_dec,action_dec]
            exs = [action_id]
            return decs, exs, starterId
    
        else:
            decs = []
            exs = [self.generateFromEvent(event,selector)]
            return decs, exs,starterId
        
    def generateFromTextAction(self,action:Action, event: Event,declarative:bool=True,starterId:int=0)->Tuple[List[str],List[str],int]:
        order = ''
        if len(action.by_order) > 0:
            for el in action.by_order:
                order += ',{0}'.format(el)
        selector = 'text("{0}"{1})'.format(action.by_text,order)
        
        if declarative:
            
            # Selector area
            starterId, selector_id = self.getNextId(starterId)
            
            selector_dec = '{0} = {1}'.format(selector_id,selector) # id = label(...)
            
            # Action area
            starterId, action_id = self.getNextId(starterId)
            action_text = self.generateFromEvent(event,selector_id)
            action_dec = '{0} = {1}'.format(action_id,action_text)
            
            # Finalization area
            decs = [selector_dec,action_dec]
            exs = [action_id]
            return decs, exs, starterId
    
        else:
            decs = []
            exs = [self.generateFromEvent(event,selector)]
            return decs, exs, starterId
        
    def generateFromRegexAction(self,action:Action, event: Event,declarative:bool=True,starterId:int=0)->Tuple[List[str],List[str],int]:
        order = ''
        if len(action.by_order) > 0:
            for el in action.by_order:
                order += ',{0}'.format(el)
        selector = 'regex("{0}"{1})'.format(action.by_regex,order)
        
        if declarative:
            
            # Selector area
            starterId, selector_id = self.getNextId(starterId)
            
            selector_dec = '{0} = {1}'.format(selector_id,selector) # id = label(...)
            
            # Action area
            starterId, action_id = self.getNextId(starterId)
            action_text = self.generateFromEvent(event,selector_id)
            action_dec = '{0} = {1}'.format(action_id,action_text)
            
            # Finalization area
            decs = [selector_dec,action_dec]
            exs = [action_id]
            return decs, exs, starterId
    
        else:
            decs = []
            exs = [self.generateFromEvent(event,selector)]
            return decs, exs, starterId
        
    def generateFromPositionAction(self,action:Action, event: Event,declarative:bool=True,starterId:int=0)->Tuple[List[str],List[str],int]:
        x_text = "{:.2f}".format(action.by_position.x)
        y_text = "{:.2f}".format(action.by_position.y)
        selector = 'position({0},{1})'.format(x_text,y_text)
        
        if declarative:
            
            # Selector area
            starterId, selector_id = self.getNextId(starterId)
            
            selector_dec = '{0} = {1}'.format(selector_id,selector) # id = label(...)
            
            # Action area
            starterId, action_id = self.getNextId(starterId)
            action_text = self.generateFromEvent(event,selector_id)
            action_dec = '{0} = {1}'.format(action_id,action_text)
            
            # Finalization area
            decs = [selector_dec,action_dec]
            exs = [action_id]
            return decs, exs , starterId
    
        else:
            decs = []
            exs = [self.generateFromEvent(event,selector)]
            return decs, exs, starterId
        
    def generateFromEvent(self,event:Event,selector:str)-> Tuple[str,str]:
        if isinstance(event,MousePressEvent):
            button_text = self.generateFromMouseButton(event.button)
            return 'mousePress({0},{1})'.format(selector,button_text)
        if isinstance(event,MouseReleaseEvent):
            button_text = self.generateFromMouseButton(event.button)
            return 'mouseRelease({0},{1})'.format(selector,button_text)
        if isinstance(event,MouseClickEvent):
            button_text = self.generateFromMouseButton(event.button)
            return 'mouseClick({0},{1})'.format(selector,button_text)
        if isinstance(event,MouseDoubleClickEvent):
            button_text = self.generateFromMouseButton(event.button)
            return 'mouseDoubleClick({0},{1})'.format(selector,button_text)
        if isinstance(event,MouseScrollEvent):
            dx = event.dx
            dy = event.dy
            return 'mouseScroll({0},{1})'.format(dx,dy)
        if isinstance(event,KeyPressEvent): 
            key_text = '"{0}"'.format(event.key)
            return 'keyPress({0})'.format(key_text)
        if isinstance(event,KeyReleaseEvent): 
            key_text = '"{0}"'.format(event.key)
            return 'keyRelease({0})'.format(key_text)
        
        
    def generateFromMouseButton(self,button:MouseButton) -> str:
        if button == MouseButton.right:
            return 'right'
        elif button == MouseButton.middle:
            return 'middle'
        else:
            return 'left'
    