#
# @file    TestXMLAttributesC.py
# @brief   XMLAttributes unit tests, C version
#
# @author  Akiya Jouraku (Python conversion)
# @author  Sarah Keating 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestXMLAttributesC.c
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

class TestXMLAttributesC(unittest.TestCase):


  def test_XMLAttributes_add1(self):
    xa = libsbml.XMLAttributes()
    xt2 = libsbml.XMLTriple("name2", "http://name2.org/", "p2")
    i = xa.add( "name1", "val1", "http://name1.org/", "p1")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    i = xa.add(xt2, "val2")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( xa.getLength() == 2 )
    self.assert_( xa.isEmpty() == False )
    i = xa.add( "noprefix", "val3")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( xa.getLength() == 3 )
    self.assert_( xa.isEmpty() == False )
    xa = None
    xt2 = None
    pass  

  def test_XMLAttributes_add_remove_qname_C(self):
    xa = libsbml.XMLAttributes()
    xt1 = libsbml.XMLTriple("name1", "http://name1.org/", "p1")
    xt2 = libsbml.XMLTriple("name2", "http://name2.org/", "p2")
    xt3 = libsbml.XMLTriple("name3", "http://name3.org/", "p3")
    xt1a = libsbml.XMLTriple("name1", "http://name1a.org/", "p1a")
    xt2a = libsbml.XMLTriple("name2", "http://name2a.org/", "p2a")
    xa.add( "name1", "val1", "http://name1.org/", "p1")
    xa.add(xt2, "val2")
    self.assert_( xa.getLength() == 2 )
    self.assert_( xa.isEmpty() == False )
    self.assert_( (  "name1" != xa.getName(0) ) == False )
    self.assert_( (  "val1"  != xa.getValue(0) ) == False )
    self.assert_( (  "http://name1.org/" != xa.getURI(0) ) == False )
    self.assert_( (  "p1"    != xa.getPrefix(0) ) == False )
    self.assert_( (  "name2" != xa.getName(1) ) == False )
    self.assert_( (  "val2"  != xa.getValue(1) ) == False )
    self.assert_( (  "http://name2.org/" != xa.getURI(1) ) == False )
    self.assert_( (  "p2"    != xa.getPrefix(1) ) == False )
    self.assert_( (  "val1"  != xa.getValue( "name1") ) == False )
    self.assert_( (  "val2"  != xa.getValue( "name2") ) == False )
    self.assert_( (  "val1"  != xa.getValue( "name1", "http://name1.org/") ) == False )
    self.assert_( (  "val2"  != xa.getValue( "name2", "http://name2.org/") ) == False )
    self.assert_( (  "val1"  != xa.getValue(xt1) ) == False )
    self.assert_( (  "val2"  != xa.getValue(xt2) ) == False )
    self.assert_( xa.hasAttribute(-1) == False )
    self.assert_( xa.hasAttribute(2) == False )
    self.assert_( xa.hasAttribute(0) == True )
    self.assert_( xa.hasAttribute( "name1", "http://name1.org/") == True )
    self.assert_( xa.hasAttribute( "name2", "http://name2.org/") == True )
    self.assert_( xa.hasAttribute( "name3", "http://name3.org/") == False )
    self.assert_( xa.hasAttribute(xt1) == True )
    self.assert_( xa.hasAttribute(xt2) == True )
    self.assert_( xa.hasAttribute(xt3) == False )
    xa.add( "noprefix", "val3")
    self.assert_( xa.getLength() == 3 )
    self.assert_( xa.isEmpty() == False )
    self.assert_( (  "noprefix" != xa.getName(2) ) == False )
    self.assert_( (  "val3"     != xa.getValue(2) ) == False )
    self.assert_( xa.getURI(2) == "" )
    self.assert_( xa.getPrefix(2) == "" )
    self.assert_( (  "val3"  != xa.getValue( "noprefix", "") ) == False )
    self.assert_( xa.hasAttribute( "noprefix"    ) == True )
    self.assert_( xa.hasAttribute( "noprefix", "") == True )
    xa.add(xt1, "mval1")
    xa.add( "name2", "mval2", "http://name2.org/", "p2")
    xa.add( "noprefix", "mval3")
    self.assert_( xa.getLength() == 3 )
    self.assert_( xa.isEmpty() == False )
    self.assert_( (  "name1" != xa.getName(0) ) == False )
    self.assert_( (  "mval1" != xa.getValue(0) ) == False )
    self.assert_( (  "http://name1.org/" != xa.getURI(0) ) == False )
    self.assert_( (  "p1"    != xa.getPrefix(0) ) == False )
    self.assert_( (  "name2"    != xa.getName(1) ) == False )
    self.assert_( (  "mval2"    != xa.getValue(1) ) == False )
    self.assert_( (  "http://name2.org/" != xa.getURI(1) ) == False )
    self.assert_( (  "p2"       != xa.getPrefix(1) ) == False )
    self.assert_( (  "noprefix" != xa.getName(2) ) == False )
    self.assert_( (  "mval3"    != xa.getValue(2) ) == False )
    self.assert_( xa.getURI(2) == "" )
    self.assert_( xa.getPrefix(2) == "" )
    self.assert_( xa.hasAttribute(xt1) == True )
    self.assert_( xa.hasAttribute( "name1", "http://name1.org/") == True )
    self.assert_( xa.hasAttribute( "noprefix") == True )
    xa.add(xt1a, "val1a")
    xa.add(xt2a, "val2a")
    self.assert_( xa.getLength() == 5 )
    self.assert_( (  "name1" != xa.getName(3) ) == False )
    self.assert_( (  "val1a" != xa.getValue(3) ) == False )
    self.assert_( (  "http://name1a.org/" != xa.getURI(3) ) == False )
    self.assert_( (  "p1a" != xa.getPrefix(3) ) == False )
    self.assert_( (  "name2" != xa.getName(4) ) == False )
    self.assert_( (  "val2a" != xa.getValue(4) ) == False )
    self.assert_( (  "http://name2a.org/" != xa.getURI(4) ) == False )
    self.assert_( (  "p2a" != xa.getPrefix(4) ) == False )
    self.assert_( (  "mval1"  != xa.getValue( "name1") ) == False )
    self.assert_( (  "mval2"  != xa.getValue( "name2") ) == False )
    self.assert_( (  "val1a"  != xa.getValue( "name1", "http://name1a.org/") ) == False )
    self.assert_( (  "val2a"  != xa.getValue( "name2", "http://name2a.org/") ) == False )
    self.assert_( (  "val1a"  != xa.getValue(xt1a) ) == False )
    self.assert_( (  "val2a"  != xa.getValue(xt2a) ) == False )
    xa.remove(xt1a)
    xa.remove(xt2a)
    self.assert_( xa.getLength() == 3 )
    xa.remove( "name1", "http://name1.org/")
    self.assert_( xa.getLength() == 2 )
    self.assert_( xa.isEmpty() == False )
    self.assert_( (  "name2" != xa.getName(0) ) == False )
    self.assert_( (  "mval2" != xa.getValue(0) ) == False )
    self.assert_( (  "http://name2.org/" != xa.getURI(0) ) == False )
    self.assert_( (  "p2" != xa.getPrefix(0) ) == False )
    self.assert_( (  "noprefix" != xa.getName(1) ) == False )
    self.assert_( (  "mval3" != xa.getValue(1) ) == False )
    self.assert_( xa.getURI(1) == "" )
    self.assert_( xa.getPrefix(1) == "" )
    self.assert_( xa.hasAttribute( "name1", "http://name1.org/") == False )
    xa.remove(xt2)
    self.assert_( xa.getLength() == 1 )
    self.assert_( xa.isEmpty() == False )
    self.assert_( (  "noprefix" != xa.getName(0) ) == False )
    self.assert_( (  "mval3" != xa.getValue(0) ) == False )
    self.assert_( xa.getURI(0) == "" )
    self.assert_( xa.getPrefix(0) == "" )
    self.assert_( xa.hasAttribute(xt2) == False )
    self.assert_( xa.hasAttribute( "name2", "http://name2.org/") == False )
    xa.remove( "noprefix", "")
    self.assert_( xa.getLength() == 0 )
    self.assert_( xa.isEmpty() == True )
    self.assert_( xa.hasAttribute( "noprefix"    ) == False )
    self.assert_( xa.hasAttribute( "noprefix", "") == False )
    xa = None
    xt1 = None
    xt2 = None
    xt3 = None
    xt1a = None
    xt2a = None
    pass  

  def test_XMLAttributes_clear1(self):
    xa = libsbml.XMLAttributes()
    xt2 = libsbml.XMLTriple("name2", "http://name2.org/", "p2")
    i = xa.add( "name1", "val1", "http://name1.org/", "p1")
    i = xa.add(xt2, "val2")
    i = xa.add( "noprefix", "val3")
    self.assert_( xa.getLength() == 3 )
    self.assert_( xa.isEmpty() == False )
    i = xa.clear()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( xa.getLength() == 0 )
    self.assert_( xa.isEmpty() == True )
    xa = None
    xt2 = None
    pass  

  def test_XMLAttributes_remove1(self):
    xa = libsbml.XMLAttributes()
    xt2 = libsbml.XMLTriple("name2", "http://name2.org/", "p2")
    i = xa.add( "name1", "val1", "http://name1.org/", "p1")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    i = xa.add(xt2, "val2")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    i = xa.add( "noprefix", "val3")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    i = xa.add( "name4", "val4", "http://name4.org/", "p1")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( xa.getLength() == 4 )
    i = xa.remove(4)
    self.assert_( i == libsbml.LIBSBML_INDEX_EXCEEDS_SIZE )
    i = xa.remove(3)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( xa.getLength() == 3 )
    i = xa.remove( "noprefix")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( xa.getLength() == 2 )
    i = xa.remove(xt2)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( xa.getLength() == 1 )
    i = xa.remove( "name1", "http://name1.org/")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( xa.getLength() == 0 )
    xa = None
    xt2 = None
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestXMLAttributesC))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
