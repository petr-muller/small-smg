'''
Created on Jun 20, 2013

@author: Petr Muller
'''
import unittest
from smglib.Object import SMGObjectFactory
from smglib.Value import SMGValueFactory
from smglib.HVEdge import SMGHVEdge

class HVEdgeTest(unittest.TestCase):
  def setUp(self):
    self.ofactory = SMGObjectFactory()
    self.vfactory = SMGValueFactory()
    
  def test_constructor(self):
    obj = self.ofactory.getNewObject(8, True)
    val = self.vfactory.getNewValue()
    
    edge = SMGHVEdge(0, 0, obj, val)
    
    self.assertIs(obj, edge.getObject())
    self.assertIs(val, edge.getValue())
    self.assertEqual(0, edge.getOffset())
    self.assertEqual(0, edge.getDataType())
    
    hvedges_from_object = obj.getHVEdges()
    hvedges_to_value = val.getHVEdges()
    
    self.assertEqual(len(hvedges_from_object), 0)
    self.assertEqual(len(hvedges_to_value), 0)
    
  def test_wireToVertices(self):
    obj = self.ofactory.getNewObject(8, True)
    val = self.vfactory.getNewValue()
    
    edge = SMGHVEdge(0, 0, obj, val)
    edge.wireToVertices()
    
    hvedges_from_object = obj.getHVEdges()
    hvedges_to_value = val.getHVEdges()
    
    self.assertEqual(len(hvedges_from_object), 1)
    self.assertIn(edge, hvedges_from_object)
    self.assertEqual(len(hvedges_to_value), 1)
    self.assertIn(edge, hvedges_to_value)