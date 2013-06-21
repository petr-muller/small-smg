'''
Created on Jun 20, 2013

@author: Petr Muller
'''

class SMGValueFactory:
  def __init__(self):
    self.ids = 1
    
  def getNewValue(self):
    value = SMGValue(self.ids)
    self.ids += 1
    
    return value
  
  def getNullValue(self):
    return SMGValue(0)

class SMGValue(object):
  def __init__(self, pValue):
    self.ptedge = None
    self.hvedges = []
    self.value = pValue    

  def getId(self):
    return self.value
  
  def getPTEdge(self):
    return self.ptedge
  
  def setPTEdge(self, edge):
    self.ptedge = edge
  
  def getHVEdges(self, offset=None):
    if offset is None:
      return self.hvedges
    else:
      return [ x for x in self.hvedges if x.getOffset() == offset ]
  
  def addHVEdge(self, edge):
    self.hvedges.append(edge)
  
  def __str__(self):
    return "%i" % self.value