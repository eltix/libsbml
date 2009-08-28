/// 
///  @file    TestXMLAttributesC.cs
///  @brief   XMLAttributes unit tests, C version
///  @author  Frank Bergmann (Csharp conversion)
///  @author  Akiya Jouraku (Csharp conversion)
///  @author  Sarah Keating 
/// 
///  $Id$
///  $HeadURL$
/// 
///  This test file was converted from src/sbml/test/TestXMLAttributesC.c
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

  public class TestXMLAttributesC {
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


    public void test_XMLAttributes_add1()
    {
      XMLAttributes xa = new  XMLAttributes();
      XMLTriple xt2 = new  XMLTriple("name2", "http://name2.org/", "p2");
      long i = xa.add( "name1", "val1", "http://name1.org/", "p1");
      assertTrue( i == libsbml.LIBSBML_OPERATION_SUCCESS );
      i = xa.add(xt2, "val2");
      assertTrue( i == libsbml.LIBSBML_OPERATION_SUCCESS );
      assertTrue( xa.getLength() == 2 );
      assertTrue( xa.isEmpty() == false );
      i = xa.add( "noprefix", "val3");
      assertTrue( i == libsbml.LIBSBML_OPERATION_SUCCESS );
      assertTrue( xa.getLength() == 3 );
      assertTrue( xa.isEmpty() == false );
      xa = null;
      xt2 = null;
    }

    public void test_XMLAttributes_add_remove_qname_C()
    {
      XMLAttributes xa = new  XMLAttributes();
      XMLTriple xt1 = new  XMLTriple("name1", "http://name1.org/", "p1");
      XMLTriple xt2 = new  XMLTriple("name2", "http://name2.org/", "p2");
      XMLTriple xt3 = new  XMLTriple("name3", "http://name3.org/", "p3");
      XMLTriple xt1a = new  XMLTriple("name1", "http://name1a.org/", "p1a");
      XMLTriple xt2a = new  XMLTriple("name2", "http://name2a.org/", "p2a");
      xa.add( "name1", "val1", "http://name1.org/", "p1");
      xa.add(xt2, "val2");
      assertTrue( xa.getLength() == 2 );
      assertTrue( xa.isEmpty() == false );
      assertTrue( (  "name1" != xa.getName(0) ) == false );
      assertTrue( (  "val1"  != xa.getValue(0) ) == false );
      assertTrue( (  "http://name1.org/" != xa.getURI(0) ) == false );
      assertTrue( (  "p1"    != xa.getPrefix(0) ) == false );
      assertTrue( (  "name2" != xa.getName(1) ) == false );
      assertTrue( (  "val2"  != xa.getValue(1) ) == false );
      assertTrue( (  "http://name2.org/" != xa.getURI(1) ) == false );
      assertTrue( (  "p2"    != xa.getPrefix(1) ) == false );
      assertTrue( (  "val1"  != xa.getValue( "name1") ) == false );
      assertTrue( (  "val2"  != xa.getValue( "name2") ) == false );
      assertTrue( (  "val1"  != xa.getValue( "name1", "http://name1.org/") ) == false );
      assertTrue( (  "val2"  != xa.getValue( "name2", "http://name2.org/") ) == false );
      assertTrue( (  "val1"  != xa.getValue(xt1) ) == false );
      assertTrue( (  "val2"  != xa.getValue(xt2) ) == false );
      assertTrue( xa.hasAttribute(-1) == false );
      assertTrue( xa.hasAttribute(2) == false );
      assertTrue( xa.hasAttribute(0) == true );
      assertTrue( xa.hasAttribute( "name1", "http://name1.org/") == true );
      assertTrue( xa.hasAttribute( "name2", "http://name2.org/") == true );
      assertTrue( xa.hasAttribute( "name3", "http://name3.org/") == false );
      assertTrue( xa.hasAttribute(xt1) == true );
      assertTrue( xa.hasAttribute(xt2) == true );
      assertTrue( xa.hasAttribute(xt3) == false );
      xa.add( "noprefix", "val3");
      assertTrue( xa.getLength() == 3 );
      assertTrue( xa.isEmpty() == false );
      assertTrue( (  "noprefix" != xa.getName(2) ) == false );
      assertTrue( (  "val3"     != xa.getValue(2) ) == false );
      assertTrue( xa.getURI(2) == "" );
      assertTrue( xa.getPrefix(2) == "" );
      assertTrue( (  "val3"  != xa.getValue( "noprefix", "") ) == false );
      assertTrue( xa.hasAttribute( "noprefix"    ) == true );
      assertTrue( xa.hasAttribute( "noprefix", "") == true );
      xa.add(xt1, "mval1");
      xa.add( "name2", "mval2", "http://name2.org/", "p2");
      xa.add( "noprefix", "mval3");
      assertTrue( xa.getLength() == 3 );
      assertTrue( xa.isEmpty() == false );
      assertTrue( (  "name1" != xa.getName(0) ) == false );
      assertTrue( (  "mval1" != xa.getValue(0) ) == false );
      assertTrue( (  "http://name1.org/" != xa.getURI(0) ) == false );
      assertTrue( (  "p1"    != xa.getPrefix(0) ) == false );
      assertTrue( (  "name2"    != xa.getName(1) ) == false );
      assertTrue( (  "mval2"    != xa.getValue(1) ) == false );
      assertTrue( (  "http://name2.org/" != xa.getURI(1) ) == false );
      assertTrue( (  "p2"       != xa.getPrefix(1) ) == false );
      assertTrue( (  "noprefix" != xa.getName(2) ) == false );
      assertTrue( (  "mval3"    != xa.getValue(2) ) == false );
      assertTrue( xa.getURI(2) == "" );
      assertTrue( xa.getPrefix(2) == "" );
      assertTrue( xa.hasAttribute(xt1) == true );
      assertTrue( xa.hasAttribute( "name1", "http://name1.org/") == true );
      assertTrue( xa.hasAttribute( "noprefix") == true );
      xa.add(xt1a, "val1a");
      xa.add(xt2a, "val2a");
      assertTrue( xa.getLength() == 5 );
      assertTrue( (  "name1" != xa.getName(3) ) == false );
      assertTrue( (  "val1a" != xa.getValue(3) ) == false );
      assertTrue( (  "http://name1a.org/" != xa.getURI(3) ) == false );
      assertTrue( (  "p1a" != xa.getPrefix(3) ) == false );
      assertTrue( (  "name2" != xa.getName(4) ) == false );
      assertTrue( (  "val2a" != xa.getValue(4) ) == false );
      assertTrue( (  "http://name2a.org/" != xa.getURI(4) ) == false );
      assertTrue( (  "p2a" != xa.getPrefix(4) ) == false );
      assertTrue( (  "mval1"  != xa.getValue( "name1") ) == false );
      assertTrue( (  "mval2"  != xa.getValue( "name2") ) == false );
      assertTrue( (  "val1a"  != xa.getValue( "name1", "http://name1a.org/") ) == false );
      assertTrue( (  "val2a"  != xa.getValue( "name2", "http://name2a.org/") ) == false );
      assertTrue( (  "val1a"  != xa.getValue(xt1a) ) == false );
      assertTrue( (  "val2a"  != xa.getValue(xt2a) ) == false );
      xa.remove(xt1a);
      xa.remove(xt2a);
      assertTrue( xa.getLength() == 3 );
      xa.remove( "name1", "http://name1.org/");
      assertTrue( xa.getLength() == 2 );
      assertTrue( xa.isEmpty() == false );
      assertTrue( (  "name2" != xa.getName(0) ) == false );
      assertTrue( (  "mval2" != xa.getValue(0) ) == false );
      assertTrue( (  "http://name2.org/" != xa.getURI(0) ) == false );
      assertTrue( (  "p2" != xa.getPrefix(0) ) == false );
      assertTrue( (  "noprefix" != xa.getName(1) ) == false );
      assertTrue( (  "mval3" != xa.getValue(1) ) == false );
      assertTrue( xa.getURI(1) == "" );
      assertTrue( xa.getPrefix(1) == "" );
      assertTrue( xa.hasAttribute( "name1", "http://name1.org/") == false );
      xa.remove(xt2);
      assertTrue( xa.getLength() == 1 );
      assertTrue( xa.isEmpty() == false );
      assertTrue( (  "noprefix" != xa.getName(0) ) == false );
      assertTrue( (  "mval3" != xa.getValue(0) ) == false );
      assertTrue( xa.getURI(0) == "" );
      assertTrue( xa.getPrefix(0) == "" );
      assertTrue( xa.hasAttribute(xt2) == false );
      assertTrue( xa.hasAttribute( "name2", "http://name2.org/") == false );
      xa.remove( "noprefix", "");
      assertTrue( xa.getLength() == 0 );
      assertTrue( xa.isEmpty() == true );
      assertTrue( xa.hasAttribute( "noprefix"    ) == false );
      assertTrue( xa.hasAttribute( "noprefix", "") == false );
      xa = null;
      xt1 = null;
      xt2 = null;
      xt3 = null;
      xt1a = null;
      xt2a = null;
    }

    public void test_XMLAttributes_clear1()
    {
      XMLAttributes xa = new  XMLAttributes();
      XMLTriple xt2 = new  XMLTriple("name2", "http://name2.org/", "p2");
      long i = xa.add( "name1", "val1", "http://name1.org/", "p1");
      i = xa.add(xt2, "val2");
      i = xa.add( "noprefix", "val3");
      assertTrue( xa.getLength() == 3 );
      assertTrue( xa.isEmpty() == false );
      i = xa.clear();
      assertTrue( i == libsbml.LIBSBML_OPERATION_SUCCESS );
      assertTrue( xa.getLength() == 0 );
      assertTrue( xa.isEmpty() == true );
      xa = null;
      xt2 = null;
    }

    public void test_XMLAttributes_remove1()
    {
      XMLAttributes xa = new  XMLAttributes();
      XMLTriple xt2 = new  XMLTriple("name2", "http://name2.org/", "p2");
      long i = xa.add( "name1", "val1", "http://name1.org/", "p1");
      assertTrue( i == libsbml.LIBSBML_OPERATION_SUCCESS );
      i = xa.add(xt2, "val2");
      assertTrue( i == libsbml.LIBSBML_OPERATION_SUCCESS );
      i = xa.add( "noprefix", "val3");
      assertTrue( i == libsbml.LIBSBML_OPERATION_SUCCESS );
      i = xa.add( "name4", "val4", "http://name4.org/", "p1");
      assertTrue( i == libsbml.LIBSBML_OPERATION_SUCCESS );
      assertTrue( xa.getLength() == 4 );
      i = xa.remove(4);
      assertTrue( i == libsbml.LIBSBML_INDEX_EXCEEDS_SIZE );
      i = xa.remove(3);
      assertTrue( i == libsbml.LIBSBML_OPERATION_SUCCESS );
      assertTrue( xa.getLength() == 3 );
      i = xa.remove( "noprefix");
      assertTrue( i == libsbml.LIBSBML_OPERATION_SUCCESS );
      assertTrue( xa.getLength() == 2 );
      i = xa.remove(xt2);
      assertTrue( i == libsbml.LIBSBML_OPERATION_SUCCESS );
      assertTrue( xa.getLength() == 1 );
      i = xa.remove( "name1", "http://name1.org/");
      assertTrue( i == libsbml.LIBSBML_OPERATION_SUCCESS );
      assertTrue( xa.getLength() == 0 );
      xa = null;
      xt2 = null;
    }

  }
}
