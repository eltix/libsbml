#
# @file    TestAnnotationCopyAndClone.py
# @brief   Test the copy and clone methods for annotation classes
#
# @author  Akiya Jouraku (Python conversion)
# @author  Sarah Keating 
# 
# ====== WARNING ===== WARNING ===== WARNING ===== WARNING ===== WARNING ======
#
# DO NOT EDIT THIS FILE.
#
# This file was generated automatically by converting the file located at
# src/annotation/test/TestCopyAndClone.cpp
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


class TestAnnotationCopyAndClone(unittest.TestCase):


  def test_CVTerm_assignmentOperator(self):
    CVTerm1 = libsbml.CVTerm(libsbml.BIOLOGICAL_QUALIFIER)
    CVTerm1.addResource("http://www.geneontology.org/#GO:0005892")
    self.assertTrue( CVTerm1.getQualifierType() == libsbml.BIOLOGICAL_QUALIFIER )
    self.assertTrue( CVTerm1.getResources().getLength() == 1 )
    self.assertTrue( CVTerm1.getResources().getValue(0) ==  "http://www.geneontology.org/#GO:0005892" )
    CVTerm2 = libsbml.CVTerm()
    CVTerm2 = CVTerm1
    self.assertTrue( CVTerm2.getQualifierType() == libsbml.BIOLOGICAL_QUALIFIER )
    self.assertTrue( CVTerm2.getResources().getLength() == 1 )
    self.assertTrue( CVTerm2.getResources().getValue(0) ==  "http://www.geneontology.org/#GO:0005892" )
    CVTerm2 = None
    CVTerm1 = None
    pass  

  def test_CVTerm_clone(self):
    CVTerm1 = libsbml.CVTerm(libsbml.BIOLOGICAL_QUALIFIER)
    CVTerm1.addResource("http://www.geneontology.org/#GO:0005892")
    self.assertTrue( CVTerm1.getQualifierType() == libsbml.BIOLOGICAL_QUALIFIER )
    self.assertTrue( CVTerm1.getResources().getLength() == 1 )
    self.assertTrue( CVTerm1.getResources().getValue(0) ==  "http://www.geneontology.org/#GO:0005892" )
    CVTerm2 = CVTerm1.clone()
    self.assertTrue( CVTerm2.getQualifierType() == libsbml.BIOLOGICAL_QUALIFIER )
    self.assertTrue( CVTerm2.getResources().getLength() == 1 )
    self.assertTrue( CVTerm2.getResources().getValue(0) ==  "http://www.geneontology.org/#GO:0005892" )
    CVTerm2 = None
    CVTerm1 = None
    pass  

  def test_CVTerm_copyConstructor(self):
    CVTerm1 = libsbml.CVTerm(libsbml.BIOLOGICAL_QUALIFIER)
    CVTerm1.addResource("http://www.geneontology.org/#GO:0005892")
    self.assertTrue( CVTerm1.getQualifierType() == libsbml.BIOLOGICAL_QUALIFIER )
    self.assertTrue( CVTerm1.getResources().getLength() == 1 )
    self.assertTrue( CVTerm1.getResources().getValue(0) ==  "http://www.geneontology.org/#GO:0005892" )
    CVTerm2 = libsbml.CVTerm(CVTerm1)
    self.assertTrue( CVTerm2.getQualifierType() == libsbml.BIOLOGICAL_QUALIFIER )
    self.assertTrue( CVTerm2.getResources().getLength() == 1 )
    self.assertTrue( CVTerm2.getResources().getValue(0) ==  "http://www.geneontology.org/#GO:0005892" )
    CVTerm2 = None
    CVTerm1 = None
    pass  

  def test_Date_assignmentOperator(self):
    date = libsbml.Date(2005,12,30,12,15,45,1,2,0)
    self.assertTrue( date.getMonth() == 12 )
    self.assertTrue( date.getSecond() == 45 )
    date2 = libsbml.Date()
    date2 = date
    self.assertTrue( date2.getMonth() == 12 )
    self.assertTrue( date2.getSecond() == 45 )
    date2 = None
    date = None
    pass  

  def test_Date_clone(self):
    date = libsbml.Date(2005,12,30,12,15,45,1,2,0)
    self.assertTrue( date.getMonth() == 12 )
    self.assertTrue( date.getSecond() == 45 )
    date2 = date.clone()
    self.assertTrue( date2.getMonth() == 12 )
    self.assertTrue( date2.getSecond() == 45 )
    date2 = None
    date = None
    pass  

  def test_Date_copyConstructor(self):
    date = libsbml.Date(2005,12,30,12,15,45,1,2,0)
    self.assertTrue( date.getMonth() == 12 )
    self.assertTrue( date.getSecond() == 45 )
    date2 = libsbml.Date(date)
    self.assertTrue( date2.getMonth() == 12 )
    self.assertTrue( date2.getSecond() == 45 )
    date2 = None
    date = None
    pass  

  def test_ModelCreator_assignmentOperator(self):
    mc = libsbml.ModelCreator()
    mc.setFamilyName("Keating")
    mc.setEmail("sbml-team@caltech.edu")
    self.assertTrue( mc.getFamilyName() ==  "Keating" )
    self.assertTrue( mc.getEmail() ==  "sbml-team@caltech.edu" )
    mc2 = libsbml.ModelCreator()
    mc2 = mc
    self.assertTrue( mc2.getFamilyName() ==  "Keating" )
    self.assertTrue( mc2.getEmail() ==  "sbml-team@caltech.edu" )
    mc2 = None
    mc = None
    pass  

  def test_ModelCreator_clone(self):
    mc = libsbml.ModelCreator()
    mc.setFamilyName("Keating")
    mc.setEmail("sbml-team@caltech.edu")
    self.assertTrue( mc.getFamilyName() ==  "Keating" )
    self.assertTrue( mc.getEmail() ==  "sbml-team@caltech.edu" )
    mc2 = mc.clone()
    self.assertTrue( mc2.getFamilyName() ==  "Keating" )
    self.assertTrue( mc2.getEmail() ==  "sbml-team@caltech.edu" )
    mc2 = None
    mc = None
    pass  

  def test_ModelCreator_copyConstructor(self):
    mc = libsbml.ModelCreator()
    mc.setFamilyName("Keating")
    mc.setEmail("sbml-team@caltech.edu")
    self.assertTrue( mc.getFamilyName() ==  "Keating" )
    self.assertTrue( mc.getEmail() ==  "sbml-team@caltech.edu" )
    mc2 = libsbml.ModelCreator(mc)
    self.assertTrue( mc2.getFamilyName() ==  "Keating" )
    self.assertTrue( mc2.getEmail() ==  "sbml-team@caltech.edu" )
    mc2 = None
    mc = None
    pass  

  def test_ModelHistory_assignmentOperator(self):
    mh = libsbml.ModelHistory()
    mc = libsbml.ModelCreator()
    mc.setGivenName("Sarah")
    mc.setFamilyName("Keating")
    mc.setEmail("sbml-team@caltech.edu")
    mh.addCreator(mc)
    mc = None
    date = libsbml.Date(2005,12,30,12,15,45,1,2,0)
    mh.setCreatedDate(date)
    date = None
    self.assertTrue( mh.getCreatedDate().getMonth() == 12 )
    self.assertTrue( mh.getCreatedDate().getSecond() == 45 )
    self.assertTrue( mh.getCreator(0).getFamilyName() ==  "Keating" )
    mh2 = libsbml.ModelHistory()
    mh2 = mh
    self.assertTrue( mh2.getCreatedDate().getMonth() == 12 )
    self.assertTrue( mh2.getCreatedDate().getSecond() == 45 )
    self.assertTrue( mh2.getCreator(0).getFamilyName() ==  "Keating" )
    mh2 = None
    mh = None
    pass  

  def test_ModelHistory_clone(self):
    mh = libsbml.ModelHistory()
    mc = libsbml.ModelCreator()
    mc.setFamilyName("Keating")
    mc.setGivenName("Sarah")
    mc.setEmail("sbml-team@caltech.edu")
    mh.addCreator(mc)
    mc = None
    date = libsbml.Date(2005,12,30,12,15,45,1,2,0)
    mh.setCreatedDate(date)
    date = None
    self.assertTrue( mh.getCreatedDate().getMonth() == 12 )
    self.assertTrue( mh.getCreatedDate().getSecond() == 45 )
    self.assertTrue( mh.getCreator(0).getFamilyName() ==  "Keating" )
    mh2 = mh.clone()
    self.assertTrue( mh2.getCreatedDate().getMonth() == 12 )
    self.assertTrue( mh2.getCreatedDate().getSecond() == 45 )
    self.assertTrue( mh2.getCreator(0).getFamilyName() ==  "Keating" )
    mh2 = None
    mh = None
    pass  

  def test_ModelHistory_copyConstructor(self):
    mh = libsbml.ModelHistory()
    mc = libsbml.ModelCreator()
    mc.setFamilyName("Keating")
    mc.setGivenName("Sarah")
    mc.setEmail("sbml-team@caltech.edu")
    mh.addCreator(mc)
    mc = None
    date = libsbml.Date(2005,12,30,12,15,45,1,2,0)
    mh.setCreatedDate(date)
    date = None
    self.assertTrue( mh.getCreatedDate().getMonth() == 12 )
    self.assertTrue( mh.getCreatedDate().getSecond() == 45 )
    self.assertTrue( mh.getCreator(0).getFamilyName() ==  "Keating" )
    mh2 = libsbml.ModelHistory(mh)
    self.assertTrue( mh2.getCreatedDate().getMonth() == 12 )
    self.assertTrue( mh2.getCreatedDate().getSecond() == 45 )
    self.assertTrue( mh2.getCreator(0).getFamilyName() ==  "Keating" )
    mh2 = None
    mh = None
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestAnnotationCopyAndClone))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)

