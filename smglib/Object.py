'''
Created on Jun 20, 2013

@author: Petr Muller
'''

class SMGObjectFactory:
  def __init__(self):
    self.ids = 1
    
  def getNewObject(self, size, validity=True):
    newObject = SMGObject(self.ids, size, validity)
    self.ids += 1

    return newObject
  
  def getNullObject(self):
    return SMGObject(0, 0, False)

class SMGObject(object):
  def __init__(self, objId, size, validity=True):
    self.id = objId
    self.size = size
    self.validity = validity

    self.hvedges = []
    self.ptedges = []
    
  def getId(self):
    return self.id

  def getHVEdges(self, offset=None, datatype=None):
    return_list = [ x for x in self.hvedges ]
    if offset is not None:
      return_list = [ x for x in return_list if x.getOffset() == offset ]
    if datatype is not None:
      return_list = [ x for x in return_list if x.getDataType() == datatype ]
    
    return return_list
  
  def addHVEdge(self, edge):
    self.hvedges.append(edge)
  
  def getPTEdges(self):
    return self.ptedges
  
  def addPTEdge(self, edge):
    self.ptedges.append(edge)
    
  def getSize(self):
    return self.size
  
  def isValid(self):
    return self.validity

  def __str__(self):
    if self.validity:
      return "#%i (%ib)" % (self.id, self.size)
    else:
      return "<invalid> #%i (%ib)" % (self.id, self.size)
      
    