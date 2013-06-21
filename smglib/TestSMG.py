'''
Created on Jun 20, 2013

@author: Petr Muller
'''
import unittest
from smglib.SMG import SMG

class SMGConstructorTest(unittest.TestCase):
  def test_constructor(self):
    smg = SMG()
    self.assertIsNotNone(smg)

class SMGBasicTest(unittest.TestCase):
  def setUp(self):
    self.smg = SMG()
    self.fobject = self.smg.addObject(4)
    self.sobject = self.smg.addObject(16)
    
    self.fvalue = self.smg.addValue()
    self.svalue = self.smg.addValue()

  def test_addPTEdge(self):
    fedge = self.smg.addPTEdge(0, self.fvalue, self.fobject)
    self.assertIs(self.fvalue.getPTEdge(), fedge)
    self.assertIn(fedge, self.fobject.getPTEdges())
    
  def test_addGetObject(self):
    obj4b = self.smg.addObject(4)
    obj8b = self.smg.addObject(8, False)
    
    smgObj4b = self.smg.getObject(obj4b.getId())
    smgObj8b = self.smg.getObject(obj8b.getId())
    
    self.assertIs(obj4b, smgObj4b)
    self.assertIs(obj8b, smgObj8b)
    
    self.assertEqual(4, smgObj4b.getSize())
    self.assertEqual(8, smgObj8b.getSize())
    
    self.assertTrue(smgObj4b.isValid())
    self.assertFalse(smgObj8b.isValid())

  def test_addGetValue(self):
    val1 = self.smg.addValue()
    val2 = self.smg.addValue()

    self.assertIsNot(val1, val2)

    smgVal1 = self.smg.getValue(val1.getId())
    smgVal2 = self.smg.getValue(val2.getId())

    self.assertIs(val1, smgVal1)
    self.assertIs(val2, smgVal2)