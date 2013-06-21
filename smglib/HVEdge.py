'''
Created on Jun 20, 2013

@author: Petr Muller
'''

class SMGHVEdge:
  def __init__(self, offset, edgeType, edgeObject, edgeValue):
    self.offset = offset
    self.type = edgeType
    self.object = edgeObject
    self.value = edgeValue

  def wireToVertices(self):
    self.object.addHVEdge(self)
    self.value.addHVEdge(self)

  def getObject(self):
    return self.object
  
  def getValue(self):
    return self.value
  
  def getOffset(self):
    return self.offset
  
  def getDataType(self):
    return self.type
  
  def __str__(self):
    return "%s --%i--%s--> %s" % (self.object, self.offset, self.type, self.value)