/*
 *
 * @file    TestCopyAndClone.java
 * @brief   Read SBML unit tests
 *
 * @author  Akiya Jouraku (Java conversion)
 * @author  Ben Bornstein 
 *
 * $Id$
 * $HeadURL$
 *
 * This test file was converted from src/sbml/test/TestCopyAndClone.cpp
 * with the help of conversion sciprt (ctest_converter.pl).
 *
 *<!---------------------------------------------------------------------------
 * This file is part of libSBML.  Please visit http://sbml.org for more
 * information about SBML, and the latest version of libSBML.
 *
 * Copyright 2005-2009 California Institute of Technology.
 * Copyright 2002-2005 California Institute of Technology and
 *                     Japan Science and Technology Corporation.
 * 
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation.  A copy of the license agreement is provided
 * in the file named "LICENSE.txt" included with this software distribution
 * and also available online as http://sbml.org/software/libsbml/license.html
 *--------------------------------------------------------------------------->*/


package org.sbml.libsbml.test.xml;

import org.sbml.libsbml.*;

import java.io.File;
import java.lang.AssertionError;

public class TestCopyAndClone {

  static void assertTrue(boolean condition) throws AssertionError
  {
    if (condition == true)
    {
      return;
    }
    throw new AssertionError();
  }

  static void assertEquals(Object a, Object b) throws AssertionError
  {
    if ( (a == null) && (b == null) )
    {
      return;
    }
    else if (a.equals(b))
    {
      return;
    }

    throw new AssertionError();
  }

  static void assertNotEquals(Object a, Object b) throws AssertionError
  {
    if ( (a == null) && (b == null) )
    {
      throw new AssertionError();
    }
    else if (a.equals(b))
    {
      throw new AssertionError();
    }
  }

  static void assertEquals(boolean a, boolean b) throws AssertionError
  {
    if ( a == b )
    {
      return;
    }
    throw new AssertionError();
  }

  static void assertNotEquals(boolean a, boolean b) throws AssertionError
  {
    if ( a != b )
    {
      return;
    }
    throw new AssertionError();
  }

  static void assertEquals(int a, int b) throws AssertionError
  {
    if ( a == b )
    {
      return;
    }
    throw new AssertionError();
  }

  static void assertNotEquals(int a, int b) throws AssertionError
  {
    if ( a != b )
    {
      return;
    }
    throw new AssertionError();
  }

  public void test_NS_assignmentOperator()
  {
    XMLNamespaces ns = new XMLNamespaces();
    ns.add("http://test1.org/", "test1");
    assertTrue( ns.getLength() == 1 );
    assertTrue( ns.isEmpty() == false );
    assertTrue( ns.getPrefix(0).equals( "test1") );
    assertTrue( ns.getURI("test1").equals( "http://test1.org/") );
    XMLNamespaces ns2 = new XMLNamespaces();
    ns2 = ns;
    assertTrue( ns2.getLength() == 1 );
    assertTrue( ns2.isEmpty() == false );
    assertTrue( ns2.getPrefix(0).equals( "test1") );
    assertTrue( ns2.getURI("test1").equals( "http://test1.org/") );
    ns2 = null;
    ns = null;
  }

  public void test_NS_clone()
  {
    XMLNamespaces ns = new XMLNamespaces();
    ns.add("http://test1.org/", "test1");
    assertTrue( ns.getLength() == 1 );
    assertTrue( ns.isEmpty() == false );
    assertTrue( ns.getPrefix(0).equals( "test1") );
    assertTrue( ns.getURI("test1").equals( "http://test1.org/") );
    XMLNamespaces ns2 = (XMLNamespaces) ns.cloneObject();
    assertTrue( ns2.getLength() == 1 );
    assertTrue( ns2.isEmpty() == false );
    assertTrue( ns2.getPrefix(0).equals( "test1") );
    assertTrue( ns2.getURI("test1").equals( "http://test1.org/") );
    ns2 = null;
    ns = null;
  }

