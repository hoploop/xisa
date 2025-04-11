from typing import List, Tuple
from player.models import CreateOperationStatement, CreateSelectorStatement, KeyPressOperation, KeyReleaseOperation, KeyTypeOperation, LabelSelector, MouseClickOperation, MouseDoubleClickOperation, MouseOperationButton, MousePressOperation, MouseReleaseOperation, MouseScrollOperation, Operation, OperationReference, PositionSelector, RegexSelector, RunOperationStatement, Selector, SelectorReference, Statement, TextSelector
from common.models.recorder import Action, Event, KeyPressEvent, KeyReleaseEvent, KeyTypeEvent, MouseButton, MouseClickEvent, MouseDoubleClickEvent, MousePressEvent, MouseReleaseEvent, MouseScrollEvent


class GrammarGenerator:
    
    def generateFromAction(self,action:Action, event: Event,declarative:bool=True,starterId:int=0)->Tuple[List[Statement],List[Statement],int]:
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
            
    def generateFromLabelAction(self,action:Action, event: Event,declarative:bool=True,starterId:int=0)->Tuple[List[Statement],List[Statement],int]:
         
        selector = LabelSelector(value=action.by_label,order=action.by_order)
        if declarative:
            starterId, selector_id = self.getNextId(starterId)
            stmt1 = CreateSelectorStatement(id=selector_id,selector=selector)
            starterId, operation_id = self.getNextId(starterId)
            op1 = self.generateOperationFromEvent(event,SelectorReference(reference=selector_id))
            stmt2 = CreateOperationStatement(id=operation_id,operation=op1)
            stmt3 = RunOperationStatement(operation=OperationReference(reference=operation_id))
            decs = [stmt1,stmt2]
            exs = [stmt3]
            return decs, exs , starterId
        else:
            op =  self.generateOperationFromEvent(event,selector)
            decs = []
            exs = [RunOperationStatement(operation=op)]
            return decs, exs, starterId
        
    def generateFromTextAction(self,action:Action, event: Event,declarative:bool=True,starterId:int=0)->Tuple[List[Statement],List[Statement],int]:
        selector = TextSelector(value=action.by_text,order=action.by_order)
        if declarative:
            starterId, selector_id = self.getNextId(starterId)
            stmt1 = CreateSelectorStatement(id=selector_id,selector=selector)
            starterId, operation_id = self.getNextId(starterId)
            op1 = self.generateOperationFromEvent(event,SelectorReference(reference=selector_id))
            stmt2 = CreateOperationStatement(id=operation_id,operation=op1)
            stmt3 = RunOperationStatement(operation=OperationReference(reference=operation_id))
            decs = [stmt1,stmt2]
            exs = [stmt3]
            return decs, exs , starterId
        else:
            op =  self.generateOperationFromEvent(event,selector)
            decs = []
            exs = [RunOperationStatement(operation=op)]
            return decs, exs, starterId
        
    def generateFromRegexAction(self,action:Action, event: Event,declarative:bool=True,starterId:int=0)->Tuple[List[Statement],List[Statement],int]:
        
        selector = RegexSelector(value=action.by_regex,order=action.by_order)
        
        if declarative:
            starterId, selector_id = self.getNextId(starterId)
            stmt1 = CreateSelectorStatement(id=selector_id,selector=selector)
            starterId, operation_id = self.getNextId(starterId)
            op1 = self.generateOperationFromEvent(event,SelectorReference(reference=selector_id))
            stmt2 = CreateOperationStatement(id=operation_id,operation=op1)
            stmt3 = RunOperationStatement(operation=OperationReference(reference=operation_id))
            decs = [stmt1,stmt2]
            exs = [stmt3]
            return decs, exs , starterId
        else:
            op =  self.generateOperationFromEvent(event,selector)
            decs = []
            exs = [RunOperationStatement(operation=op)]
            return decs, exs, starterId
        
    def generateFromPositionAction(self,action:Action, event: Event,declarative:bool=True,starterId:int=0)->Tuple[List[Statement],List[Statement],int]:
        
        selector = PositionSelector(x=action.by_position.x,y=action.by_position.y)
        
        if declarative:
            starterId, selector_id = self.getNextId(starterId)
            stmt1 = CreateSelectorStatement(id=selector_id,selector=selector)
            starterId, operation_id = self.getNextId(starterId)
            op1 = self.generateOperationFromEvent(event,SelectorReference(reference=selector_id))
            stmt2 = CreateOperationStatement(id=operation_id,operation=op1)
            stmt3 = RunOperationStatement(operation=OperationReference(reference=operation_id))
            decs = [stmt1,stmt2]
            exs = [stmt3]
            return decs, exs , starterId
        else:
            op =  self.generateOperationFromEvent(event,selector)
            decs = []
            exs = [RunOperationStatement(operation=op)]
            return decs, exs, starterId
        
    def generateOperationFromEvent(self,event:Event,selector:Selector)-> Operation:
        if isinstance(event,MousePressEvent):
            return MousePressOperation(selector=selector,button=self.generateFromMouseButton(event.button))
        
        if isinstance(event,MouseReleaseEvent):
            return MouseReleaseOperation(selector=selector,button=self.generateFromMouseButton(event.button))
        if isinstance(event,MouseClickEvent):
            return MouseClickOperation(selector=selector,button=self.generateFromMouseButton(event.button))
        if isinstance(event,MouseDoubleClickEvent):
            return MouseDoubleClickOperation(selector=selector,button=self.generateFromMouseButton(event.button))
        if isinstance(event,MouseScrollEvent):
            dx = event.dx
            dy = event.dy
            return MouseScrollOperation(dx=dx,dy=dy,selector=selector)
        if isinstance(event,KeyPressEvent): 
            return KeyPressOperation(value=event.key,selector=selector)
        if isinstance(event,KeyTypeEvent): 
            return KeyTypeOperation(value=event.key,selector=selector)
        if isinstance(event,KeyReleaseEvent): 
            return KeyReleaseOperation(value=event.key,selector=selector)
            
        
        
        
    def generateFromMouseButton(self,button:MouseButton) -> MouseOperationButton:
        if button == MouseButton.right:
            return MouseOperationButton.RIGHT
        elif button == MouseButton.middle:
            return MouseOperationButton.MIDDLE
        else:
            return MouseOperationButton.LEFT
    