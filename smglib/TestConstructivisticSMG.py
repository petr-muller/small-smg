'''
Created on Jun 20, 2013

@author: Petr Muller
'''
import unittest
from smglib.SMG import ConstructivisticSMG

class ConstructivisticSMGTest(unittest.TestCase):
  def setUp(self):
    self.smg = ConstructivisticSMG()

  def test_addPointer(self):
    pointer = self.smg.addPointer()
    smgPointer = self.smg.getObject(pointer.getId())
    
    self.assertIs(pointer, smgPointer)
    self.assertTrue(smgPointer.isValid())
    self.assertEqual(self.smg.getPointerSize(), smgPointer.getSize())
    
  def test_createPointerTarget(self):
    data_type = (0,4,0,8)
    data_type_size = (2 * self.smg.getPointerSize()) + sum(data_type)

    pointer = self.smg.addPointer()
    node = self.smg.createPointerTarget(pointer, data_type)
    
    self.assertGreaterEqual(node.getSize(), data_type_size)
    
    hvedges = pointer.getHVEdges(offset=0, datatype=data_type)
    self.assertEqual(1, len(hvedges))
    
    value = hvedges[0].getValue()
    
    ptedge = value.getPTEdge()
    
    self.assertIs(ptedge.getObject(), node)
    self.assertEqual(0, ptedge.getOffset())

  def test_setSomeValue(self):
    obj = self.smg.addObject(16)
    edges = obj.getHVEdges()
    self.assertEqual(0, len(edges))

    value = self.smg.setSomeValue(obj, 8, 4)

    edges = obj.getHVEdges(offset=8)
    self.assertEqual(1, len(edges))
    edge = edges[0]
    self.assertIs(obj, edge.getObject())
    self.assertIs(value, edge.getValue())
    
    edges = obj.getHVEdges(datatype=4)
    self.assertEqual(1, len(edges))
    edge = edges[0]
    self.assertIs(obj, edge.getObject())
    self.assertIs(value, edge.getValue())

  def test_setNullPointer(self):
    obj = self.smg.addObject(16)
    self.smg.setNullPointer(obj, 0)

    edges = obj.getHVEdges(offset=0)
    self.assertEqual(1, len(edges))
    edge = edges[0]
    self.assertEquals(edge.getDataType(), self.smg.getPointerSize())
    self.assertIs(edge.getObject(), obj)
    self.assertIs(edge.getValue(), self.smg.getObject(0))