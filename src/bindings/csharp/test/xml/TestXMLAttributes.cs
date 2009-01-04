/// 
///  @file    TestXMLAttributes.cs
///  @brief   TestXMLAttributes unit tests
///  @author  Frank Bergmann (Csharp conversion)
///  @author  Akiya Jouraku (Csharp conversion)
///  @author  Ben Bornstein 
/// 
///  $Id:$
///  $HeadURL:$
/// 
///  This test file was converted from src/sbml/test/TestXMLAttributes.cpp
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

  public class TestXMLAttributes {
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



  public double util_NaN()
  {
    double z = 0.0;
    return 0.0/z;
  }

  public double util_PosInf()
  {
    double z = 0.0;
    return 1.0/z;
  }

  public double util_NegInf()
  {
    double z = 0.0;
    return -1.0/z;
  }

    public void test_XMLAttributes_add_get()
    {
      XMLAttributes attrs = new XMLAttributes();
      assertTrue( attrs.getLength() == 0 );
      assertEquals( true, attrs.isEmpty() );
      attrs.add("xmlns", "http://foo.org/");
      assertTrue( attrs.getLength() == 1 );
      assertTrue( attrs.isEmpty() == false );
      attrs.add("foo", "bar");
      assertTrue( attrs.getLength() == 2 );
      assertTrue( attrs.isEmpty() == false );
      assertTrue( attrs.getIndex("xmlns") == 0 );
      assertTrue( attrs.getIndex("foo"  ) == 1 );
      assertTrue( attrs.getIndex("bar"  ) == -1 );
      assertTrue( attrs.getValue("xmlns") ==  "http://foo.org/"  );
      assertTrue( attrs.getValue("foo"  ) ==  "bar"              );
      assertTrue( attrs.getValue("bar"  ) ==  ""                 );
      assertTrue( attrs.getName(0) ==  "xmlns"  );
      assertTrue( attrs.getName(1) ==  "foo"    );
      assertTrue( attrs.getName(2) ==  ""       );
    }

    public void test_XMLAttributes_add_removeResource()
    {
      XMLAttributes att1 = new XMLAttributes();
      att1.addResource("rdf", "http://foo.org/");
      att1.addResource("rdf", "http://foo1.org/");
      assertTrue( att1.getLength() == 2 );
      assertTrue( att1.isEmpty() == false );
      assertTrue( att1.getName(0) ==   "rdf"  );
      assertTrue( att1.getValue(0) ==  "http://foo.org/"  );
      assertTrue( att1.getName(1) ==   "rdf"  );
      assertTrue( att1.getValue(1) ==  "http://foo1.org/"  );
      att1.addResource("rdf", "http://foo2.org/");
      assertTrue( att1.getLength() == 3 );
      assertTrue( att1.isEmpty() == false );
      assertTrue( att1.getName(2) ==   "rdf"  );
      assertTrue( att1.getValue(2) ==  "http://foo2.org/"  );
      att1.removeResource(1);
      assertTrue( att1.getLength() == 2 );
      assertTrue( att1.isEmpty() == false );
      assertTrue( att1.getName(0) ==   "rdf"  );
      assertTrue( att1.getValue(0) ==  "http://foo.org/"  );
      assertTrue( att1.getName(1) ==   "rdf"  );
      assertTrue( att1.getValue(1) ==  "http://foo2.org/"  );
    }

    public void test_XMLAttributes_assignment()
    {
      XMLAttributes att1 = new XMLAttributes();
      att1.add("xmlns", "http://foo.org/");
      assertTrue( att1.getLength() == 1 );
      assertTrue( att1.isEmpty() == false );
      assertTrue( att1.getIndex("xmlns") == 0 );
      assertTrue( att1.getName(0) ==   "xmlns"  );
      assertTrue( att1.getValue("xmlns") ==  "http://foo.org/"  );
      XMLAttributes att2 = new XMLAttributes();
      att2 = att1;
      assertTrue( att2.getLength() == 1 );
      assertTrue( att2.isEmpty() == false );
      assertTrue( att2.getIndex("xmlns") == 0 );
      assertTrue( att2.getName(0) ==   "xmlns"  );
      assertTrue( att2.getValue("xmlns") ==  "http://foo.org/"  );
      att2 = null;
      att1 = null;
    }

    public void test_XMLAttributes_clone()
    {
      XMLAttributes att1 = new XMLAttributes();
      att1.add("xmlns", "http://foo.org/");
      assertTrue( att1.getLength() == 1 );
      assertTrue( att1.isEmpty() == false );
      assertTrue( att1.getIndex("xmlns") == 0 );
      assertTrue( att1.getName(0) ==   "xmlns"  );
      assertTrue( att1.getValue("xmlns") ==  "http://foo.org/"  );
      XMLAttributes att2 = ((XMLAttributes) att1.clone());
      assertTrue( att2.getLength() == 1 );
      assertTrue( att2.isEmpty() == false );
      assertTrue( att2.getIndex("xmlns") == 0 );
      assertTrue( att2.getName(0) ==   "xmlns"  );
      assertTrue( att2.getValue("xmlns") ==  "http://foo.org/"  );
      att2 = null;
      att1 = null;
    }

    public void test_XMLAttributes_copy()
    {
      XMLAttributes att1 = new XMLAttributes();
      att1.add("xmlns", "http://foo.org/");
      assertTrue( att1.getLength() == 1 );
      assertTrue( att1.isEmpty() == false );
      assertTrue( att1.getIndex("xmlns") == 0 );
      assertTrue( att1.getName(0) ==   "xmlns"  );
      assertTrue( att1.getValue("xmlns") ==  "http://foo.org/"  );
      XMLAttributes att2 = new XMLAttributes(att1);
      assertTrue( att2.getLength() == 1 );
      assertTrue( att2.isEmpty() == false );
      assertTrue( att2.getIndex("xmlns") == 0 );
      assertTrue( att2.getName(0) ==   "xmlns"  );
      assertTrue( att2.getValue("xmlns") ==  "http://foo.org/"  );
      att2 = null;
      att1 = null;
    }

  }
}
