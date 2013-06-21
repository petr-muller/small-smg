#!/usr/bin/python3

'''
Created on Jun 20, 2013

@author: Petr Muller
'''
from smglib.SMG import ConstructivisticSMG
from smglib.Plotter import SMGPlotter
import sys

def getSMG():
  data_node = (0,0,4)
  smg = ConstructivisticSMG()
  stack_variable = smg.addPointer()
  tree_root = smg.createPointerTarget(stack_variable, data_node)
  
  tree_lvl2_left = smg.createPointerTarget(tree_root, data_node, offset=0)
  tree_lvl2_right = smg.createPointerTarget(tree_root, data_node, offset=8)
  
  tree_lvl3_ll = smg.createPointerTarget(tree_lvl2_left, data_node, offset=0)
  tree_lvl3_lr = smg.createPointerTarget(tree_lvl2_left, data_node, offset=8)
  
  tree_lvl3_rl = smg.createPointerTarget(tree_lvl2_right, data_node, offset=0)
  tree_lvl3_rr = smg.createPointerTarget(tree_lvl2_right, data_node, offset=8)
  
  for node in ( tree_root, tree_lvl2_left, tree_lvl2_right, tree_lvl3_ll,
                tree_lvl3_lr, tree_lvl3_rl, tree_lvl3_rr ):
    smg.setSomeValue(node, 16, 4)

  for node in ( tree_lvl3_ll, tree_lvl3_lr, tree_lvl3_rl, tree_lvl3_rr ):
    smg.setNullPointer(node, 0)
    smg.setNullPointer(node, 8)
  
  return smg

if __name__ == "__main__":
  smg = getSMG()
  plotter = SMGPlotter()
  plotter.plot(smg, sys.stdout)