/*
 *
 * @file    TestReadFromFile6.java
 * @brief   Reads test-data/l2v2-newComponents.xml into memory and tests it.
 *
 * @author  Akiya Jouraku (Java conversion)
 * @author  Sarah Keating 
 *
 * $Id$
 * $HeadURL$
 *
 * This test file was converted from src/sbml/test/TestReadFromFile6.cpp
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


package org.sbml.libsbml.test.sbml;

import org.sbml.libsbml.*;

import java.io.File;
import java.lang.AssertionError;

public class TestReadFromFile6 {

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

  public void test_read_l2v2_newComponents()
  {
    SBMLReader reader = new SBMLReader();
    SBMLDocument d;
    Model m;
    Compartment c;
    CompartmentType ct;
    Species s;
    Parameter p;
    Reaction r;
    SpeciesReference sr;
    KineticLaw kl;
    Constraint con;
    InitialAssignment ia;
    SpeciesType st;
    ListOfCompartmentTypes loct;
    CompartmentType ct1;
    ListOfConstraints locon;
    Constraint con1;
    ListOfInitialAssignments loia;
    InitialAssignment ia1;
    ListOfReactions lor;
    Reaction r1;
    ListOfSpeciesReferences losr;
    SpeciesReference sr1;
    ASTNode ast;
    String filename = new String( "../../sbml/test/test-data/" );
    filename += "l2v2-newComponents.xml";
    d = reader.readSBML(filename);
    if (d == null);
    {
    }
    assertTrue( d.getLevel() == 2 );
    assertTrue( d.getVersion() == 2 );
    m = d.getModel();
    assertTrue( m != null );
    assertTrue( m.getId().equals( "l2v2_newComponents") );
    assertTrue( m.getSBOTerm() == 4 );
    assertTrue( m.getSBOTermID().equals( "SBO:0000004") );
    assertTrue( m.getNumCompartments() == 2 );
    c = m.getCompartment(0);
    assertTrue( c != null );
    assertTrue( c.getId().equals( "cell") );
    assertEquals(c.getCompartmentType(), "mitochondria");
    assertTrue( c.getOutside().equals( "m") );
    assertTrue( c.getSBOTerm() == -1 );
    assertTrue( c.getSBOTermID().equals( "") );
    c = m.getCompartment(1);
    assertTrue( c != null );
    assertTrue( c.getId().equals( "m") );
    assertEquals(c.getCompartmentType(), "mitochondria");
    assertTrue( m.getNumCompartmentTypes() == 1 );
    ct = m.getCompartmentType(0);
    assertTrue( ct != null );
    assertTrue( ct.getId().equals( "mitochondria") );
    loct = m.getListOfCompartmentTypes();
    ct1 = loct.get(0);
    assertTrue( ct1.equals(ct) );
    ct1 = loct.get("mitochondria");
    assertTrue( ct1.equals(ct) );
    assertTrue( m.getNumSpeciesTypes() == 1 );
    st = m.getSpeciesType(0);
    assertTrue( st != null );
    assertTrue( st.getId().equals( "Glucose") );
    assertTrue( m.getNumSpecies() == 2 );
    s = m.getSpecies(0);
    assertTrue( s != null );
    assertTrue( s.getId().equals( "X0") );
    assertEquals(s.getSpeciesType(), "Glucose");
    assertTrue( s.getCompartment().equals( "cell") );
    assertEquals( false, s.isSetInitialAmount() );
    assertEquals( false, s.isSetInitialConcentration() );
    s = m.getSpecies(1);
    assertTrue( s != null );
    assertTrue( s.getId().equals( "X1") );
    assertEquals( false, s.isSetSpeciesType() );
    assertTrue( s.getCompartment().equals( "cell") );
    assertTrue( s.getInitialConcentration() == 0.013 );
    assertEquals( false, s.isSetInitialAmount() );
    assertEquals( true, s.isSetInitialConcentration() );
    assertTrue( m.getNumParameters() == 1 );
    p = m.getParameter(0);
    assertTrue( p != null );
    assertTrue( p.getId().equals( "y") );
    assertTrue( p.getValue() == 2 );
    assertTrue( p.getUnits().equals( "dimensionless") );
    assertTrue( p.getId().equals( "y") );
    assertTrue( p.getSBOTerm() == 2 );
    assertTrue( p.getSBOTermID().equals( "SBO:0000002") );
    assertTrue( m.getNumConstraints() == 1 );
    con = m.getConstraint(0);
    assertTrue( con != null );
    assertTrue( con.getSBOTerm() == 64 );
    assertTrue( con.getSBOTermID().equals( "SBO:0000064") );
    ast = con.getMath();
    assertTrue(libsbml.formulaToString(ast).equals( "lt(1, cell)"));
    locon = m.getListOfConstraints();
    con1 = locon.get(0);
    assertTrue( con1.equals(con) );
    assertTrue( m.getNumInitialAssignments() == 1 );
    ia = m.getInitialAssignment(0);
    assertTrue( ia != null );
    assertTrue( ia.getSBOTerm() == 64 );
    assertTrue( ia.getSBOTermID().equals( "SBO:0000064") );
    assertTrue( ia.getSymbol().equals( "X0") );
    ast = ia.getMath();
    assertTrue(libsbml.formulaToString(ast).equals( "y * X1"));
    loia = m.getListOfInitialAssignments();
    ia1 = loia.get(0);
    assertTrue( ia1.equals(ia) );
    ia1 = loia.get("X0");
    assertTrue( ia1.equals(ia) );
    assertTrue( m.getNumReactions() == 1 );
    r = m.getReaction(0);
    assertTrue( r != null );
    assertTrue( r.getSBOTerm() == 231 );
    assertTrue( r.getSBOTermID().equals( "SBO:0000231") );
    assertTrue( r.getId().equals( "in") );
    lor = m.getListOfReactions();
    r1 = lor.get(0);
    assertTrue( r1.equals(r) );
    r1 = lor.get("in");
    assertTrue( r1.equals(r) );
    assertEquals( true, r.isSetKineticLaw() );
    kl = r.getKineticLaw();
    assertTrue( kl != null );
    assertTrue( kl.getSBOTerm() == 1 );
    assertTrue( kl.getSBOTermID().equals( "SBO:0000001") );
    assertEquals( true, kl.isSetMath() );
    ast = kl.getMath();
    assertTrue(libsbml.formulaToString(ast).equals( "v * X0 / t"));
    assertTrue( kl.getNumParameters() == 2 );
    p = kl.getParameter(0);
    assertTrue( p != null );
    assertTrue( p.getSBOTerm() == 2 );
    assertTrue( p.getSBOTermID().equals( "SBO:0000002") );
    assertTrue( p.getId().equals( "v") );
    assertTrue( p.getUnits().equals( "litre") );
    assertTrue( r.getNumReactants() == 1 );
    assertTrue( r.getNumProducts() == 0 );
    assertTrue( r.getNumModifiers() == 0 );
    sr = r.getReactant(0);
    assertTrue( sr != null );
    assertTrue( sr.getName().equals( "sarah") );
    assertTrue( sr.getId().equals( "me") );
    assertTrue( sr.getSpecies().equals( "X0") );
    losr = r.getListOfReactants();
    sr1 = (SpeciesReference) losr.get(0);
    assertTrue( sr1.equals(sr) );
    sr1 = (SpeciesReference) losr.get("me");
    assertTrue( sr1.equals(sr) );
    d = null;
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