  public void test_NS_copyConstructor()
  {
    XMLNamespaces ns = new XMLNamespaces();
    ns.add("http://test1.org/", "test1");
    assertTrue( ns.getLength() == 1 );
    assertTrue( ns.isEmpty() == false );
    assertTrue( ns.getPrefix(0).equals( "test1") );
    assertTrue( ns.getURI("test1").equals( "http://test1.org/") );
    XMLNamespaces ns2 = new XMLNamespaces(ns);
    assertTrue( ns2.getLength() == 1 );
    assertTrue( ns2.isEmpty() == false );
    assertTrue( ns2.getPrefix(0).equals( "test1") );
    assertTrue( ns2.getURI("test1").equals( "http://test1.org/") );
    ns2 = null;
    ns = null;
  }

  public void test_Node_assignmentOperator()
  {
    XMLAttributes att = new XMLAttributes();
    XMLTriple t = new XMLTriple("sarah", "http://foo.org/", "bar");
    XMLToken token = new XMLToken(t,att,3,4);
    XMLNode node = new XMLNode(token);
    XMLNode child = new XMLNode();
    node.addChild(child);
    assertTrue( node.getNumChildren() == 1 );
    assertTrue( node.getName().equals( "sarah") );
    assertTrue( node.getURI().equals( "http://foo.org/") );
    assertTrue( node.getPrefix().equals( "bar") );
    assertTrue( node.isEnd() == false );
    assertTrue( node.isEOF() == false );
    assertTrue( node.getLine() == 3 );
    assertTrue( node.getColumn() == 4 );
    XMLNode node2 = new XMLNode();
    node2 = node;
    assertTrue( node2.getNumChildren() == 1 );
    assertTrue( node2.getName().equals( "sarah") );
    assertTrue( node2.getURI().equals( "http://foo.org/") );
    assertTrue( node2.getPrefix().equals( "bar") );
    assertTrue( node2.isEnd() == false );
    assertTrue( node2.isEOF() == false );
    assertTrue( node2.getLine() == 3 );
    assertTrue( node2.getColumn() == 4 );
    t = null;
    token = null;
    node = null;
    node2 = null;
  }

  public void test_Node_clone()
  {
    XMLAttributes att = new XMLAttributes();
    XMLTriple t = new XMLTriple("sarah", "http://foo.org/", "bar");
    XMLToken token = new XMLToken(t,att,3,4);
    XMLNode node = new XMLNode(token);
    XMLNode child = new XMLNode();
    node.addChild(child);
    assertTrue( node.getNumChildren() == 1 );
    assertTrue( node.getName().equals( "sarah") );
    assertTrue( node.getURI().equals( "http://foo.org/") );
    assertTrue( node.getPrefix().equals( "bar") );
    assertTrue( node.isEnd() == false );
    assertTrue( node.isEOF() == false );
    assertTrue( node.getLine() == 3 );
    assertTrue( node.getColumn() == 4 );
    XMLNode node2 = (XMLNode) node.cloneObject();
    assertTrue( node2.getNumChildren() == 1 );
    assertTrue( node2.getName().equals( "sarah") );
    assertTrue( node2.getURI().equals( "http://foo.org/") );
    assertTrue( node2.getPrefix().equals( "bar") );
    assertTrue( node2.isEnd() == false );
    assertTrue( node2.isEOF() == false );
    assertTrue( node2.getLine() == 3 );
    assertTrue( node2.getColumn() == 4 );
    t = null;
    token = null;
    node = null;
    node2 = null;
  }

