#
# @file    TestCompartment.rb
# @brief   Compartment unit tests
#
# @author  Akiya Jouraku (Ruby conversion)
# @author  Ben Bornstein 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestCompartment.c
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

class TestCompartment < Test::Unit::TestCase

  def setup
    @@c = LibSBML::Compartment.new()
    if (@@c == nil)
    end
  end

  def teardown
    @@c = nil
  end

  def test_Compartment_create
    assert( @@c.getTypeCode() == LibSBML::SBML_COMPARTMENT )
    assert( @@c.getMetaId() == "" )
    assert( @@c.getNotes() == nil )
    assert( @@c.getAnnotation() == nil )
    assert( @@c.getId() == "" )
    assert( @@c.getName() == "" )
    assert( @@c.getUnits() == "" )
    assert( @@c.getOutside() == "" )
    assert( @@c.getSpatialDimensions() == 3 )
    assert( @@c.getVolume() == 1.0 )
    assert( @@c.getConstant() == true )
    assert_equal false, @@c.isSetId()
    assert_equal false, @@c.isSetName()
    assert_equal false, @@c.isSetSize()
    assert_equal false, @@c.isSetVolume()
    assert_equal false, @@c.isSetUnits()
    assert_equal false, @@c.isSetOutside()
  end

  def test_Compartment_createWith
    c = LibSBML::Compartment.new("A", "")
    assert( c.getTypeCode() == LibSBML::SBML_COMPARTMENT )
    assert( c.getMetaId() == "" )
    assert( c.getNotes() == nil )
    assert( c.getAnnotation() == nil )
    assert( c.getName() == "" )
    assert( c.getSpatialDimensions() == 3 )
    assert ((  "A"      == c.getId() ))
    assert( c.getConstant() == true )
    assert_equal true, c.isSetId()
    assert_equal false, c.isSetName()
    c = nil
  end

  def test_Compartment_createWithLevelVersionAndNamespace
    xmlns = LibSBML::XMLNamespaces.new()
    xmlns.add( "http://www.sbml.org", "sbml")
    c = LibSBML::Compartment.new(2,1,xmlns)
    assert( c.getTypeCode() == LibSBML::SBML_COMPARTMENT )
    assert( c.getMetaId() == "" )
    assert( c.getNotes() == nil )
    assert( c.getAnnotation() == nil )
    assert( c.getLevel() == 2 )
    assert( c.getVersion() == 1 )
    assert( c.getNamespaces() != "" )
    assert( c.getNamespaces().getLength() == 1 )
    assert( c.getName() == "" )
    assert( c.getSpatialDimensions() == 3 )
    assert( c.getConstant() == true )
    c = nil
  end

  def test_Compartment_free_NULL
  end

  def test_Compartment_getSpatialDimensions
    @@c.setSpatialDimensions(1)
    assert( @@c.getSpatialDimensions() == 1 )
  end

  def test_Compartment_getsetConstant
    @@c.setConstant(true)
    assert( @@c.getConstant() == true )
  end

  def test_Compartment_getsetType
    @@c.setCompartmentType( "cell")
    assert ((  "cell"  == @@c.getCompartmentType() ))
    assert_equal true, @@c.isSetCompartmentType()
    @@c.unsetCompartmentType()
    assert_equal false, @@c.isSetCompartmentType()
  end

  def test_Compartment_initDefaults
    c = LibSBML::Compartment.new("A", "")
    c.initDefaults()
    assert ((  "A" == c.getId() ))
    assert( c.getName() == "" )
    assert( c.getUnits() == "" )
    assert( c.getOutside() == "" )
    assert( c.getSpatialDimensions() == 3 )
    assert( c.getVolume() == 1.0 )
    assert( c.getConstant() == true )
    assert_equal true, c.isSetId()
    assert_equal false, c.isSetName()
    assert_equal false, c.isSetSize()
    assert_equal false, c.isSetVolume()
    assert_equal false, c.isSetUnits()
    assert_equal false, c.isSetOutside()
    c = nil
  end

  def test_Compartment_setId
    id =  "mitochondria";
    @@c.setId(id)
    assert (( id == @@c.getId() ))
    assert_equal true, @@c.isSetId()
    if (@@c.getId() == id)
    end
    @@c.setId(@@c.getId())
    assert (( id == @@c.getId() ))
    @@c.setId("")
    assert_equal false, @@c.isSetId()
    if (@@c.getId() != nil)
    end
  end

  def test_Compartment_setName
    name =  "My Favorite Factory";
    @@c.setName(name)
    assert (( name == @@c.getName() ))
    assert_equal true, @@c.isSetName()
    if (@@c.getName() == name)
    end
    @@c.setName(@@c.getName())
    assert (( name == @@c.getName() ))
    @@c.setName("")
    assert_equal false, @@c.isSetName()
    if (@@c.getName() != nil)
    end
  end

  def test_Compartment_setOutside
    outside =  "cell";
    @@c.setOutside(outside)
    assert (( outside == @@c.getOutside() ))
    assert_equal true, @@c.isSetOutside()
    if (@@c.getOutside() == outside)
    end
    @@c.setOutside(@@c.getOutside())
    assert (( outside == @@c.getOutside() ))
    @@c.setOutside("")
    assert_equal false, @@c.isSetOutside()
    if (@@c.getOutside() != nil)
    end
  end

  def test_Compartment_setUnits
    units =  "volume";
    @@c.setUnits(units)
    assert (( units == @@c.getUnits() ))
    assert_equal true, @@c.isSetUnits()
    if (@@c.getUnits() == units)
    end
    @@c.setUnits(@@c.getUnits())
    assert (( units == @@c.getUnits() ))
    @@c.setUnits("")
    assert_equal false, @@c.isSetUnits()
    if (@@c.getUnits() != nil)
    end
  end

  def test_Compartment_unsetSize
    @@c.setSize(0.2)
    assert( @@c.getSize() == 0.2 )
    assert_equal true, @@c.isSetSize()
    @@c.unsetSize()
    assert_equal false, @@c.isSetSize()
  end

  def test_Compartment_unsetVolume
    @@c.setVolume(1.0)
    assert( @@c.getVolume() == 1.0 )
    assert_equal true, @@c.isSetVolume()
    @@c.unsetVolume()
    assert_equal false, @@c.isSetVolume()
  end

end
