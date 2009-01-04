#
# @file    TestReadFromFile2.py
# @brief   Tests for reading MathML from files into ASTNodes.
#
# @author  Akiya Jouraku (Python conversion)
# @author  Sarah Keating 
#
# $Id:$
# $HeadURL:$
#
# This test file was converted from src/sbml/test/TestReadFromFile2.cpp
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

class TestMathReadFromFile2(unittest.TestCase):


  def test_read_MathML_2(self):
    reader = libsbml.SBMLReader()
    d = libsbml.SBMLDocument()
    m = libsbml.Model()
    fd = libsbml.FunctionDefinition()
    ia = libsbml.InitialAssignment()
    filename = "../../math/test/test-data/" 
    filename += "mathML_2.xml"
    d = reader.readSBML(filename)
    if (d == None):
      pass    
    m = d.getModel()
    self.assert_( m != None )
    self.assert_( m.getNumFunctionDefinitions() == 2 )
    self.assert_( m.getNumInitialAssignments() == 1 )
    self.assert_( m.getNumRules() == 2 )
    fd = m.getFunctionDefinition(0)
    fd_math = fd.getMath()
    self.assert_( fd_math.getType() == libsbml.AST_LAMBDA )
    self.assert_( fd_math.getNumChildren() == 1 )
    self.assert_((  "lambda()" == libsbml.formulaToString(fd_math) ))
    child = fd_math.getChild(0)
    self.assert_( child.getType() == libsbml.AST_UNKNOWN )
    self.assert_( child.getNumChildren() == 0 )
    self.assert_((  "" == libsbml.formulaToString(child) ))
    fd = m.getFunctionDefinition(1)
    fd1_math = fd.getMath()
    self.assert_( fd1_math.getType() == libsbml.AST_LAMBDA )
    self.assert_( fd1_math.getNumChildren() == 2 )
    self.assert_((                            "lambda(x, piecewise(p, leq(x, 4)))" == libsbml.formulaToString(fd1_math) ))
    child1 = fd1_math.getRightChild()
    self.assert_( child1.getType() == libsbml.AST_FUNCTION_PIECEWISE )
    self.assert_( child1.getNumChildren() == 2 )
    self.assert_((                                      "piecewise(p, leq(x, 4))" == libsbml.formulaToString(child1) ))
    c1 = child1.getChild(0)
    self.assert_( c1.getType() == libsbml.AST_NAME )
    self.assert_( c1.getNumChildren() == 0 )
    self.assert_((  "p" == libsbml.formulaToString(c1) ))
    c2 = child1.getChild(1)
    self.assert_( c2.getType() == libsbml.AST_RELATIONAL_LEQ )
    self.assert_( c2.getNumChildren() == 2 )
    self.assert_((  "leq(x, 4)" == libsbml.formulaToString(c2) ))
    ia = m.getInitialAssignment(0)
    ia_math = ia.getMath()
    self.assert_( ia_math.getType() == libsbml.AST_FUNCTION_PIECEWISE )
    self.assert_( ia_math.getNumChildren() == 4 )
    self.assert_((                      "piecewise(-x, lt(x, 0), 0, eq(x, 0))" == libsbml.formulaToString(ia_math) ))
    child1 = ia_math.getChild(0)
    child2 = ia_math.getChild(1)
    child3 = ia_math.getChild(2)
    child4 = ia_math.getChild(3)
    self.assert_( child1.getType() == libsbml.AST_MINUS )
    self.assert_( child1.getNumChildren() == 1 )
    self.assert_((  "-x" == libsbml.formulaToString(child1) ))
    self.assert_( child2.getType() == libsbml.AST_RELATIONAL_LT )
    self.assert_( child2.getNumChildren() == 2 )
    self.assert_((  "lt(x, 0)" == libsbml.formulaToString(child2) ))
    self.assert_( child3.getType() == libsbml.AST_REAL )
    self.assert_( child3.getNumChildren() == 0 )
    self.assert_((  "0" == libsbml.formulaToString(child3) ))
    self.assert_( child4.getType() == libsbml.AST_RELATIONAL_EQ )
    self.assert_( child4.getNumChildren() == 2 )
    self.assert_((  "eq(x, 0)" == libsbml.formulaToString(child4) ))
    r = m.getRule(0)
    r_math = r.getMath()
    self.assert_( r_math.getType() == libsbml.AST_CONSTANT_TRUE )
    self.assert_( r_math.getNumChildren() == 0 )
    self.assert_((  "true" == libsbml.formulaToString(r_math) ))
    r = m.getRule(1)
    r1_math = r.getMath()
    self.assert_( r1_math.getType() == libsbml.AST_FUNCTION_LOG )
    self.assert_( r1_math.getNumChildren() == 2 )
    self.assert_((  "log(3, x)" == libsbml.formulaToString(r1_math) ))
    child1 = r1_math.getChild(0)
    child2 = r1_math.getChild(1)
    self.assert_( child1.getType() == libsbml.AST_REAL )
    self.assert_( child1.getNumChildren() == 0 )
    self.assert_((  "3" == libsbml.formulaToString(child1) ))
    self.assert_( child2.getType() == libsbml.AST_NAME )
    self.assert_( child2.getNumChildren() == 0 )
    self.assert_((  "x" == libsbml.formulaToString(child2) ))
    d = None
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestReadFromFile2))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
