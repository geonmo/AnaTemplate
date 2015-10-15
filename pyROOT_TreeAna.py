#!/usr/bin/env python
#-*- coding: utf-8 -*-
from ROOT import TFile
from ROOT import gDirectory
import sys,os
from optparse import OptionParser

class TreeAna :
  def __init__(self) :
    # open the file
    usage='''%prog -t ttll/tree <data.root>'''
    parser = OptionParser(usage=usage)
    parser.add_option("-t","--treee",action="store",type="string",dest="treePath",help="The path of the tree")
    (options, args) = parser.parse_args()
    if ( len(args) != 1 ) :
      print "please, see this usage"
      print parser. print_usage()
      sys.exit(-1)
    self.myfile = TFile( args[0] )
    self.treePath = options.treePath
  def Ana(self,mychain) :
    pass
    #for jpsi_mass in mychain.jpsi_mass :
    #  print jpsi_mass
  def Loop(self) :
    # retrieve the ntuple of interest
    mychain = self.myfile.Get( self.treePath )
    entries = mychain.GetEntriesFast()
    for jentry in xrange( entries ):
     # get the next tree in the chain and verify
       ientry = mychain.LoadTree( jentry )
       if ientry < 0:
          break
     # copy next entry into memory and verify
       nb = mychain.GetEntry( jentry )
       if nb <= 0:
          continue
       self.Ana(mychain)

## If directly use ths script,
if __name__ == "__main__" :
  ana = TreeAna( )
  ana.Loop()