  public void test_Node_copyConstructor()
  {
    XMLAttributes att = new XMLAttributes();
    XMLTriple t = new XMLTriple("sarah", "http://foo.org/", "bar");
    XMLToken token = new XMLToken(t,att,3,4);
    XMLNode node = new XMLNode(token);
    XMLNode child = new XMLNode();
    node.addChild(child);
    assertTrue( node.getNumChildren() == 1 );
    assertTrue( node.getName().equals( "sarah") );
    assertTrue( node.getURI().equals( "http://foo.org/") );
    assertTrue( node.getPrefix().equals( "bar") );
    assertTrue( node.isEnd() == false );
    assertTrue( node.isEOF() == false );
    assertTrue( node.getLine() == 3 );
    assertTrue( node.getColumn() == 4 );
    XMLNode node2 = new XMLNode(node);
    assertTrue( node2.getNumChildren() == 1 );
    assertTrue( node2.getName().equals( "sarah") );
    assertTrue( node2.getURI().equals( "http://foo.org/") );
    assertTrue( node2.getPrefix().equals( "bar") );
    assertTrue( node2.isEnd() == false );
    assertTrue( node2.isEOF() == false );
    assertTrue( node2.getLine() == 3 );
    assertTrue( node2.getColumn() == 4 );
    t = null;
    token = null;
    node = null;
    node2 = null;
  }

  public void test_Token_assignmentOperator()
  {
    XMLTriple t = new XMLTriple("sarah", "http://foo.org/", "bar");
    XMLToken token = new XMLToken(t,3,4);
    assertTrue( token.getName().equals( "sarah") );
    assertTrue( token.getURI().equals( "http://foo.org/") );
    assertTrue( token.getPrefix().equals( "bar") );
    assertTrue( token.isEnd() == true );
    assertTrue( token.isEOF() == false );
    assertTrue( token.getLine() == 3 );
    assertTrue( token.getColumn() == 4 );
    XMLToken token2 = new XMLToken();
    token2 = token;
    assertTrue( token2.getName().equals( "sarah") );
    assertTrue( token2.getURI().equals( "http://foo.org/") );
    assertTrue( token2.getPrefix().equals( "bar") );
    assertTrue( token2.isEnd() == true );
    assertTrue( token2.isEOF() == false );
    assertTrue( token2.getLine() == 3 );
    assertTrue( token2.getColumn() == 4 );
    t = null;
    token = null;
    token2 = null;
  }

  public void test_Token_clone()
  {
    XMLTriple t = new XMLTriple("sarah", "http://foo.org/", "bar");
    XMLToken token = new XMLToken(t,3,4);
    assertTrue( token.getName().equals( "sarah") );
    assertTrue( token.getURI().equals( "http://foo.org/") );
    assertTrue( token.getPrefix().equals( "bar") );
    assertTrue( token.isEnd() == true );
    assertTrue( token.isEOF() == false );
    assertTrue( token.getLine() == 3 );
    assertTrue( token.getColumn() == 4 );
    XMLToken token2 = (XMLToken) token.cloneObject();
    assertTrue( token2.getName().equals( "sarah") );
    assertTrue( token2.getURI().equals( "http://foo.org/") );
    assertTrue( token2.getPrefix().equals( "bar") );
    assertTrue( token2.isEnd() == true );
    assertTrue( token2.isEOF() == false );
    assertTrue( token2.getLine() == 3 );
    assertTrue( token2.getColumn() == 4 );
    t = null;
    token = null;
    token2 = null;
  }

  public void test_Token_copyConstructor()
  {
    XMLTriple t = new XMLTriple("sarah", "http://foo.org/", "bar");
    XMLToken token = new XMLToken(t,3,4);
    assertTrue( token.getName().equals( "sarah") );
    assertTrue( token.getURI().equals( "http://foo.org/") );
    assertTrue( token.getPrefix().equals( "bar") );
    assertTrue( token.isEnd() == true );
    assertTrue( token.isEOF() == false );
    assertTrue( token.getLine() == 3 );
    assertTrue( token.getColumn() == 4 );
    XMLToken token2 = new XMLToken(token);
    assertTrue( token2.getName().equals( "sarah") );
    assertTrue( token2.getURI().equals( "http://foo.org/") );
    assertTrue( token2.getPrefix().equals( "bar") );
    assertTrue( token2.isEnd() == true );
    assertTrue( token2.isEOF() == false );
    assertTrue( token2.getLine() == 3 );
    assertTrue( token2.getColumn() == 4 );
    t = null;
    token = null;
    token2 = null;
  }

