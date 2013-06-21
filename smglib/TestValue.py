'''
Created on Jun 20, 2013

@author: Petr Muller
'''
import unittest
from smglib.Value import SMGValueFactory
from smglib.Object import SMGObjectFactory
from smglib.PTEdge import SMGPTEdge
from smglib.HVEdge import SMGHVEdge

class SMGValueFactoryTest(unittest.TestCase):
  def setUp(self):
    self.factory = SMGValueFactory()
    
  def test_getNullValue(self):
    value = self.factory.getNullValue()
    self.assertEqual(value.getId(), 0)
    value = self.factory.getNullValue()
    self.assertEqual(value.getId(), 0)

class SMGValueTest(unittest.TestCase):
  def setUp(self):
    self.ofactory = SMGObjectFactory()
    self.vfactory = SMGValueFactory()
    
    self.value = self.vfactory.getNewValue()

  def test_getSetPTEdge(self):
    self.assertIsNone(self.value.getPTEdge())
    
    edge = SMGPTEdge(0, self.value, self.ofactory.getNewObject(8))
    self.value.setPTEdge(edge)
    
    self.assertIs(edge, self.value.getPTEdge())

  def test_getAddHVEdge(self):
    self.assertEqual(0, len(self.value.getHVEdges()))
    
    edge = SMGHVEdge(0, 0, self.ofactory.getNewObject(8), self.value)
    self.value.addHVEdge(edge)
    
    edges = self.value.getHVEdges()
    self.assertIn(edge, edges)
    self.assertEqual(1, len(edges))

  def test_getHVEdgesFiltered(self):
    obj = self.ofactory.getNewObject(16)
    edgeAt0 = SMGHVEdge(0, 0, obj, self.value)
    edgeAt8 = SMGHVEdge(8, 0, obj, self.value)
    self.value.addHVEdge(edgeAt0)
    self.value.addHVEdge(edgeAt8)
    
    edges = self.value.getHVEdges(offset=0)
    self.assertEqual(1, len(edges))
    self.assertIn(edgeAt0, edges)