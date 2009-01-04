#
# @file    TestParameterRule.rb
# @brief   ParameterRule unit tests
#
# @author  Akiya Jouraku (Ruby conversion)
# @author  Ben Bornstein 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestParameterRule.c
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

class TestParameterRule < Test::Unit::TestCase

  def setup
    @@pr = LibSBML::AssignmentRule.new()
    @@pr.setL1TypeCode(LibSBML::SBML_PARAMETER_RULE)
    if (@@pr == nil)
    end
  end

  def teardown
    @@pr = nil
  end

  def test_ParameterRule_create
    assert( @@pr.getTypeCode() == LibSBML::SBML_ASSIGNMENT_RULE )
    assert( @@pr.getL1TypeCode() == LibSBML::SBML_PARAMETER_RULE )
    assert( @@pr.getNotes() == nil )
    assert( @@pr.getAnnotation() == nil )
    assert( @@pr.getFormula() == "" )
    assert( @@pr.getUnits() == "" )
    assert( @@pr.getVariable() == "" )
    assert( @@pr.getType() == LibSBML::RULE_TYPE_SCALAR )
    assert_equal false, @@pr.isSetVariable()
    assert_equal false, @@pr.isSetUnits()
  end

  def test_ParameterRule_createWith
    pr = LibSBML::RateRule.new("c", "v + 1")
    pr.setL1TypeCode(LibSBML::SBML_PARAMETER_RULE)
    assert( pr.getTypeCode() == LibSBML::SBML_RATE_RULE )
    assert( pr.getL1TypeCode() == LibSBML::SBML_PARAMETER_RULE )
    assert( pr.getNotes() == nil )
    assert( pr.getAnnotation() == nil )
    assert( pr.getUnits() == "" )
    assert ((  "v + 1" == pr.getFormula() ))
    assert ((  "c" == pr.getVariable() ))
    assert( pr.getType() == LibSBML::RULE_TYPE_RATE )
    assert_equal true, pr.isSetVariable()
    assert_equal false, pr.isSetUnits()
    pr = nil
  end

  def test_ParameterRule_free_NULL
  end

  def test_ParameterRule_setName
    name =  "cell";
    @@pr.setVariable(name)
    assert (( name == @@pr.getVariable() ))
    assert_equal true, @@pr.isSetVariable()
    if (@@pr.getVariable() == name)
    end
    c = @@pr.getVariable()
    @@pr.setVariable(c)
    assert (( name == @@pr.getVariable() ))
    @@pr.setVariable("")
    assert_equal false, @@pr.isSetVariable()
    if (@@pr.getVariable() != nil)
    end
  end

  def test_ParameterRule_setUnits
    units =  "cell";
    @@pr.setUnits(units)
    assert (( units == @@pr.getUnits() ))
    assert_equal true, @@pr.isSetUnits()
    if (@@pr.getUnits() == units)
    end
    @@pr.setUnits(@@pr.getUnits())
    assert (( units == @@pr.getUnits() ))
    @@pr.setUnits("")
    assert_equal false, @@pr.isSetUnits()
    if (@@pr.getUnits() != nil)
    end
  end

end
