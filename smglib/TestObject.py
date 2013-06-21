'''
Created on Jun 20, 2013

@author: Petr Muller
'''
import unittest
from smglib.Object import SMGObjectFactory, SMGObject
from smglib.Value import SMGValueFactory
from smglib.PTEdge import SMGPTEdge
from smglib.HVEdge import SMGHVEdge

class SMGObjectFactoryTest(unittest.TestCase):
  
  def setUp(self):
    self.factory = SMGObjectFactory()
  
  def test_getNullObject(self):
    null_object = self.factory.getNullObject()
    self.assertEqual(null_object.getId(), 0)
    
    null_object = self.factory.getNullObject()
    self.assertEqual(null_object.getId(), 0)
    
  def test_getNewObject(self):
    fobject = self.factory.getNewObject(4, True)
    sobject = self.factory.getNewObject(8, True)
    
    self.assertNotEqual(fobject.getId(), 0)
    self.assertNotEqual(sobject.getId(), 0)
    self.assertNotEqual(fobject.getId(), sobject.getId())

class SMGObjectConstructorTest(unittest.TestCase):
  def test_constructor(self):
    object1 = SMGObject(1, 4, True)
    object2 = SMGObject(2, 8, False)
    
    self.assertEqual(4, object1.getSize())
    self.assertEqual(8, object2.getSize())
    
    self.assertTrue(object1.isValid())
    self.assertFalse(object2.isValid())

class SMGObjectGenericTest(unittest.TestCase):
  def setUp(self):
    self.vfactory = SMGValueFactory()
    self.ofactory = SMGObjectFactory()

    self.object = self.ofactory.getNewObject(8)

  def test_getAddPTEdges(self):
    edges = self.object.getPTEdges()
    self.assertEqual(0, len(edges))
    
    edge = SMGPTEdge(0, self.vfactory.getNewValue(), self.object)
    self.object.addPTEdge(edge)
    
    edges = self.object.getPTEdges()
    self.assertEqual(1, len(edges))
    self.assertIs(edges[0], edge)

  def test_getAddHVEdges(self):
    edges = self.object.getHVEdges()
    self.assertEqual(0, len(edges))
    
    edge = SMGHVEdge(0, 0, self.object, self.vfactory.getNewValue())
    self.object.addHVEdge(edge)
    
    edges = self.object.getHVEdges()
    self.assertEqual(1, len(edges))
    self.assertIs(edges[0], edge)

  def test_getHVEdgesFiltered(self):
    obj = self.ofactory.getNewObject(16)
    val = self.vfactory.getNewValue()
    edgeAt0 = SMGHVEdge(0, 0, obj, val)
    edgeAt8 = SMGHVEdge(8, 4, obj, val)
    self.object.addHVEdge(edgeAt0)
    self.object.addHVEdge(edgeAt8)
    
    edges = self.object.getHVEdges(offset=0)
    self.assertEqual(1, len(edges))
    self.assertIn(edgeAt0, edges)
    
    edges = self.object.getHVEdges(datatype=4)
    self.assertEqual(1, len(edges))
    self.assertIn(edgeAt8, edges)