#
# @file    TestSyntaxChecker.py
# @brief   SyntaxChecker unit tests
#
# @author  Akiya Jouraku (Python conversion)
# @author  Sarah Keating 
# 
# ====== WARNING ===== WARNING ===== WARNING ===== WARNING ===== WARNING ======
#
# DO NOT EDIT THIS FILE.
#
# This file was generated automatically by converting the file located at
# src/sbml/test/TestSyntaxChecker.c
# using the conversion program dev/utilities/translateTests/translateTests.pl.
# Any changes made here will be lost the next time the file is regenerated.
#
# -----------------------------------------------------------------------------
# This file is part of libSBML.  Please visit http://sbml.org for more
# information about SBML, and the latest version of libSBML.
#
# Copyright 2005-2010 California Institute of Technology.
# Copyright 2002-2005 California Institute of Technology and
#                     Japan Science and Technology Corporation.
# 
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation.  A copy of the license agreement is provided
# in the file named "LICENSE.txt" included with this software distribution
# and also available online as http://sbml.org/software/libsbml/license.html
# -----------------------------------------------------------------------------

import sys
import unittest
import libsbml


class TestSyntaxChecker(unittest.TestCase):


  def test_SyntaxChecker_validID(self):
    self.assertTrue( libsbml.SyntaxChecker.isValidXMLID("cell") == True )
    self.assertTrue( libsbml.SyntaxChecker.isValidXMLID("1cell") == False )
    self.assertTrue( libsbml.SyntaxChecker.isValidXMLID("_cell") == True )
    pass  

  def test_SyntaxChecker_validId(self):
    self.assertTrue( libsbml.SyntaxChecker.isValidSBMLSId("cell") == True )
    self.assertTrue( libsbml.SyntaxChecker.isValidSBMLSId("1cell") == False )
    self.assertTrue( libsbml.SyntaxChecker.isValidSBMLSId("") == False )
    pass  

  def test_SyntaxChecker_validUnitId(self):
    self.assertTrue( libsbml.SyntaxChecker.isValidUnitSId("cell") == True )
    self.assertTrue( libsbml.SyntaxChecker.isValidUnitSId("1cell") == False )
    pass  

  def test_SyntaxChecker_validXHTML(self):
    NS24 = libsbml.SBMLNamespaces(2,4)
    NS31 = libsbml.SBMLNamespaces(3,1)
    toptriple = libsbml.XMLTriple("notes", "", "")
    triple = libsbml.XMLTriple("p", "", "")
    att = libsbml.XMLAttributes()
    ns = libsbml.XMLNamespaces()
    ns.add( "http://www.w3.org/1999/xhtml", "")
    tt = libsbml.XMLToken("This is my text")
    n1 = libsbml.XMLNode(tt)
    toptoken = libsbml.XMLToken(toptriple,att)
    topnode = libsbml.XMLNode(toptoken)
    token = libsbml.XMLToken(triple,att,ns)
    node = libsbml.XMLNode(token)
    node.addChild(n1)
    topnode.addChild(node)
    self.assertTrue( libsbml.SyntaxChecker.hasExpectedXHTMLSyntax(topnode,None) == True )
    self.assertTrue( libsbml.SyntaxChecker.hasExpectedXHTMLSyntax(topnode,NS24) == True )
    self.assertTrue( libsbml.SyntaxChecker.hasExpectedXHTMLSyntax(topnode,NS31) == True )
    triple = libsbml.XMLTriple("html", "", "")
    token = libsbml.XMLToken(triple,att,ns)
    node = libsbml.XMLNode(token)
    node.addChild(n1)
    topnode.removeChild(0)
    topnode.addChild(node)
    self.assertTrue( libsbml.SyntaxChecker.hasExpectedXHTMLSyntax(topnode,None) == True )
    self.assertTrue( libsbml.SyntaxChecker.hasExpectedXHTMLSyntax(topnode,NS24) == False )
    self.assertTrue( libsbml.SyntaxChecker.hasExpectedXHTMLSyntax(topnode,NS31) == True )
    triple = libsbml.XMLTriple("html", "", "")
    ns.clear()
    token = libsbml.XMLToken(triple,att,ns)
    node = libsbml.XMLNode(token)
    node.addChild(n1)
    topnode.removeChild(0)
    topnode.addChild(node)
    self.assertTrue( libsbml.SyntaxChecker.hasExpectedXHTMLSyntax(topnode,None) == False )
    self.assertTrue( libsbml.SyntaxChecker.hasExpectedXHTMLSyntax(topnode,NS24) == False )
    self.assertTrue( libsbml.SyntaxChecker.hasExpectedXHTMLSyntax(topnode,NS31) == False )
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestSyntaxChecker))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
