#
# @file    TestCopyAndClone.py
# @brief   Read SBML unit tests
#
# @author  Akiya Jouraku (Python conversion)
# @author  Ben Bornstein 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestCopyAndClone.cpp
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

class TestCopyAndClone(unittest.TestCase):


  def test_CompartmentType_assignmentOperator(self):
    o1 = libsbml.CompartmentType(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = libsbml.CompartmentType(2,4)
    o2 = o1
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_CompartmentType_clone(self):
    o1 = libsbml.CompartmentType(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = o1.clone()
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_CompartmentType_copyConstructor(self):
    o1 = libsbml.CompartmentType(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = libsbml.CompartmentType(o1)
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Compartment_assignmentOperator(self):
    o1 = libsbml.Compartment(2,4)
    o1.setId("c")
    o1.setOutside("c2")
    self.assert_( o1.getId() ==  "c" )
    self.assert_( o1.getOutside() ==  "c2" )
    o2 = libsbml.Compartment(2,4)
    o2 = o1
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getOutside() ==  "c2" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Compartment_clone(self):
    o1 = libsbml.Compartment(2,4)
    o1.setId("c")
    o1.setOutside("c2")
    self.assert_( o1.getId() ==  "c" )
    self.assert_( o1.getOutside() ==  "c2" )
    o2 = o1.clone()
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getOutside() ==  "c2" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Compartment_copyConstructor(self):
    o1 = libsbml.Compartment(2,4)
    o1.setId("c")
    o1.setOutside("c2")
    self.assert_( o1.getId() ==  "c" )
    self.assert_( o1.getOutside() ==  "c2" )
    o2 = libsbml.Compartment(o1)
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getOutside() ==  "c2" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Constraint_assignmentOperator(self):
    o1 = libsbml.Constraint(2,4)
    o1.setMetaId("c")
    self.assert_( o1.getMetaId() ==  "c" )
    text = libsbml.XMLNode.convertStringToXMLNode(" Some text ")
    triple = libsbml.XMLTriple("p", "http://www.w3.org/1999/xhtml", "")
    att = libsbml.XMLAttributes()
    xmlns = libsbml.XMLNamespaces()
    xmlns.add("http://www.w3.org/1999/xhtml")
    p = libsbml.XMLNode(triple,att,xmlns)
    p.addChild(text)
    triple1 = libsbml.XMLTriple("message", "", "")
    att1 = libsbml.XMLAttributes()
    message = libsbml.XMLNode(triple1,att1)
    message.addChild(p)
    math = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(math)
    o1.setMessage(message)
    math = None
    message = None
    self.assert_( o1.getMath() != None )
    self.assert_( o1.getMessage() != "" )
    o2 = libsbml.Constraint(2,4)
    o2 = o1
    self.assert_( o2.getMetaId() ==  "c" )
    self.assert_( o1.getMath() != None )
    self.assert_( o1.getMessage() != "" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Constraint_clone(self):
    o1 = libsbml.Constraint(2,4)
    o1.setMetaId("c")
    self.assert_( o1.getMetaId() ==  "c" )
    text = libsbml.XMLNode.convertStringToXMLNode(" Some text ")
    triple = libsbml.XMLTriple("p", "http://www.w3.org/1999/xhtml", "")
    att = libsbml.XMLAttributes()
    xmlns = libsbml.XMLNamespaces()
    xmlns.add("http://www.w3.org/1999/xhtml")
    p = libsbml.XMLNode(triple,att,xmlns)
    p.addChild(text)
    triple1 = libsbml.XMLTriple("message", "", "")
    att1 = libsbml.XMLAttributes()
    message = libsbml.XMLNode(triple1,att1)
    message.addChild(p)
    math = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(math)
    o1.setMessage(message)
    math = None
    message = None
    self.assert_( o1.getMath() != None )
    self.assert_( o1.getMessage() != "" )
    o2 = o1.clone()
    self.assert_( o2.getMetaId() ==  "c" )
    self.assert_( o1.getMath() != None )
    self.assert_( o1.getMessage() != "" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Constraint_copyConstructor(self):
    o1 = libsbml.Constraint(2,4)
    o1.setMetaId("c")
    self.assert_( o1.getMetaId() ==  "c" )
    text = libsbml.XMLNode.convertStringToXMLNode(" Some text ")
    triple = libsbml.XMLTriple("p", "http://www.w3.org/1999/xhtml", "")
    att = libsbml.XMLAttributes()
    xmlns = libsbml.XMLNamespaces()
    xmlns.add("http://www.w3.org/1999/xhtml")
    p = libsbml.XMLNode(triple,att,xmlns)
    p.addChild(text)
    triple1 = libsbml.XMLTriple("message", "", "")
    att1 = libsbml.XMLAttributes()
    message = libsbml.XMLNode(triple1,att1)
    message.addChild(p)
    math = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(math)
    o1.setMessage(message)
    math = None
    message = None
    self.assert_( o1.getMath() != None )
    self.assert_( o1.getMessage() != "" )
    o2 = libsbml.Constraint(o1)
    self.assert_( o2.getMetaId() ==  "c" )
    self.assert_( o1.getMath() != None )
    self.assert_( o1.getMessage() != "" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Delay_assignmentOperator(self):
    o1 = libsbml.Delay(2,4)
    node = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(node)
    node = None
    self.assert_( o1.getMath() != None )
    o2 = libsbml.Delay(2,4)
    o2 = o1
    self.assert_( o1.getMath() != None )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Delay_clone(self):
    o1 = libsbml.Delay(2,4)
    node = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(node)
    node = None
    self.assert_( o1.getMath() != None )
    o2 = o1.clone()
    self.assert_( o1.getMath() != None )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Delay_copyConstructor(self):
    o1 = libsbml.Delay(2,4)
    node = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(node)
    node = None
    self.assert_( o1.getMath() != None )
    o2 = libsbml.Delay(o1)
    self.assert_( o2.getMath() != None )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_EventAssignment_assignmentOperator(self):
    o1 = libsbml.EventAssignment(2,4)
    o1.setVariable("c2")
    self.assert_( o1.getVariable() ==  "c2" )
    node = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(node)
    node = None
    self.assert_( o1.getMath() != None )
    o2 = libsbml.EventAssignment(2,4)
    o2 = o1
    self.assert_( o2.getVariable() ==  "c2" )
    self.assert_( o2.getMath() != None )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_EventAssignment_clone(self):
    o1 = libsbml.EventAssignment(2,4)
    o1.setVariable("c2")
    self.assert_( o1.getVariable() ==  "c2" )
    node = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(node)
    node = None
    self.assert_( o1.getMath() != None )
    o2 = o1.clone()
    self.assert_( o2.getVariable() ==  "c2" )
    self.assert_( o2.getMath() != None )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_EventAssignment_copyConstructor(self):
    o1 = libsbml.EventAssignment(2,4)
    o1.setVariable("c2")
    self.assert_( o1.getVariable() ==  "c2" )
    node = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(node)
    node = None
    self.assert_( o1.getMath() != None )
    o2 = libsbml.EventAssignment(o1)
    self.assert_( o2.getVariable() ==  "c2" )
    self.assert_( o2.getMath() != None )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Event_assignmentOperator(self):
    o1 = libsbml.Event(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = libsbml.Event(2,4)
    o2 = o1
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Event_clone(self):
    o1 = libsbml.Event(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = o1.clone()
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Event_copyConstructor(self):
    o1 = libsbml.Event(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = libsbml.Event(o1)
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_FunctionDefinition_assignmentOperator(self):
    o1 = libsbml.FunctionDefinition(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    node = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(node)
    node = None
    self.assert_( o1.getMath() != None )
    o2 = libsbml.FunctionDefinition(2,4)
    o2 = o1
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getMath() != None )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_FunctionDefinition_clone(self):
    o1 = libsbml.FunctionDefinition(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    node = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(node)
    node = None
    self.assert_( o1.getMath() != None )
    o2 = o1.clone()
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getMath() != None )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_FunctionDefinition_copyConstructor(self):
    o1 = libsbml.FunctionDefinition(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    node = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(node)
    node = None
    self.assert_( o1.getMath() != None )
    o2 = libsbml.FunctionDefinition(o1)
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getMath() != None )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_InitialAssignment_assignmentOperator(self):
    o1 = libsbml.InitialAssignment(2,4)
    o1.setSymbol("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = libsbml.InitialAssignment(2,4)
    o2 = o1
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_InitialAssignment_clone(self):
    o1 = libsbml.InitialAssignment(2,4)
    o1.setSymbol("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = o1.clone()
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_InitialAssignment_copyConstructor(self):
    o1 = libsbml.InitialAssignment(2,4)
    o1.setSymbol("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = libsbml.InitialAssignment(o1)
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_KineticLaw_assignmentOperator(self):
    o1 = libsbml.KineticLaw(2,4)
    p = libsbml.Parameter(2,4)
    p.setId("jake")
    o1.addParameter(p)
    p = None
    self.assert_( o1.getNumParameters() == 1 )
    self.assert_( o1.getParameter(0).getId() ==  "jake" )
    o2 = libsbml.KineticLaw(2,4)
    o2 = o1
    self.assert_( o2.getNumParameters() == 1 )
    self.assert_( o2.getParameter(0).getId() ==  "jake" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_KineticLaw_clone(self):
    o1 = libsbml.KineticLaw(2,4)
    p = libsbml.Parameter(2,4)
    p.setId("jake")
    o1.addParameter(p)
    p = None
    self.assert_( o1.getNumParameters() == 1 )
    self.assert_( o1.getParameter(0).getId() ==  "jake" )
    o2 = o1.clone()
    self.assert_( o2.getNumParameters() == 1 )
    self.assert_( o2.getParameter(0).getId() ==  "jake" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_KineticLaw_copyConstructor(self):
    o1 = libsbml.KineticLaw(2,4)
    p = libsbml.Parameter(2,4)
    p.setId("jake")
    o1.addParameter(p)
    p = None
    self.assert_( o1.getNumParameters() == 1 )
    self.assert_( o1.getParameter(0).getId() ==  "jake" )
    o2 = libsbml.KineticLaw(o1)
    self.assert_( o2.getNumParameters() == 1 )
    self.assert_( o2.getParameter(0).getId() ==  "jake" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_ListOf_assignmentOperator(self):
    o1 = libsbml.ListOf()
    s = libsbml.Species(2,1)
    s.setId("species_1")
    o1.append(s)
    s = None
    o2 = libsbml.ListOf()
    o2 = o1
    self.assert_( o2.size() == 1 )
    self.assert_( o2.get(0).getId() ==  "species_1" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_ListOf_clone(self):
    o1 = libsbml.ListOf()
    s = libsbml.Species(2,1)
    s.setId("species_1")
    o1.append(s)
    s = None
    o2 = o1.clone()
    self.assert_( o2.size() == 1 )
    self.assert_( o2.get(0).getId() ==  "species_1" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_ListOf_copyConstructor(self):
    o1 = libsbml.ListOf()
    s = libsbml.Species(2,1)
    s.setId("species_1")
    o1.append(s)
    s = None
    o2 = libsbml.ListOf(o1)
    self.assert_( o2.size() == 1 )
    self.assert_( o2.get(0).getId() ==  "species_1" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Model_assignmentOperator(self):
    o1 = libsbml.Model(2,4)
    o1.setId("c")
    p = libsbml.Parameter(2,4)
    p.setId("alex")
    o1.addParameter(p)
    p = None
    fud = None
    self.assert_( o1.getId() ==  "c" )
    self.assert_( o1.getNumParameters() == 1 )
    self.assert_( o1.getParameter(0).getId() ==  "alex" )
    o2 = libsbml.Model(2,4)
    o2 = o1
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getNumParameters() == 1 )
    self.assert_( o2.getParameter(0).getId() ==  "alex" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Model_clone(self):
    o1 = libsbml.Model(2,4)
    o1.setId("c")
    p = libsbml.Parameter(2,4)
    p.setId("alex")
    o1.addParameter(p)
    p = None
    fud = None
    self.assert_( o1.getId() ==  "c" )
    self.assert_( o1.getNumParameters() == 1 )
    self.assert_( o1.getParameter(0).getId() ==  "alex" )
    o2 = o1.clone()
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getNumParameters() == 1 )
    self.assert_( o2.getParameter(0).getId() ==  "alex" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Model_copyConstructor(self):
    o1 = libsbml.Model(2,4)
    o1.setId("c")
    p = libsbml.Parameter(2,4)
    p.setId("alex")
    o1.addParameter(p)
    p = None
    fud = None
    self.assert_( o1.getId() ==  "c" )
    self.assert_( o1.getNumParameters() == 1 )
    self.assert_( o1.getParameter(0).getId() ==  "alex" )
    o2 = libsbml.Model(o1)
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getNumParameters() == 1 )
    self.assert_( o2.getParameter(0).getId() ==  "alex" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Parameter_assignmentOperator(self):
    o1 = libsbml.Parameter(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = libsbml.Parameter(2,4)
    o2 = o1
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Parameter_clone(self):
    o1 = libsbml.Parameter(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = o1.clone()
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Parameter_copyConstructor(self):
    o1 = libsbml.Parameter(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = libsbml.Parameter(o1)
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Reaction_assignmentOperator(self):
    o1 = libsbml.Reaction(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    kl = libsbml.KineticLaw(2,4)
    o1.setKineticLaw(kl)
    kl = None
    self.assert_( o1.isSetKineticLaw() == True )
    self.assert_( o1.getKineticLaw() != None )
    o2 = libsbml.Reaction(2,4)
    o2 = o1
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.isSetKineticLaw() == True )
    self.assert_( o2.getKineticLaw() != None )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Reaction_clone(self):
    o1 = libsbml.Reaction(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    kl = libsbml.KineticLaw(2,4)
    o1.setKineticLaw(kl)
    kl = None
    self.assert_( o1.isSetKineticLaw() == True )
    self.assert_( o1.getKineticLaw() != None )
    o2 = o1.clone()
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.isSetKineticLaw() == True )
    self.assert_( o2.getKineticLaw() != None )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Reaction_copyConstructor(self):
    o1 = libsbml.Reaction(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    kl = libsbml.KineticLaw(2,4)
    o1.setKineticLaw(kl)
    kl = None
    self.assert_( o1.isSetKineticLaw() == True )
    self.assert_( o1.getKineticLaw() != None )
    o2 = libsbml.Reaction(o1)
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.isSetKineticLaw() == True )
    self.assert_( o2.getKineticLaw() != None )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Rule_assignmentOperator(self):
    o1 = libsbml.RateRule(2,4)
    o1.setVariable("a")
    self.assert_( o1.getVariable() ==  "a" )
    node = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(node)
    node = None
    self.assert_( o1.isSetMath() == True )
    o2 = libsbml.RateRule(2,4)
    o2 = o1
    self.assert_( o2.getVariable() ==  "a" )
    self.assert_( o2.isSetMath() == True )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Rule_clone(self):
    o1 = libsbml.RateRule(2,1)
    o1.setVariable("a")
    self.assert_( o1.getVariable() ==  "a" )
    node = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(node)
    node = None
    self.assert_( o1.isSetMath() == True )
    o2 = o1.clone()
    self.assert_( o2.getVariable() ==  "a" )
    self.assert_( o2.isSetMath() == True )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Rule_copyConstructor(self):
    o1 = libsbml.RateRule(2,1)
    o1.setVariable("a")
    self.assert_( o1.getVariable() ==  "a" )
    node = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(node)
    node = None
    self.assert_( o1.isSetMath() == True )
    o2 = libsbml.Rule(o1)
    self.assert_( o2.getVariable() ==  "a" )
    self.assert_( o2.isSetMath() == True )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_SBMLDocument_assignmentOperator(self):
    o1 = libsbml.SBMLDocument()
    o1.setLevelAndVersion(2,1)
    self.assert_( o1.getLevel() == 2 )
    self.assert_( o1.getVersion() == 1 )
    o2 = libsbml.SBMLDocument()
    o2 = o1
    self.assert_( o2.getLevel() == 2 )
    self.assert_( o2.getVersion() == 1 )
    o2 = None
    o1 = None
    pass  

  def test_SBMLDocument_clone(self):
    o1 = libsbml.SBMLDocument()
    o1.setLevelAndVersion(1,1)
    m = libsbml.Model(1,1)
    m.setId("foo")
    o1.setModel(m)
    self.assert_( o1.getLevel() == 1 )
    self.assert_( o1.getVersion() == 1 )
    self.assert_( o1.getModel().getId() ==  "foo" )
    self.assert_( o1.getModel().getLevel() == 1 )
    self.assert_( o1.getModel().getVersion() == 1 )
    self.assert_( o1.getModel().getSBMLDocument() == o1 )
    o2 = o1.clone()
    self.assert_( o2.getLevel() == 1 )
    self.assert_( o2.getVersion() == 1 )
    self.assert_( o2.getModel().getId() ==  "foo" )
    self.assert_( o2.getModel().getLevel() == 1 )
    self.assert_( o2.getModel().getVersion() == 1 )
    self.assert_( o2.getModel().getSBMLDocument() == o2 )
    o2 = None
    o1 = None
    pass  

  def test_SBMLDocument_copyConstructor(self):
    o1 = libsbml.SBMLDocument()
    o1.setLevelAndVersion(2,1)
    self.assert_( o1.getLevel() == 2 )
    self.assert_( o1.getVersion() == 1 )
    o2 = libsbml.SBMLDocument(o1)
    self.assert_( o2.getLevel() == 2 )
    self.assert_( o2.getVersion() == 1 )
    o2 = None
    o1 = None
    pass  

  def test_SpeciesReference_assignmentOperator(self):
    o1 = libsbml.SpeciesReference(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = libsbml.SpeciesReference(2,4)
    o2 = o1
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_SpeciesReference_clone(self):
    o1 = libsbml.SpeciesReference(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = o1.clone()
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_SpeciesReference_copyConstructor(self):
    o1 = libsbml.SpeciesReference(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = libsbml.SpeciesReference(o1)
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_SpeciesType_assignmentOperator(self):
    o1 = libsbml.SpeciesType(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = libsbml.SpeciesType(2,4)
    o2 = o1
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_SpeciesType_clone(self):
    o1 = libsbml.SpeciesType(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = o1.clone()
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_SpeciesType_copyConstructor(self):
    o1 = libsbml.SpeciesType(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = libsbml.SpeciesType(o1)
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Species_assignmentOperator(self):
    o1 = libsbml.Species(2,4)
    o1.setId("c")
    o1.setSpeciesType("c1")
    self.assert_( o1.getId() ==  "c" )
    self.assert_( o1.getSpeciesType() ==  "c1" )
    o2 = libsbml.Species(2,4)
    o2 = o1
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getSpeciesType() ==  "c1" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Species_clone(self):
    o1 = libsbml.Species(2,4)
    o1.setId("c")
    o1.setSpeciesType("c1")
    self.assert_( o1.getId() ==  "c" )
    self.assert_( o1.getSpeciesType() ==  "c1" )
    o2 = o1.clone()
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getSpeciesType() ==  "c1" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Species_copyConstructor(self):
    o1 = libsbml.Species(2,4)
    o1.setId("c")
    o1.setSpeciesType("c1")
    self.assert_( o1.getId() ==  "c" )
    self.assert_( o1.getSpeciesType() ==  "c1" )
    o2 = libsbml.Species(o1)
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getSpeciesType() ==  "c1" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Trigger_assignmentOperator(self):
    o1 = libsbml.Trigger(2,4)
    node = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(node)
    node = None
    self.assert_( o1.getMath() != None )
    o2 = libsbml.Trigger(2,4)
    o2 = o1
    self.assert_( o1.getMath() != None )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Trigger_clone(self):
    o1 = libsbml.Trigger(2,4)
    node = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(node)
    node = None
    self.assert_( o1.getMath() != None )
    o2 = o1.clone()
    self.assert_( o1.getMath() != None )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Trigger_copyConstructor(self):
    o1 = libsbml.Trigger(2,4)
    node = libsbml.ASTNode(libsbml.AST_CONSTANT_PI)
    o1.setMath(node)
    node = None
    self.assert_( o1.getMath() != None )
    o2 = libsbml.Trigger(o1)
    self.assert_( o2.getMath() != None )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_UnitDefinition_assignmentOperator(self):
    o1 = libsbml.UnitDefinition(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = libsbml.UnitDefinition(2,4)
    o2 = o1
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_UnitDefinition_clone(self):
    o1 = libsbml.UnitDefinition(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = o1.clone()
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_UnitDefinition_copyConstructor(self):
    o1 = libsbml.UnitDefinition(2,4)
    o1.setId("c")
    self.assert_( o1.getId() ==  "c" )
    o2 = libsbml.UnitDefinition(o1)
    self.assert_( o2.getId() ==  "c" )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Unit_assignmentOperator(self):
    o1 = libsbml.Unit(2,4)
    o1.setKind(libsbml.UNIT_KIND_MOLE)
    self.assert_( o1.getKind() == libsbml.UNIT_KIND_MOLE )
    o2 = libsbml.Unit(2,4)
    o2 = o1
    self.assert_( o2.getKind() == libsbml.UNIT_KIND_MOLE )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Unit_clone(self):
    o1 = libsbml.Unit(2,4)
    o1.setKind(libsbml.UNIT_KIND_MOLE)
    self.assert_( o1.getKind() == libsbml.UNIT_KIND_MOLE )
    o2 = o1.clone()
    self.assert_( o2.getKind() == libsbml.UNIT_KIND_MOLE )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

  def test_Unit_copyConstructor(self):
    o1 = libsbml.Unit(2,4)
    o1.setKind(libsbml.UNIT_KIND_MOLE)
    self.assert_( o1.getKind() == libsbml.UNIT_KIND_MOLE )
    o2 = libsbml.Unit(o1)
    self.assert_( o2.getKind() == libsbml.UNIT_KIND_MOLE )
    self.assert_( o2.getParentSBMLObject() == o1.getParentSBMLObject() )
    o2 = None
    o1 = None
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestCopyAndClone))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
