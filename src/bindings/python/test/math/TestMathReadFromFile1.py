#
# @file    TestReadFromFile1.py
# @brief   Tests for reading MathML from files into ASTNodes.
#
# @author  Akiya Jouraku (Python conversion)
# @author  Sarah Keating 
#
# $Id:$
# $HeadURL:$
#
# This test file was converted from src/sbml/test/TestReadFromFile1.cpp
# with the help of conversion sciprt (ctest_converter.pl).
#
#<!---------------------------------------------------------------------------
# This file is part of libSBML.  Please visit http://sbml.org for more
# information about SBML, and the latest version of libSBML.
#
# Copyright 2005-2009 California Institute of Technology.
# Copyright 2002-2005 California Institute of Technology and
#                     Japan Science and Technology Corporation.
# 
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation.  A copy of the license agreement is provided
# in the file named "LICENSE.txt" included with this software distribution
# and also available online as http://sbml.org/software/libsbml/license.html
#--------------------------------------------------------------------------->*/
import sys
import unittest
import libsbml

class TestMathReadFromFile1(unittest.TestCase):


  def test_read_MathML_1(self):
    reader = libsbml.SBMLReader()
    d = libsbml.SBMLDocument()
    m = libsbml.Model()
    fd = libsbml.FunctionDefinition()
    ia = libsbml.InitialAssignment()
    kl = libsbml.KineticLaw()
    filename = "../../math/test/test-data/" 
    filename += "mathML_1.xml"
    d = reader.readSBML(filename)
    if (d == None):
      pass    
    m = d.getModel()
    self.assert_( m != None )
    self.assert_( m.getNumFunctionDefinitions() == 2 )
    self.assert_( m.getNumInitialAssignments() == 1 )
    self.assert_( m.getNumRules() == 2 )
    self.assert_( m.getNumReactions() == 1 )
    fd = m.getFunctionDefinition(0)
    fd_math = fd.getMath()
    self.assert_( fd_math.getType() == libsbml.AST_LAMBDA )
    self.assert_( fd_math.getNumChildren() == 2 )
    self.assert_((  "lambda(x, )" == libsbml.formulaToString(fd_math) ))
    self.assert_( fd_math.getParentSBMLObject() == fd )
    child = fd_math.getRightChild()
    self.assert_( child.getType() == libsbml.AST_UNKNOWN )
    self.assert_( child.getNumChildren() == 0 )
    self.assert_((  "" == libsbml.formulaToString(child) ))
    fd = m.getFunctionDefinition(1)
    fd1_math = fd.getMath()
    self.assert_( fd1_math.getType() == libsbml.AST_LAMBDA )
    self.assert_( fd1_math.getNumChildren() == 2 )
    self.assert_((  "lambda(x, true)" == libsbml.formulaToString(fd1_math) ))
    self.assert_( fd1_math.getParentSBMLObject() == fd )
    child1 = fd1_math.getRightChild()
    self.assert_( child1.getType() == libsbml.AST_CONSTANT_TRUE )
    self.assert_( child1.getNumChildren() == 0 )
    self.assert_((  "true" == libsbml.formulaToString(child1) ))
    ia = m.getInitialAssignment(0)
    ia_math = ia.getMath()
    self.assert_( ia_math.getType() == libsbml.AST_UNKNOWN )
    self.assert_( ia_math.getNumChildren() == 0 )
    self.assert_((  "" == libsbml.formulaToString(ia_math) ))
    self.assert_( ia_math.getParentSBMLObject() == ia )
    r = m.getRule(0)
    r_math = r.getMath()
    self.assert_( r_math.getType() == libsbml.AST_CONSTANT_TRUE )
    self.assert_( r_math.getNumChildren() == 0 )
    self.assert_((  "true" == libsbml.formulaToString(r_math) ))
    self.assert_( r_math.getParentSBMLObject() == r )
    r = m.getRule(1)
    r1_math = r.getMath()
    self.assert_( r1_math.getType() == libsbml.AST_REAL )
    self.assert_( r1_math.getNumChildren() == 0 )
    self.assert_((  "INF" == libsbml.formulaToString(r1_math) ))
    self.assert_( r1_math.getParentSBMLObject() == r )
    kl = m.getReaction(0).getKineticLaw()
    kl_math = kl.getMath()
    self.assert_( kl_math.getType() == libsbml.AST_REAL )
    self.assert_( kl_math.getNumChildren() == 0 )
    self.assert_((  "4.5" == libsbml.formulaToString(kl_math) ))
    self.assert_( kl_math.getParentSBMLObject() == kl )
    d = None
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestReadFromFile1))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
