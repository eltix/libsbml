#
# @file    TestParameterRule.py
# @brief   ParameterRule unit tests
#
# @author  Akiya Jouraku (Python conversion)
# @author  Ben Bornstein 
# 
# ====== WARNING ===== WARNING ===== WARNING ===== WARNING ===== WARNING ======
#
# DO NOT EDIT THIS FILE.
#
# This file was generated automatically by converting the file located at
# src/sbml/test/TestParameterRule.c
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


class TestParameterRule(unittest.TestCase):

  global PR
  PR = None

  def setUp(self):
    self.PR = libsbml.AssignmentRule(1,2)
    self.PR.setL1TypeCode(libsbml.SBML_PARAMETER_RULE)
    if (self.PR == None):
      pass    
    pass  

  def tearDown(self):
    _dummyList = [ self.PR ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_ParameterRule_create(self):
    self.assertTrue( self.PR.getTypeCode() == libsbml.SBML_ASSIGNMENT_RULE )
    self.assertTrue( self.PR.getL1TypeCode() == libsbml.SBML_PARAMETER_RULE )
    self.assertTrue( self.PR.getNotes() == None )
    self.assertTrue( self.PR.getAnnotation() == None )
    self.assertTrue( self.PR.getFormula() == "" )
    self.assertTrue( self.PR.getUnits() == "" )
    self.assertTrue( self.PR.getVariable() == "" )
    self.assertTrue( self.PR.getType() == libsbml.RULE_TYPE_SCALAR )
    self.assertEqual( False, self.PR.isSetVariable() )
    self.assertEqual( False, self.PR.isSetUnits() )
    pass  

  def test_ParameterRule_free_NULL(self):
    _dummyList = [ None ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_ParameterRule_setName(self):
    name =  "cell";
    self.PR.setVariable(name)
    self.assertTrue(( name == self.PR.getVariable() ))
    self.assertEqual( True, self.PR.isSetVariable() )
    if (self.PR.getVariable() == name):
      pass    
    c = self.PR.getVariable()
    self.PR.setVariable(c)
    self.assertTrue(( name == self.PR.getVariable() ))
    self.PR.setVariable("")
    self.assertEqual( False, self.PR.isSetVariable() )
    if (self.PR.getVariable() != None):
      pass    
    pass  

  def test_ParameterRule_setUnits(self):
    units =  "cell";
    self.PR.setUnits(units)
    self.assertTrue(( units == self.PR.getUnits() ))
    self.assertEqual( True, self.PR.isSetUnits() )
    if (self.PR.getUnits() == units):
      pass    
    self.PR.setUnits(self.PR.getUnits())
    self.assertTrue(( units == self.PR.getUnits() ))
    self.PR.setUnits("")
    self.assertEqual( False, self.PR.isSetUnits() )
    if (self.PR.getUnits() != None):
      pass    
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestParameterRule))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
