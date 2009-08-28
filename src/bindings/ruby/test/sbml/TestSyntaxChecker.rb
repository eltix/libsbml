#
# @file    TestSyntaxChecker.rb
# @brief   SyntaxChecker unit tests
#
# @author  Akiya Jouraku (Ruby conversion)
# @author  Sarah Keating 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestSyntaxChecker.c
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

class TestSyntaxChecker < Test::Unit::TestCase

  def test_SyntaxChecker_validID
    assert( LibSBML::SyntaxChecker.isValidXMLID("cell") == true )
    assert( LibSBML::SyntaxChecker.isValidXMLID("1cell") == false )
    assert( LibSBML::SyntaxChecker.isValidXMLID("_cell") == true )
  end

  def test_SyntaxChecker_validId
    assert( LibSBML::SyntaxChecker.isValidSBMLSId("cell") == true )
    assert( LibSBML::SyntaxChecker.isValidSBMLSId("1cell") == false )
  end

  def test_SyntaxChecker_validUnitId
    assert( LibSBML::SyntaxChecker.isValidUnitSId("cell") == true )
    assert( LibSBML::SyntaxChecker.isValidUnitSId("1cell") == false )
  end

  def test_SyntaxChecker_validXHTML
    triple = LibSBML::XMLTriple.new("p", "", "")
    att = LibSBML::XMLAttributes.new()
    ns = LibSBML::XMLNamespaces.new()
    ns.add( "http://www.w3.org/1999/xhtml", "")
    tt = LibSBML::XMLToken.new("This is my text")
    n1 = LibSBML::XMLNode.new(tt)
    token = LibSBML::XMLToken.new(triple,att,ns)
    node = LibSBML::XMLNode.new(token)
    node.addChild(n1)
    assert( LibSBML::SyntaxChecker.hasExpectedXHTMLSyntax(node,nil) == false )
    triple = LibSBML::XMLTriple.new("html", "", "")
    ns.clear()
    token = LibSBML::XMLToken.new(triple,att,ns)
    node = LibSBML::XMLNode.new(token)
    node.addChild(n1)
    assert( LibSBML::SyntaxChecker.hasExpectedXHTMLSyntax(node,nil) == false )
  end

end
