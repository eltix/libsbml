#
# @file    TestReadFromFile6.py
# @brief   Reads test-data/l2v2-newComponents.xml into memory and tests it.
#
# @author  Akiya Jouraku (Python conversion)
# @author  Sarah Keating 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestReadFromFile6.cpp
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

class TestReadFromFile6(unittest.TestCase):


  def test_read_l2v2_newComponents(self):
    reader = libsbml.SBMLReader()
    filename = "../../sbml/test/test-data/"
    filename += "l2v2-newComponents.xml"
    d = reader.readSBML(filename)
    if (d == None):
      pass    
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 2 )
    m = d.getModel()
    self.assert_( m != None )
    self.assert_( m.getId() ==  "l2v2_newComponents" )
    self.assert_( m.getSBOTerm() == 4 )
    self.assert_( m.getSBOTermID() ==  "SBO:0000004" )
    self.assert_( m.getNumCompartments() == 2 )
    c = m.getCompartment(0)
    self.assert_( c != None )
    self.assert_( c.getId() ==  "cell" )
    self.assert_( c.getCompartmentType() ==  "mitochondria" )
    self.assert_( c.getOutside() ==  "m" )
    self.assert_( c.getSBOTerm() == -1 )
    self.assert_( c.getSBOTermID() ==  "" )
    c = m.getCompartment(1)
    self.assert_( c != None )
    self.assert_( c.getId() ==  "m" )
    self.assert_( c.getCompartmentType() ==  "mitochondria" )
    self.assert_( m.getNumCompartmentTypes() == 1 )
    ct = m.getCompartmentType(0)
    self.assert_( ct != None )
    self.assert_( ct.getId() ==  "mitochondria" )
    loct = m.getListOfCompartmentTypes()
    ct1 = loct.get(0)
    self.assert_( ct1 == ct )
    ct1 = loct.get("mitochondria")
    self.assert_( ct1 == ct )
    self.assert_( m.getNumSpeciesTypes() == 1 )
    st = m.getSpeciesType(0)
    self.assert_( st != None )
    self.assert_( st.getId() ==  "Glucose" )
    self.assert_( m.getNumSpecies() == 2 )
    s = m.getSpecies(0)
    self.assert_( s != None )
    self.assert_( s.getId() ==  "X0" )
    self.assert_( s.getSpeciesType() ==  "Glucose" )
    self.assert_( s.getCompartment() ==  "cell" )
    self.assertEqual( False, s.isSetInitialAmount() )
    self.assertEqual( False, s.isSetInitialConcentration() )
    s = m.getSpecies(1)
    self.assert_( s != None )
    self.assert_( s.getId() ==  "X1" )
    self.assertEqual( False, s.isSetSpeciesType() )
    self.assert_( s.getCompartment() ==  "cell" )
    self.assert_( s.getInitialConcentration() == 0.013 )
    self.assertEqual( False, s.isSetInitialAmount() )
    self.assertEqual( True, s.isSetInitialConcentration() )
    self.assert_( m.getNumParameters() == 1 )
    p = m.getParameter(0)
    self.assert_( p != None )
    self.assert_( p.getId() ==  "y" )
    self.assert_( p.getValue() == 2 )
    self.assert_( p.getUnits() ==  "dimensionless" )
    self.assert_( p.getId() ==  "y" )
    self.assert_( p.getSBOTerm() == 2 )
    self.assert_( p.getSBOTermID() ==  "SBO:0000002" )
    self.assert_( m.getNumConstraints() == 1 )
    con = m.getConstraint(0)
    self.assert_( con != None )
    self.assert_( con.getSBOTerm() == 64 )
    self.assert_( con.getSBOTermID() ==  "SBO:0000064" )
    ast = con.getMath()
    self.assert_((  "lt(1, cell)" == libsbml.formulaToString(ast) ))
    locon = m.getListOfConstraints()
    con1 = locon.get(0)
    self.assert_( con1 == con )
    self.assert_( m.getNumInitialAssignments() == 1 )
    ia = m.getInitialAssignment(0)
    self.assert_( ia != None )
    self.assert_( ia.getSBOTerm() == 64 )
    self.assert_( ia.getSBOTermID() ==  "SBO:0000064" )
    self.assert_( ia.getSymbol() ==  "X0" )
    ast = ia.getMath()
    self.assert_((  "y * X1" == libsbml.formulaToString(ast) ))
    loia = m.getListOfInitialAssignments()
    ia1 = loia.get(0)
    self.assert_( ia1 == ia )
    ia1 = loia.get("X0")
    self.assert_( ia1 == ia )
    self.assert_( m.getNumReactions() == 1 )
    r = m.getReaction(0)
    self.assert_( r != None )
    self.assert_( r.getSBOTerm() == 231 )
    self.assert_( r.getSBOTermID() ==  "SBO:0000231" )
    self.assert_( r.getId() ==  "in" )
    lor = m.getListOfReactions()
    r1 = lor.get(0)
    self.assert_( r1 == r )
    r1 = lor.get("in")
    self.assert_( r1 == r )
    self.assertEqual( True, r.isSetKineticLaw() )
    kl = r.getKineticLaw()
    self.assert_( kl != None )
    self.assert_( kl.getSBOTerm() == 1 )
    self.assert_( kl.getSBOTermID() ==  "SBO:0000001" )
    self.assertEqual( True, kl.isSetMath() )
    ast = kl.getMath()
    self.assert_((  "v * X0 / t" == libsbml.formulaToString(ast) ))
    self.assert_( kl.getNumParameters() == 2 )
    p = kl.getParameter(0)
    self.assert_( p != None )
    self.assert_( p.getSBOTerm() == 2 )
    self.assert_( p.getSBOTermID() ==  "SBO:0000002" )
    self.assert_( p.getId() ==  "v" )
    self.assert_( p.getUnits() ==  "litre" )
    self.assert_( r.getNumReactants() == 1 )
    self.assert_( r.getNumProducts() == 0 )
    self.assert_( r.getNumModifiers() == 0 )
    sr = r.getReactant(0)
    self.assert_( sr != None )
    self.assert_( sr.getName() ==  "sarah" )
    self.assert_( sr.getId() ==  "me" )
    self.assert_( sr.getSpecies() ==  "X0" )
    losr = r.getListOfReactants()
    sr1 = losr.get(0)
    self.assert_( sr1 == sr )
    sr1 = losr.get("me")
    self.assert_( sr1 == sr )
    d = None
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestReadFromFile6))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
