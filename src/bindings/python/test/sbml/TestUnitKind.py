#
# @file    TestUnitKind.py
# @brief   UnitKind enumeration unit tests
#
# @author  Akiya Jouraku (Python conversion)
# @author  Ben Bornstein 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestUnitKind.c
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

class TestUnitKind(unittest.TestCase):


  def test_UnitKind_equals(self):
    self.assertEqual( 1, libsbml.UnitKind_equals(libsbml.UNIT_KIND_AMPERE,libsbml.UNIT_KIND_AMPERE) )
    self.assertEqual( 1, libsbml.UnitKind_equals(libsbml.UNIT_KIND_INVALID,libsbml.UNIT_KIND_INVALID) )
    self.assertEqual( 1, libsbml.UnitKind_equals(libsbml.UNIT_KIND_LITER,libsbml.UNIT_KIND_LITER) )
    self.assertEqual( 1, libsbml.UnitKind_equals(libsbml.UNIT_KIND_LITRE,libsbml.UNIT_KIND_LITRE) )
    self.assertEqual( 1, libsbml.UnitKind_equals(libsbml.UNIT_KIND_METER,libsbml.UNIT_KIND_METER) )
    self.assertEqual( 1, libsbml.UnitKind_equals(libsbml.UNIT_KIND_METRE,libsbml.UNIT_KIND_METRE) )
    self.assertEqual( 1, libsbml.UnitKind_equals(libsbml.UNIT_KIND_LITER,libsbml.UNIT_KIND_LITRE) )
    self.assertEqual( 1, libsbml.UnitKind_equals(libsbml.UNIT_KIND_LITRE,libsbml.UNIT_KIND_LITER) )
    self.assertEqual( 1, libsbml.UnitKind_equals(libsbml.UNIT_KIND_METER,libsbml.UNIT_KIND_METRE) )
    self.assertEqual( 1, libsbml.UnitKind_equals(libsbml.UNIT_KIND_METRE,libsbml.UNIT_KIND_METER) )
    self.assertEqual( 0, libsbml.UnitKind_equals(libsbml.UNIT_KIND_AMPERE,libsbml.UNIT_KIND_WEBER) )
    pass  

  def test_UnitKind_forName(self):
    self.assert_( libsbml.UnitKind_forName("ampere") == libsbml.UNIT_KIND_AMPERE )
    self.assert_( libsbml.UnitKind_forName("becquerel") == libsbml.UNIT_KIND_BECQUEREL )
    self.assert_( libsbml.UnitKind_forName("candela") == libsbml.UNIT_KIND_CANDELA )
    self.assert_( libsbml.UnitKind_forName("Celsius") == libsbml.UNIT_KIND_CELSIUS )
    self.assert_( libsbml.UnitKind_forName("coulomb") == libsbml.UNIT_KIND_COULOMB )
    self.assert_( libsbml.UnitKind_forName("dimensionless") == libsbml.UNIT_KIND_DIMENSIONLESS )
    self.assert_( libsbml.UnitKind_forName("farad") == libsbml.UNIT_KIND_FARAD )
    self.assert_( libsbml.UnitKind_forName("gram") == libsbml.UNIT_KIND_GRAM )
    self.assert_( libsbml.UnitKind_forName("gray") == libsbml.UNIT_KIND_GRAY )
    self.assert_( libsbml.UnitKind_forName("henry") == libsbml.UNIT_KIND_HENRY )
    self.assert_( libsbml.UnitKind_forName("hertz") == libsbml.UNIT_KIND_HERTZ )
    self.assert_( libsbml.UnitKind_forName("item") == libsbml.UNIT_KIND_ITEM )
    self.assert_( libsbml.UnitKind_forName("joule") == libsbml.UNIT_KIND_JOULE )
    self.assert_( libsbml.UnitKind_forName("katal") == libsbml.UNIT_KIND_KATAL )
    self.assert_( libsbml.UnitKind_forName("kelvin") == libsbml.UNIT_KIND_KELVIN )
    self.assert_( libsbml.UnitKind_forName("kilogram") == libsbml.UNIT_KIND_KILOGRAM )
    self.assert_( libsbml.UnitKind_forName("liter") == libsbml.UNIT_KIND_LITER )
    self.assert_( libsbml.UnitKind_forName("litre") == libsbml.UNIT_KIND_LITRE )
    self.assert_( libsbml.UnitKind_forName("lumen") == libsbml.UNIT_KIND_LUMEN )
    self.assert_( libsbml.UnitKind_forName("lux") == libsbml.UNIT_KIND_LUX )
    self.assert_( libsbml.UnitKind_forName("meter") == libsbml.UNIT_KIND_METER )
    self.assert_( libsbml.UnitKind_forName("metre") == libsbml.UNIT_KIND_METRE )
    self.assert_( libsbml.UnitKind_forName("mole") == libsbml.UNIT_KIND_MOLE )
    self.assert_( libsbml.UnitKind_forName("newton") == libsbml.UNIT_KIND_NEWTON )
    self.assert_( libsbml.UnitKind_forName("ohm") == libsbml.UNIT_KIND_OHM )
    self.assert_( libsbml.UnitKind_forName("pascal") == libsbml.UNIT_KIND_PASCAL )
    self.assert_( libsbml.UnitKind_forName("radian") == libsbml.UNIT_KIND_RADIAN )
    self.assert_( libsbml.UnitKind_forName("second") == libsbml.UNIT_KIND_SECOND )
    self.assert_( libsbml.UnitKind_forName("siemens") == libsbml.UNIT_KIND_SIEMENS )
    self.assert_( libsbml.UnitKind_forName("sievert") == libsbml.UNIT_KIND_SIEVERT )
    self.assert_( libsbml.UnitKind_forName("steradian") == libsbml.UNIT_KIND_STERADIAN )
    self.assert_( libsbml.UnitKind_forName("tesla") == libsbml.UNIT_KIND_TESLA )
    self.assert_( libsbml.UnitKind_forName("volt") == libsbml.UNIT_KIND_VOLT )
    self.assert_( libsbml.UnitKind_forName("watt") == libsbml.UNIT_KIND_WATT )
    self.assert_( libsbml.UnitKind_forName("weber") == libsbml.UNIT_KIND_WEBER )
    self.assert_( libsbml.UnitKind_forName(None) == libsbml.UNIT_KIND_INVALID )
    self.assert_( libsbml.UnitKind_forName("") == libsbml.UNIT_KIND_INVALID )
    self.assert_( libsbml.UnitKind_forName("foobar") == libsbml.UNIT_KIND_INVALID )
    pass  

  def test_UnitKind_isValidUnitKindString(self):
    self.assertEqual( 0, libsbml.UnitKind_isValidUnitKindString("fun-foam-unit for kids!",1,1) )
    self.assertEqual( 1, libsbml.UnitKind_isValidUnitKindString("litre",2,2) )
    self.assertEqual( 0, libsbml.UnitKind_isValidUnitKindString("liter",2,2) )
    self.assertEqual( 1, libsbml.UnitKind_isValidUnitKindString("liter",1,2) )
    self.assertEqual( 0, libsbml.UnitKind_isValidUnitKindString("meter",2,3) )
    self.assertEqual( 1, libsbml.UnitKind_isValidUnitKindString("metre",2,1) )
    self.assertEqual( 1, libsbml.UnitKind_isValidUnitKindString("meter",1,2) )
    self.assertEqual( 1, libsbml.UnitKind_isValidUnitKindString("Celsius",2,1) )
    self.assertEqual( 0, libsbml.UnitKind_isValidUnitKindString("Celsius",2,2) )
    pass  

  def test_UnitKind_toString(self):
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_AMPERE)
    self.assert_((  "ampere" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_BECQUEREL)
    self.assert_((  "becquerel" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_CANDELA)
    self.assert_((  "candela" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_CELSIUS)
    self.assert_((  "Celsius" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_COULOMB)
    self.assert_((  "coulomb" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_DIMENSIONLESS)
    self.assert_((  "dimensionless" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_FARAD)
    self.assert_((  "farad" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_GRAM)
    self.assert_((  "gram" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_GRAY)
    self.assert_((  "gray" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_HENRY)
    self.assert_((  "henry" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_HERTZ)
    self.assert_((  "hertz" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_ITEM)
    self.assert_((  "item" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_JOULE)
    self.assert_((  "joule" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_KATAL)
    self.assert_((  "katal" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_KELVIN)
    self.assert_((  "kelvin" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_KILOGRAM)
    self.assert_((  "kilogram" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_LITER)
    self.assert_((  "liter" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_LITRE)
    self.assert_((  "litre" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_LUMEN)
    self.assert_((  "lumen" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_LUX)
    self.assert_((  "lux" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_METER)
    self.assert_((  "meter" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_METRE)
    self.assert_((  "metre" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_MOLE)
    self.assert_((  "mole" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_NEWTON)
    self.assert_((  "newton" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_OHM)
    self.assert_((  "ohm" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_PASCAL)
    self.assert_((  "pascal" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_RADIAN)
    self.assert_((  "radian" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_SECOND)
    self.assert_((  "second" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_SIEMENS)
    self.assert_((  "siemens" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_SIEVERT)
    self.assert_((  "sievert" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_STERADIAN)
    self.assert_((  "steradian" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_TESLA)
    self.assert_((  "tesla" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_VOLT)
    self.assert_((  "volt" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_WATT)
    self.assert_((  "watt" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_WEBER)
    self.assert_((  "weber" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_INVALID)
    self.assert_((  "(Invalid UnitKind)" == s ))
    s = libsbml.UnitKind_toString(-1)
    self.assert_((  "(Invalid UnitKind)" == s ))
    s = libsbml.UnitKind_toString(libsbml.UNIT_KIND_INVALID + 1)
    self.assert_((  "(Invalid UnitKind)" == s ))
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestUnitKind))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
