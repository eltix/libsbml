/// 
///  @file    TestAssignmentRule.cs
///  @brief   AssignmentRule unit tests
///  @author  Frank Bergmann (Csharp conversion)
///  @author  Akiya Jouraku (Csharp conversion)
///  @author  Ben Bornstein 
/// 
///  $Id$
///  $HeadURL$
/// 
///  This test file was converted from src/sbml/test/TestAssignmentRule.c
///  with the help of conversion sciprt (ctest_converter.pl).
/// 
/// <!---------------------------------------------------------------------------
///  This file is part of libSBML.  Please visit http://sbml.org for more
///  information about SBML, and the latest version of libSBML.
/// 
///  Copyright 2005-2009 California Institute of Technology.
///  Copyright 2002-2005 California Institute of Technology and
///                      Japan Science and Technology Corporation.
///  
///  This library is free software; you can redistribute it and/or modify it
///  under the terms of the GNU Lesser General Public License as published by
///  the Free Software Foundation.  A copy of the license agreement is provided
///  in the file named "LICENSE.txt" included with this software distribution
///  and also available online as http://sbml.org/software/libsbml/license.html
/// --------------------------------------------------------------------------->*/


namespace LibSBMLCSTest {

  using libsbml;

  using  System.IO;

  public class TestAssignmentRule {
    public class AssertionError : System.Exception 
    {
      public AssertionError() : base()
      {
        
      }
    }


    static void assertTrue(bool condition)
    {
      if (condition == true)
      {
        return;
      }
      throw new AssertionError();
    }

    static void assertEquals(object a, object b)
    {
      if ( (a == null) && (b == null) )
      {
        return;
      }
      else if ( (a == null) || (b == null) )
      {
        throw new AssertionError();
      }
      else if (a.Equals(b))
      {
        return;
      }
  
      throw new AssertionError();
    }

    static void assertNotEquals(object a, object b)
    {
      if ( (a == null) && (b == null) )
      {
        throw new AssertionError();
      }
      else if ( (a == null) || (b == null) )
      {
        return;
      }
      else if (a.Equals(b))
      {
        throw new AssertionError();
      }
    }

    static void assertEquals(bool a, bool b)
    {
      if ( a == b )
      {
        return;
      }
      throw new AssertionError();
    }

    static void assertNotEquals(bool a, bool b)
    {
      if ( a != b )
      {
        return;
      }
      throw new AssertionError();
    }

    static void assertEquals(int a, int b)
    {
      if ( a == b )
      {
        return;
      }
      throw new AssertionError();
    }

    static void assertNotEquals(int a, int b)
    {
      if ( a != b )
      {
        return;
      }
      throw new AssertionError();
    }

    private Rule AR;

    public void setUp()
    {
      AR = new  AssignmentRule(2,4);
      if (AR == null);
      {
      }
    }

    public void tearDown()
    {
      AR = null;
    }

    public void test_AssignmentRule_L2_create()
    {
      assertTrue( AR.getTypeCode() == libsbml.SBML_ASSIGNMENT_RULE );
      assertTrue( AR.getMetaId() == "" );
      assertTrue( AR.getNotes() == null );
      assertTrue( AR.getAnnotation() == null );
      assertTrue( AR.getFormula() == "" );
      assertTrue( AR.getMath() == null );
      assertTrue( AR.getVariable() == "" );
      assertTrue( AR.getType() == libsbml.RULE_TYPE_SCALAR );
    }

    public void test_AssignmentRule_createWithFormula()
    {
      ASTNode math;
      string formula;
      Rule ar = new  AssignmentRule(2,4);
      ar.setVariable( "s");
      ar.setFormula( "1 + 1");
      assertTrue( ar.getTypeCode() == libsbml.SBML_ASSIGNMENT_RULE );
      assertTrue( ar.getMetaId() == "" );
      assertTrue((  "s" == ar.getVariable() ));
      math = ar.getMath();
      assertTrue( math != null );
      formula = libsbml.formulaToString(math);
      assertTrue( formula != null );
      assertTrue((  "1 + 1" == formula ));
      assertTrue(( formula == ar.getFormula() ));
      ar = null;
    }

    public void test_AssignmentRule_createWithMath()
    {
      ASTNode math = libsbml.parseFormula("1 + 1");
      Rule ar = new  AssignmentRule(2,4);
      ar.setVariable( "s");
      ar.setMath(math);
      assertTrue( ar.getTypeCode() == libsbml.SBML_ASSIGNMENT_RULE );
      assertTrue( ar.getMetaId() == "" );
      assertTrue((  "s" == ar.getVariable() ));
      assertTrue((  "1 + 1" == ar.getFormula() ));
      assertTrue( ar.getMath() != math );
      ar = null;
    }

    public void test_AssignmentRule_createWithNS()
    {
      XMLNamespaces xmlns = new  XMLNamespaces();
      xmlns.add( "http://www.sbml.org", "testsbml");
      SBMLNamespaces sbmlns = new  SBMLNamespaces(2,1);
      sbmlns.addNamespaces(xmlns);
      Rule object1 = new  AssignmentRule(sbmlns);
      assertTrue( object1.getTypeCode() == libsbml.SBML_ASSIGNMENT_RULE );
      assertTrue( object1.getMetaId() == "" );
      assertTrue( object1.getNotes() == null );
      assertTrue( object1.getAnnotation() == null );
      assertTrue( object1.getLevel() == 2 );
      assertTrue( object1.getVersion() == 1 );
      assertTrue( object1.getNamespaces() != null );
      assertTrue( object1.getNamespaces().getLength() == 2 );
      object1 = null;
    }

    public void test_AssignmentRule_free_NULL()
    {
    }

    public void test_AssignmentRule_setVariable()
    {
      string variable =  "x";;
      AR.setVariable(variable);
      assertTrue(( variable == AR.getVariable() ));
      assertEquals( true, AR.isSetVariable() );
      if (AR.getVariable() == variable);
      {
      }
      AR.setVariable(AR.getVariable());
      assertTrue(( variable == AR.getVariable() ));
      AR.setVariable("");
      assertEquals( false, AR.isSetVariable() );
      if (AR.getVariable() != null);
      {
      }
    }

  }
}
