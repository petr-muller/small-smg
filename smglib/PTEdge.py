'''
Created on Jun 20, 2013

@author: Petr Muller
'''

class SMGPTEdge:
  def __init__(self, offset, edgeValue, edgeObject):
    self.offset = offset
    self.value = edgeValue
    self.object = edgeObject

  def wireToVertices(self):
    self.object.addPTEdge(self)
    self.value.setPTEdge(self)
    
  def getObject(self):
    return self.object
  
  def getValue(self):
    return self.value
  
  def getOffset(self):
    return self.offset
  
  def __str__(self):
    return "%s --> %s[%i]" % ( self.value, self.object, self.offset)