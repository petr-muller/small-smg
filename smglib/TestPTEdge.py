'''
Created on Jun 20, 2013

@author: Petr Muller
'''
import unittest
from smglib.Object import SMGObjectFactory
from smglib.Value import SMGValueFactory
from smglib.PTEdge import SMGPTEdge

class PTEdgeTest(unittest.TestCase):
  def setUp(self):
    self.ofactory = SMGObjectFactory()
    self.vfactory = SMGValueFactory()
    
  def test_constructor(self):
    obj = self.ofactory.getNewObject(4, True)
    val = self.vfactory.getNewValue()
    
    edge = SMGPTEdge(0, val, obj)
    
    self.assertIs(obj, edge.getObject())
    self.assertIs(val, edge.getValue())
    self.assertEqual(0, edge.getOffset())
    
    ptedges_to_object = obj.getPTEdges()
    ptedge_from_value = val.getPTEdge()
    
    self.assertEqual(len(ptedges_to_object), 0)
    self.assertIs(ptedge_from_value, None)
    
  def test_wireToVertices(self):
    obj = self.ofactory.getNewObject(4, True)
    val = self.vfactory.getNewValue()
    
    edge = SMGPTEdge(0, val, obj)
    edge.wireToVertices()
    
    ptedges_to_object = obj.getPTEdges()
    ptedge_from_value = val.getPTEdge()
    
    self.assertEqual(len(ptedges_to_object), 1)
    self.assertIs(ptedges_to_object[0], edge)
    
    self.assertIs(ptedge_from_value, edge)
    