  public void test_Triple_assignmentOperator()
  {
    XMLTriple t = new XMLTriple("sarah", "http://foo.org/", "bar");
    assertTrue( t.getName().equals( "sarah") );
    assertTrue( t.getURI().equals( "http://foo.org/") );
    assertTrue( t.getPrefix().equals( "bar") );
    XMLTriple t2 = new XMLTriple();
    t2 = t;
    assertTrue( t2.getName().equals( "sarah") );
    assertTrue( t2.getURI().equals( "http://foo.org/") );
    assertTrue( t2.getPrefix().equals( "bar") );
    t = null;
    t2 = null;
  }

  public void test_Triple_clone()
  {
    XMLTriple t = new XMLTriple("sarah", "http://foo.org/", "bar");
    assertTrue( t.getName().equals( "sarah") );
    assertTrue( t.getURI().equals( "http://foo.org/") );
    assertTrue( t.getPrefix().equals( "bar") );
    XMLTriple t2 = (XMLTriple) t.cloneObject();
    assertTrue( t2.getName().equals( "sarah") );
    assertTrue( t2.getURI().equals( "http://foo.org/") );
    assertTrue( t2.getPrefix().equals( "bar") );
    t = null;
    t2 = null;
  }

  public void test_Triple_copyConstructor()
  {
    XMLTriple t = new XMLTriple("sarah", "http://foo.org/", "bar");
    assertTrue( t.getName().equals( "sarah") );
    assertTrue( t.getURI().equals( "http://foo.org/") );
    assertTrue( t.getPrefix().equals( "bar") );
    XMLTriple t2 = new XMLTriple(t);
    assertTrue( t2.getName().equals( "sarah") );
    assertTrue( t2.getURI().equals( "http://foo.org/") );
    assertTrue( t2.getPrefix().equals( "bar") );
    t = null;
    t2 = null;
  }

  /**
   * Loads the SWIG-generated libSBML Java module when this class is
   * loaded, or reports a sensible diagnostic message about why it failed.
   */
  static
  {
    String varname;
    String shlibname;

    if (System.getProperty("mrj.version") != null)
    {
      varname = "DYLD_LIBRARY_PATH";    // We're on a Mac.
      shlibname = "libsbmlj.jnilib and/or libsbml.dylib";
    }
    else
    {
      varname = "LD_LIBRARY_PATH";      // We're not on a Mac.
      shlibname = "libsbmlj.so and/or libsbml.so";
    }

    try
    {
      System.loadLibrary("sbmlj");
      // For extra safety, check that the jar file is in the classpath.
      Class.forName("org.sbml.libsbml.libsbml");
    }
    catch (SecurityException e)
    {
      e.printStackTrace();
      System.err.println("Could not load the libSBML library files due to a"+
                         " security exception.\n");
      System.exit(1);
    }
    catch (UnsatisfiedLinkError e)
    {
      e.printStackTrace();
      System.err.println("Error: could not link with the libSBML library files."+
                         " It is likely\nyour " + varname +
                         " environment variable does not include the directories\n"+
                         "containing the " + shlibname + " library files.\n");
      System.exit(1);
    }
    catch (ClassNotFoundException e)
    {
      e.printStackTrace();
      System.err.println("Error: unable to load the file libsbmlj.jar."+
                         " It is likely\nyour -classpath option and CLASSPATH" +
                         " environment variable\n"+
                         "do not include the path to libsbmlj.jar.\n");
      System.exit(1);
    }
  }
}
