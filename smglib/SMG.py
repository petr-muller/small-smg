'''
Created on Jun 20, 2013

@author: Petr Muller
'''
from smglib.Object import SMGObjectFactory
from smglib.Value import SMGValueFactory
from smglib.PTEdge import SMGPTEdge
from smglib.HVEdge import SMGHVEdge

class SMG(object):
  def __init__(self):
    self.objects = {}
    self.values = {}
    
    self.factory_objects = SMGObjectFactory()
    self.factory_values = SMGValueFactory()
    
    null_object = self.factory_objects.getNullObject()
    null_value = self.factory_values.getNullValue()
    
    self._addObject(null_object)
    self._addValue(null_value)
    self.addPTEdge(0, null_value, null_object)

  def _addObject(self, smgObject):
    self.objects[smgObject.getId()] = smgObject
    
  def addObject(self, size, validity=True):
    new_object = self.factory_objects.getNewObject(size, validity)
    self._addObject(new_object)
    return new_object
  
  def getObject(self, objectId):
    return self.objects[objectId]
  
  def _addValue(self, smgValue):
    self.values[smgValue.getId()] = smgValue

  def addValue(self):
    new_value = self.factory_values.getNewValue()
    self._addValue(new_value)
    return new_value

  def getValue(self, valueId):
    return self.values[valueId]

  def addPTEdge(self, offset, value, smgObject):
    edge = SMGPTEdge(offset, value, smgObject)
    edge.wireToVertices()
    return edge

  def addHVEdge(self, offset, datatype, smg_object, value):
    edge = SMGHVEdge(offset, datatype, smg_object, value)
    edge.wireToVertices()
    return edge
  
  def getObjects(self):
    return self.objects.values()
  
  def getValues(self):
    return self.values.values()

  def __str__(self):
    return """\
== OBJECTS ==
%s
== VALUES  ==
%s
== HAS VALUE EDGES ==
%s
== POINTS TO EDGES ==
%s
""" % ( [str(x) for x in self.objects.values() ], [ str(x) for x in self.values.values() ],[ [ str(z) for z in y ] for y in [ x.getHVEdges() for x in self.objects.values() ]], [ str(x.getPTEdge()) for x in self.values.values() if x.getPTEdge() is not None])

class ConstructivisticSMG(SMG):
  def __init__(self):
    super(ConstructivisticSMG, self).__init__()
    self.pointerSize = 8

  def addPointer(self):
    return self.addObject(self.pointerSize)
  
  def getPointerSize(self):
    return self.pointerSize

  def createPointerTarget(self, obj, data_type, offset=0):
    value = self.addValue()
    
    data_type_size = sum(data_type) + (data_type.count(0) * self.pointerSize) 
    new_object = self.addObject(data_type_size)
    
    self.addHVEdge(offset, data_type, obj, value)
    self.addPTEdge(0, value, new_object)
    
    return new_object

  def setSomeValue(self, obj, offset, datatype):
    value = self.addValue()
    self.addHVEdge(offset, datatype, obj, value)
    return value
  
  def setNullPointer(self, obj, offset):
    self.addHVEdge(offset, self.pointerSize, obj, self.getValue(0))