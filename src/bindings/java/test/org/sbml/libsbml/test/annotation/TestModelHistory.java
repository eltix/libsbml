/*
 *
 * @file    TestModelHistory.java
 * @brief   ModelHistory unit tests
 *
 * @author  Akiya Jouraku (Java conversion)
 * @author  Sarah Keating 
 *
 * $Id$
 * $HeadURL$
 *
 * This test file was converted from src/sbml/test/TestModelHistory.c
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


package org.sbml.libsbml.test.annotation;

import org.sbml.libsbml.*;

import java.io.File;
import java.lang.AssertionError;

public class TestModelHistory {

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
    else if ( (a == null) || (b == null) )
    {
      throw new AssertionError();
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
    else if ( (a == null) || (b == null) )
    {
      return;
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

  public void test_Date_create()
  {
    Date date = new  Date(2005,12,30,12,15,45,1,2,0);
    assertTrue( date != null );
    assertTrue( date.getYear() == 2005 );
    assertTrue( date.getMonth() == 12 );
    assertTrue( date.getDay() == 30 );
    assertTrue( date.getHour() == 12 );
    assertTrue( date.getMinute() == 15 );
    assertTrue( date.getSecond() == 45 );
    assertTrue( date.getSignOffset() == 1 );
    assertTrue( date.getHoursOffset() == 2 );
    assertTrue( date.getMinutesOffset() == 0 );
    date = null;
  }

  public void test_Date_createFromString()
  {
    String dd =  "2012-12-02T14:56:11Z";;
    Date date = new  Date(dd);
    assertTrue( date != null );
    assertTrue(date.getDateAsString().equals( "2012-12-02T14:56:11Z"));
    assertTrue( date.getYear() == 2012 );
    assertTrue( date.getMonth() == 12 );
    assertTrue( date.getDay() == 2 );
    assertTrue( date.getHour() == 14 );
    assertTrue( date.getMinute() == 56 );
    assertTrue( date.getSecond() == 11 );
    assertTrue( date.getSignOffset() == 0 );
    assertTrue( date.getHoursOffset() == 0 );
    assertTrue( date.getMinutesOffset() == 0 );
    date = null;
  }

  public void test_Date_getDateAsString()
  {
    String dd =  "2005-02-02T14:56:11Z";;
    Date date = new  Date(dd);
    assertTrue( date != null );
    assertTrue( date.getYear() == 2005 );
    assertTrue( date.getMonth() == 2 );
    assertTrue( date.getDay() == 2 );
    assertTrue( date.getHour() == 14 );
    assertTrue( date.getMinute() == 56 );
    assertTrue( date.getSecond() == 11 );
    assertTrue( date.getSignOffset() == 0 );
    assertTrue( date.getHoursOffset() == 0 );
    assertTrue( date.getMinutesOffset() == 0 );
    date.setYear(2012);
    date.setMonth(3);
    date.setDay(28);
    date.setHour(23);
    date.setMinute(4);
    date.setSecond(32);
    date.setSignOffset(1);
    date.setHoursOffset(2);
    date.setMinutesOffset(32);
    assertTrue(date.getDateAsString().equals( "2012-03-28T23:04:32+02:32"));
    date = null;
  }

  public void test_Date_setters()
  {
    Date date = new  Date(2005,12,30,12,15,45,1,2,0);
    assertTrue( date != null );
    date.setYear(2012);
    date.setMonth(3);
    date.setDay(28);
    date.setHour(23);
    date.setMinute(4);
    date.setSecond(32);
    date.setSignOffset(1);
    date.setHoursOffset(2);
    date.setMinutesOffset(32);
    assertTrue( date.getYear() == 2012 );
    assertTrue( date.getMonth() == 3 );
    assertTrue( date.getDay() == 28 );
    assertTrue( date.getHour() == 23 );
    assertTrue( date.getMinute() == 4 );
    assertTrue( date.getSecond() == 32 );
    assertTrue( date.getSignOffset() == 1 );
    assertTrue( date.getHoursOffset() == 2 );
    assertTrue( date.getMinutesOffset() == 32 );
    assertTrue(date.getDateAsString().equals( "2012-03-28T23:04:32+02:32"));
    date = null;
  }

  public void test_ModelCreator_create()
  {
    ModelCreator mc = new  ModelCreator();
    assertTrue( mc != null );
    mc = null;
  }

  public void test_ModelCreator_setters()
  {
    ModelCreator mc = new  ModelCreator();
    assertTrue( mc != null );
    assertTrue( mc.isSetFamilyName() == false );
    assertTrue( mc.isSetGivenName() == false );
    assertTrue( mc.isSetEmail() == false );
    assertTrue( mc.isSetOrganisation() == false );
    mc.setFamilyName( "Keating");
    mc.setGivenName( "Sarah");
    mc.setEmail( "sbml-team@caltech.edu");
    mc.setOrganisation( "UH");
    assertTrue(mc.getFamilyName().equals( "Keating"));
    assertTrue(mc.getGivenName().equals( "Sarah"));
    assertTrue(mc.getEmail().equals( "sbml-team@caltech.edu"));
    assertTrue(mc.getOrganisation().equals( "UH"));
    assertTrue( mc.isSetFamilyName() == true );
    assertTrue( mc.isSetGivenName() == true );
    assertTrue( mc.isSetEmail() == true );
    assertTrue( mc.isSetOrganisation() == true );
    mc.unsetFamilyName();
    mc.unsetGivenName();
    mc.unsetEmail();
    mc.unsetOrganisation();
    assertTrue(mc.getFamilyName().equals( ""));
    assertTrue(mc.getGivenName().equals( ""));
    assertTrue(mc.getEmail().equals( ""));
    assertTrue(mc.getOrganisation().equals( ""));
    assertTrue( mc.isSetFamilyName() == false );
    assertTrue( mc.isSetGivenName() == false );
    assertTrue( mc.isSetEmail() == false );
    assertTrue( mc.isSetOrganisation() == false );
    assertTrue( mc.isSetOrganization() == false );
    mc.setOrganization( "UH");
    assertTrue(mc.getOrganization().equals( "UH"));
    assertTrue( mc.isSetOrganization() == true );
    mc.unsetOrganisation();
    assertTrue(mc.getOrganization().equals( ""));
    assertTrue( mc.isSetOrganization() == false );
    mc = null;
  }

  public void test_ModelHistory_addCreator()
  {
    ModelCreator newMC;
    ModelHistory history = new  ModelHistory();
    assertTrue( history.getNumCreators() == 0 );
    assertTrue( history != null );
    ModelCreator mc = new  ModelCreator();
    assertTrue( mc != null );
    mc.setFamilyName( "Keating");
    mc.setGivenName( "Sarah");
    mc.setEmail( "sbml-team@caltech.edu");
    mc.setOrganisation( "UH");
    history.addCreator(mc);
    assertTrue( history.getNumCreators() == 1 );
    mc = null;
    newMC = history.getListCreators().get(0);
    assertTrue( newMC != null );
    assertTrue(newMC.getFamilyName().equals( "Keating"));
    assertTrue(newMC.getGivenName().equals( "Sarah"));
    assertTrue(newMC.getEmail().equals( "sbml-team@caltech.edu"));
    assertTrue(newMC.getOrganisation().equals( "UH"));
    history = null;
  }

  public void test_ModelHistory_addModifiedDate()
  {
    ModelHistory history = new  ModelHistory();
    assertTrue( history != null );
    assertTrue( history.isSetModifiedDate() == false );
    assertTrue( history.getNumModifiedDates() == 0 );
    Date date = new  Date(2005,12,30,12,15,45,1,2,0);
    history.addModifiedDate(date);
    date = null;
    assertTrue( history.getNumModifiedDates() == 1 );
    assertTrue( history.isSetModifiedDate() == true );
    Date newdate = history.getListModifiedDates().get(0);
    assertTrue( newdate.getYear() == 2005 );
    assertTrue( newdate.getMonth() == 12 );
    assertTrue( newdate.getDay() == 30 );
    assertTrue( newdate.getHour() == 12 );
    assertTrue( newdate.getMinute() == 15 );
    assertTrue( newdate.getSecond() == 45 );
    assertTrue( newdate.getSignOffset() == 1 );
    assertTrue( newdate.getHoursOffset() == 2 );
    assertTrue( newdate.getMinutesOffset() == 0 );
    Date date1 = new  Date(2008,11,2,16,42,40,1,2,0);
    history.addModifiedDate(date1);
    date1 = null;
    assertTrue( history.getNumModifiedDates() == 2 );
    assertTrue( history.isSetModifiedDate() == true );
    Date newdate1 = history.getModifiedDate(1);
    assertTrue( newdate1.getYear() == 2008 );
    assertTrue( newdate1.getMonth() == 11 );
    assertTrue( newdate1.getDay() == 2 );
    assertTrue( newdate1.getHour() == 16 );
    assertTrue( newdate1.getMinute() == 42 );
    assertTrue( newdate1.getSecond() == 40 );
    assertTrue( newdate1.getSignOffset() == 1 );
    assertTrue( newdate1.getHoursOffset() == 2 );
    assertTrue( newdate1.getMinutesOffset() == 0 );
    history = null;
  }

  public void test_ModelHistory_create()
  {
    ModelHistory history = new  ModelHistory();
    assertTrue( history != null );
    assertTrue( history.getListCreators() != null );
    assertTrue( history.getCreatedDate() == null );
    assertTrue( history.getModifiedDate() == null );
    history = null;
  }

  public void test_ModelHistory_setCreatedDate()
  {
    ModelHistory history = new  ModelHistory();
    assertTrue( history != null );
    assertTrue( history.isSetCreatedDate() == false );
    Date date = new  Date(2005,12,30,12,15,45,1,2,0);
    history.setCreatedDate(date);
    assertTrue( history.isSetCreatedDate() == true );
    date = null;
    Date newdate = history.getCreatedDate();
    assertTrue( newdate.getYear() == 2005 );
    assertTrue( newdate.getMonth() == 12 );
    assertTrue( newdate.getDay() == 30 );
    assertTrue( newdate.getHour() == 12 );
    assertTrue( newdate.getMinute() == 15 );
    assertTrue( newdate.getSecond() == 45 );
    assertTrue( newdate.getSignOffset() == 1 );
    assertTrue( newdate.getHoursOffset() == 2 );
    assertTrue( newdate.getMinutesOffset() == 0 );
    history = null;
  }

  public void test_ModelHistory_setModifiedDate()
  {
    ModelHistory history = new  ModelHistory();
    assertTrue( history != null );
    assertTrue( history.isSetModifiedDate() == false );
    Date date = new  Date(2005,12,30,12,15,45,1,2,0);
    history.setModifiedDate(date);
    date = null;
    assertTrue( history.isSetModifiedDate() == true );
    Date newdate = history.getModifiedDate();
    assertTrue( newdate.getYear() == 2005 );
    assertTrue( newdate.getMonth() == 12 );
    assertTrue( newdate.getDay() == 30 );
    assertTrue( newdate.getHour() == 12 );
    assertTrue( newdate.getMinute() == 15 );
    assertTrue( newdate.getSecond() == 45 );
    assertTrue( newdate.getSignOffset() == 1 );
    assertTrue( newdate.getHoursOffset() == 2 );
    assertTrue( newdate.getMinutesOffset() == 0 );
    history = null;
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
