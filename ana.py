#!/usr/bin/env python
from pyROOT_TreeAna import TreeAna

class JpsiAna(TreeAna) :
  def __init__(self) :
    TreeAna.__init__(self)
  def Ana( self, mychain) :
    for jpsi_mass in mychain.jpsi_mass :
      print jpsi_mass
   
## If directly use ths script,
if __name__ == "__main__" :
  ana = JpsiAna( )
  ana.Loop()

