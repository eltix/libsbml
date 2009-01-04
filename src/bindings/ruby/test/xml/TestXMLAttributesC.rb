#
# @file    TestXMLAttributesC.rb
# @brief   XMLAttributes unit tests, C version
#
# @author  Akiya Jouraku (Ruby conversion)
# @author  Sarah Keating 
#
# $Id:$
# $HeadURL:$
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
require 'test/unit'
require 'libSBML'

class TestXMLAttributesC < Test::Unit::TestCase

  def test_XMLAttributes_add_remove_qname_C
    xa = LibSBML::XMLAttributes.new()
    xt1 = LibSBML::XMLTriple.new("name1", "http://name1.org/", "p1")
    xt2 = LibSBML::XMLTriple.new("name2", "http://name2.org/", "p2")
    xt3 = LibSBML::XMLTriple.new("name3", "http://name3.org/", "p3")
    xt1a = LibSBML::XMLTriple.new("name1", "http://name1a.org/", "p1a")
    xt2a = LibSBML::XMLTriple.new("name2", "http://name2a.org/", "p2a")
    xa.add( "name1", "val1", "http://name1.org/", "p1")
    xa.add(xt2, "val2")
    assert( xa.getLength() == 2 )
    assert( xa.isEmpty() == false )
    assert( (  "name1" != xa.getName(0) ) == false )
    assert( (  "val1"  != xa.getValue(0) ) == false )
    assert( (  "http://name1.org/" != xa.getURI(0) ) == false )
    assert( (  "p1"    != xa.getPrefix(0) ) == false )
    assert( (  "name2" != xa.getName(1) ) == false )
    assert( (  "val2"  != xa.getValue(1) ) == false )
    assert( (  "http://name2.org/" != xa.getURI(1) ) == false )
    assert( (  "p2"    != xa.getPrefix(1) ) == false )
    assert( (  "val1"  != xa.getValue( "name1") ) == false )
    assert( (  "val2"  != xa.getValue( "name2") ) == false )
    assert( (  "val1"  != xa.getValue( "name1", "http://name1.org/") ) == false )
    assert( (  "val2"  != xa.getValue( "name2", "http://name2.org/") ) == false )
    assert( (  "val1"  != xa.getValue(xt1) ) == false )
    assert( (  "val2"  != xa.getValue(xt2) ) == false )
    assert( xa.hasAttribute(-1) == false )
    assert( xa.hasAttribute(2) == false )
    assert( xa.hasAttribute(0) == true )
    assert( xa.hasAttribute( "name1", "http://name1.org/") == true )
    assert( xa.hasAttribute( "name2", "http://name2.org/") == true )
    assert( xa.hasAttribute( "name3", "http://name3.org/") == false )
    assert( xa.hasAttribute(xt1) == true )
    assert( xa.hasAttribute(xt2) == true )
    assert( xa.hasAttribute(xt3) == false )
    xa.add( "noprefix", "val3")
    assert( xa.getLength() == 3 )
    assert( xa.isEmpty() == false )
    assert( (  "noprefix" != xa.getName(2) ) == false )
    assert( (  "val3"     != xa.getValue(2) ) == false )
    assert( xa.getURI(2) == "" )
    assert( xa.getPrefix(2) == "" )
    assert( (  "val3"  != xa.getValue( "noprefix", "") ) == false )
    assert( xa.hasAttribute( "noprefix"    ) == true )
    assert( xa.hasAttribute( "noprefix", "") == true )
    xa.add(xt1, "mval1")
    xa.add( "name2", "mval2", "http://name2.org/", "p2")
    xa.add( "noprefix", "mval3")
    assert( xa.getLength() == 3 )
    assert( xa.isEmpty() == false )
    assert( (  "name1" != xa.getName(0) ) == false )
    assert( (  "mval1" != xa.getValue(0) ) == false )
    assert( (  "http://name1.org/" != xa.getURI(0) ) == false )
    assert( (  "p1"    != xa.getPrefix(0) ) == false )
    assert( (  "name2"    != xa.getName(1) ) == false )
    assert( (  "mval2"    != xa.getValue(1) ) == false )
    assert( (  "http://name2.org/" != xa.getURI(1) ) == false )
    assert( (  "p2"       != xa.getPrefix(1) ) == false )
    assert( (  "noprefix" != xa.getName(2) ) == false )
    assert( (  "mval3"    != xa.getValue(2) ) == false )
    assert( xa.getURI(2) == "" )
    assert( xa.getPrefix(2) == "" )
    assert( xa.hasAttribute(xt1) == true )
    assert( xa.hasAttribute( "name1", "http://name1.org/") == true )
    assert( xa.hasAttribute( "noprefix") == true )
    xa.add(xt1a, "val1a")
    xa.add(xt2a, "val2a")
    assert( xa.getLength() == 5 )
    assert( (  "name1" != xa.getName(3) ) == false )
    assert( (  "val1a" != xa.getValue(3) ) == false )
    assert( (  "http://name1a.org/" != xa.getURI(3) ) == false )
    assert( (  "p1a" != xa.getPrefix(3) ) == false )
    assert( (  "name2" != xa.getName(4) ) == false )
    assert( (  "val2a" != xa.getValue(4) ) == false )
    assert( (  "http://name2a.org/" != xa.getURI(4) ) == false )
    assert( (  "p2a" != xa.getPrefix(4) ) == false )
    assert( (  "mval1"  != xa.getValue( "name1") ) == false )
    assert( (  "mval2"  != xa.getValue( "name2") ) == false )
    assert( (  "val1a"  != xa.getValue( "name1", "http://name1a.org/") ) == false )
    assert( (  "val2a"  != xa.getValue( "name2", "http://name2a.org/") ) == false )
    assert( (  "val1a"  != xa.getValue(xt1a) ) == false )
    assert( (  "val2a"  != xa.getValue(xt2a) ) == false )
    xa.remove(xt1a)
    xa.remove(xt2a)
    assert( xa.getLength() == 3 )
    xa.remove( "name1", "http://name1.org/")
    assert( xa.getLength() == 2 )
    assert( xa.isEmpty() == false )
    assert( (  "name2" != xa.getName(0) ) == false )
    assert( (  "mval2" != xa.getValue(0) ) == false )
    assert( (  "http://name2.org/" != xa.getURI(0) ) == false )
    assert( (  "p2" != xa.getPrefix(0) ) == false )
    assert( (  "noprefix" != xa.getName(1) ) == false )
    assert( (  "mval3" != xa.getValue(1) ) == false )
    assert( xa.getURI(1) == "" )
    assert( xa.getPrefix(1) == "" )
    assert( xa.hasAttribute( "name1", "http://name1.org/") == false )
    xa.remove(xt2)
    assert( xa.getLength() == 1 )
    assert( xa.isEmpty() == false )
    assert( (  "noprefix" != xa.getName(0) ) == false )
    assert( (  "mval3" != xa.getValue(0) ) == false )
    assert( xa.getURI(0) == "" )
    assert( xa.getPrefix(0) == "" )
    assert( xa.hasAttribute(xt2) == false )
    assert( xa.hasAttribute( "name2", "http://name2.org/") == false )
    xa.remove( "noprefix", "")
    assert( xa.getLength() == 0 )
    assert( xa.isEmpty() == true )
    assert( xa.hasAttribute( "noprefix"    ) == false )
    assert( xa.hasAttribute( "noprefix", "") == false )
    xa = nil
    xt1 = nil
    xt2 = nil
    xt3 = nil
    xt1a = nil
    xt2a = nil
  end

end
