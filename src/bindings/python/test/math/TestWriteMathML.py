#
# @file    TestWriteMathML.py
# @brief   Write MathML unit tests
#
# @author  Akiya Jouraku (Python conversion)
# @author  Ben Bornstein 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestWriteMathML.cpp
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

def util_NaN():
  z = 1e300
  z = z * z

  return z - z

def util_PosInf():
  z = 1e300
  z = z * z

  return z

def util_NegInf():
  z = 1e300
  z = z * z

  return -z 

def MATHML_FOOTER():
  return "</math>"
  pass

def MATHML_HEADER():
  return "<math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n"
  pass

def XML_HEADER():
  return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
  pass

def wrapMathML(s):
  r = XML_HEADER()
  r += MATHML_HEADER()
  r += s
  r += MATHML_FOOTER()
  return r
  pass

class TestWriteMathML(unittest.TestCase):

  S = None
  N = None

  def equals(self, *x):
    if len(x) == 2:
      return x[0] == x[1]
    elif len(x) == 1:
      return x[0] == self.OSS.str()

  def setUp(self):
    self.N = 0
    self.S = 0
    pass  

  def tearDown(self):
    self.N = None
    self.S = None
    pass  

  def test_MathMLFormatter_ci(self):
    expected = wrapMathML("  <ci> foo </ci>\n")
    self.N = libsbml.parseFormula("foo")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_cn_e_notation_1(self):
    expected = wrapMathML("  <cn type=\"e-notation\"> 0 <sep/> 3 </cn>\n"  
    )
    self.N = libsbml.parseFormula("0e3")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_cn_e_notation_2(self):
    expected = wrapMathML("  <cn type=\"e-notation\"> 2 <sep/> 3 </cn>\n"  
    )
    self.N = libsbml.parseFormula("2e3")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_cn_e_notation_3(self):
    expected = wrapMathML("  <cn type=\"e-notation\"> 1234567.8 <sep/> 3 </cn>\n"  
    )
    self.N = libsbml.parseFormula("1234567.8e3")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_cn_e_notation_4(self):
    expected = wrapMathML("  <cn type=\"e-notation\"> 6.0221367 <sep/> 23 </cn>\n"  
    )
    self.N = libsbml.parseFormula("6.0221367e+23")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_cn_e_notation_5(self):
    expected = wrapMathML("  <cn type=\"e-notation\"> 4 <sep/> -6 </cn>\n"  
    )
    self.N = libsbml.parseFormula(".000004")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_cn_e_notation_6(self):
    expected = wrapMathML("  <cn type=\"e-notation\"> 4 <sep/> -12 </cn>\n"  
    )
    self.N = libsbml.parseFormula(".000004e-6")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_cn_e_notation_7(self):
    expected = wrapMathML("  <cn type=\"e-notation\"> -1 <sep/> -6 </cn>\n"  
    )
    self.N = libsbml.parseFormula("-1e-6")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_cn_integer(self):
    expected = wrapMathML("  <cn type=\"integer\"> 5 </cn>\n")
    self.N = libsbml.parseFormula("5")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_cn_rational(self):
    expected = wrapMathML("  <cn type=\"rational\"> 1 <sep/> 3 </cn>\n"  
    )
    self.N = libsbml.ASTNode()
    self.N.setValue(1,3)
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_cn_real_1(self):
    expected = wrapMathML("  <cn> 1.2 </cn>\n")
    self.N = libsbml.parseFormula("1.2")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_cn_real_2(self):
    expected = wrapMathML("  <cn> 1234567.8 </cn>\n")
    self.N = libsbml.parseFormula("1234567.8")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_cn_real_3(self):
    expected = wrapMathML("  <cn> -3.14 </cn>\n")
    self.N = libsbml.parseFormula("-3.14")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_cn_real_locale(self):
    expected = wrapMathML("  <cn> 2.72 </cn>\n")
    self.N = libsbml.parseFormula("2.72")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_constant_exponentiale(self):
    expected = wrapMathML("  <exponentiale/>\n")
    self.N = libsbml.ASTNode(libsbml.AST_CONSTANT_E)
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_constant_false(self):
    expected = wrapMathML("  <false/>\n")
    self.N = libsbml.ASTNode(libsbml.AST_CONSTANT_FALSE)
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_constant_infinity(self):
    expected = wrapMathML("  <infinity/>\n")
    self.N = libsbml.ASTNode()
    self.N.setValue( util_PosInf() )
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_constant_infinity_neg(self):
    expected = wrapMathML("  <apply> <minus/> <infinity/> </apply>\n"  
    )
    self.N = libsbml.ASTNode()
    self.N.setValue(- util_PosInf())
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_constant_notanumber(self):
    expected = wrapMathML("  <notanumber/>\n")
    self.N = libsbml.ASTNode(libsbml.AST_REAL)
    self.N.setValue( util_NaN() )
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_constant_true(self):
    expected = wrapMathML("  <true/>\n")
    self.N = libsbml.ASTNode(libsbml.AST_CONSTANT_TRUE)
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_csymbol_delay(self):
    expected = wrapMathML("  <apply>\n" + 
    "    <csymbol encoding=\"text\" definitionURL=\"http://www.sbml.org/sbml/" + 
    "symbols/delay\"> my_delay </csymbol>\n" + 
    "    <ci> x </ci>\n" + 
    "    <cn> 0.1 </cn>\n" + 
    "  </apply>\n")
    self.N = libsbml.parseFormula("delay(x, 0.1)")
    self.N.setName("my_delay")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_csymbol_time(self):
    expected = wrapMathML("  <csymbol encoding=\"text\" " + "definitionURL=\"http://www.sbml.org/sbml/symbols/time\"> t </csymbol>\n")
    self.N = libsbml.ASTNode(libsbml.AST_NAME_TIME)
    self.N.setName("t")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_function_1(self):
    expected = wrapMathML("  <apply>\n" + 
    "    <ci> foo </ci>\n" + 
    "    <cn type=\"integer\"> 1 </cn>\n" + 
    "    <cn type=\"integer\"> 2 </cn>\n" + 
    "    <cn type=\"integer\"> 3 </cn>\n" + 
    "  </apply>\n")
    self.N = libsbml.parseFormula("foo(1, 2, 3)")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_function_2(self):
    expected = wrapMathML("  <apply>\n" + 
    "    <ci> foo </ci>\n" + 
    "    <cn type=\"integer\"> 1 </cn>\n" + 
    "    <cn type=\"integer\"> 2 </cn>\n" + 
    "    <apply>\n" + 
    "      <ci> bar </ci>\n" + 
    "      <ci> z </ci>\n" + 
    "    </apply>\n" + 
    "  </apply>\n")
    self.N = libsbml.parseFormula("foo(1, 2, bar(z))")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_lambda(self):
    expected = wrapMathML("  <lambda>\n" + 
    "    <bvar>\n" + 
    "      <ci> x </ci>\n" + 
    "    </bvar>\n" + 
    "    <bvar>\n" + 
    "      <ci> y </ci>\n" + 
    "    </bvar>\n" + 
    "    <apply>\n" + 
    "      <root/>\n" + 
    "      <degree>\n" + 
    "        <cn type=\"integer\"> 2 </cn>\n" + 
    "      </degree>\n" + 
    "      <apply>\n" + 
    "        <plus/>\n" + 
    "        <apply>\n" + 
    "          <power/>\n" + 
    "          <ci> x </ci>\n" + 
    "          <cn type=\"integer\"> 2 </cn>\n" + 
    "        </apply>\n" + 
    "        <apply>\n" + 
    "          <power/>\n" + 
    "          <ci> y </ci>\n" + 
    "          <cn type=\"integer\"> 2 </cn>\n" + 
    "        </apply>\n" + 
    "      </apply>\n" + 
    "    </apply>\n" + 
    "  </lambda>\n")
    self.N = libsbml.parseFormula("lambda(x, y, root(2, x^2 + y^2))")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_lambda_no_bvars(self):
    expected = wrapMathML("  <lambda>\n" + 
    "    <apply>\n" + 
    "      <plus/>\n" + 
    "      <cn type=\"integer\"> 2 </cn>\n" + 
    "      <cn type=\"integer\"> 2 </cn>\n" + 
    "    </apply>\n" + 
    "  </lambda>\n")
    self.N = libsbml.parseFormula("lambda(2 + 2)")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_log(self):
    expected = wrapMathML("  <apply>\n" + 
    "    <log/>\n" + 
    "    <logbase>\n" + 
    "      <cn type=\"integer\"> 2 </cn>\n" + 
    "    </logbase>\n" + 
    "    <ci> N </ci>\n" + 
    "  </apply>\n")
    self.N = libsbml.parseFormula("log(2, N)")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_minus(self):
    expected = wrapMathML("  <apply>\n" + 
    "    <minus/>\n" + 
    "    <cn type=\"integer\"> 1 </cn>\n" + 
    "    <cn type=\"integer\"> 2 </cn>\n" + 
    "  </apply>\n")
    self.N = libsbml.parseFormula("1 - 2")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_minus_unary_1(self):
    expected = wrapMathML("  <cn type=\"integer\"> -2 </cn>\n"  
    )
    self.N = libsbml.parseFormula("-2")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_minus_unary_2(self):
    expected = wrapMathML("  <apply>\n" + 
    "    <minus/>\n" + 
    "    <ci> a </ci>\n" + 
    "  </apply>\n")
    self.N = libsbml.parseFormula("-a")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_piecewise(self):
    expected = wrapMathML("  <piecewise>\n" + 
    "    <piece>\n" + 
    "      <apply>\n" + 
    "        <minus/>\n" + 
    "        <ci> x </ci>\n" + 
    "      </apply>\n" + 
    "      <apply>\n" + 
    "        <lt/>\n" + 
    "        <ci> x </ci>\n" + 
    "        <cn type=\"integer\"> 0 </cn>\n" + 
    "      </apply>\n" + 
    "    </piece>\n" + 
    "    <piece>\n" + 
    "      <cn type=\"integer\"> 0 </cn>\n" + 
    "      <apply>\n" + 
    "        <eq/>\n" + 
    "        <ci> x </ci>\n"  + 
    "        <cn type=\"integer\"> 0 </cn>\n" + 
    "      </apply>\n" + 
    "    </piece>\n" + 
    "    <piece>\n" + 
    "      <ci> x </ci>\n" + 
    "      <apply>\n" + 
    "        <gt/>\n" + 
    "        <ci> x </ci>\n"  + 
    "        <cn type=\"integer\"> 0 </cn>\n" + 
    "      </apply>\n" + 
    "    </piece>\n" + 
    "  </piecewise>\n")
    f =  "piecewise(-x, lt(x, 0), 0, eq(x, 0), x, gt(x, 0))";
    self.N = libsbml.parseFormula(f)
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_piecewise_otherwise(self):
    expected = wrapMathML("  <piecewise>\n" + 
    "    <piece>\n" + 
    "      <cn type=\"integer\"> 0 </cn>\n" + 
    "      <apply>\n" + 
    "        <lt/>\n" + 
    "        <ci> x </ci>\n" + 
    "        <cn type=\"integer\"> 0 </cn>\n" + 
    "      </apply>\n" + 
    "    </piece>\n" + 
    "    <otherwise>\n" + 
    "      <ci> x </ci>\n"  + 
    "    </otherwise>\n" + 
    "  </piecewise>\n")
    self.N = libsbml.parseFormula("piecewise(0, lt(x, 0), x)")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_plus_binary(self):
    expected = wrapMathML("  <apply>\n" + 
    "    <plus/>\n" + 
    "    <cn type=\"integer\"> 1 </cn>\n" + 
    "    <cn type=\"integer\"> 2 </cn>\n" + 
    "  </apply>\n")
    self.N = libsbml.parseFormula("1 + 2")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_plus_nary_1(self):
    expected = wrapMathML("  <apply>\n" + 
    "    <plus/>\n" + 
    "    <cn type=\"integer\"> 1 </cn>\n" + 
    "    <cn type=\"integer\"> 2 </cn>\n" + 
    "    <cn type=\"integer\"> 3 </cn>\n" + 
    "  </apply>\n")
    self.N = libsbml.parseFormula("1 + 2 + 3")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_plus_nary_2(self):
    expected = wrapMathML("  <apply>\n" + 
    "    <plus/>\n" + 
    "    <cn type=\"integer\"> 1 </cn>\n" + 
    "    <cn type=\"integer\"> 2 </cn>\n" + 
    "    <cn type=\"integer\"> 3 </cn>\n" + 
    "  </apply>\n")
    self.N = libsbml.parseFormula("(1 + 2) + 3")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_plus_nary_3(self):
    expected = wrapMathML("  <apply>\n" + 
    "    <plus/>\n" + 
    "    <cn type=\"integer\"> 1 </cn>\n" + 
    "    <cn type=\"integer\"> 2 </cn>\n" + 
    "    <cn type=\"integer\"> 3 </cn>\n" + 
    "  </apply>\n")
    self.N = libsbml.parseFormula("1 + (2 + 3)")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_plus_nary_4(self):
    expected = wrapMathML("  <apply>\n" + 
    "    <plus/>\n" + 
    "    <cn type=\"integer\"> 1 </cn>\n" + 
    "    <cn type=\"integer\"> 2 </cn>\n" + 
    "    <apply>\n" + 
    "      <times/>\n" + 
    "      <ci> x </ci>\n" + 
    "      <ci> y </ci>\n" + 
    "      <ci> z </ci>\n" + 
    "    </apply>\n" + 
    "    <cn type=\"integer\"> 3 </cn>\n" + 
    "  </apply>\n")
    self.N = libsbml.parseFormula("1 + 2 + x * y * z + 3")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_root(self):
    expected = wrapMathML("  <apply>\n" + 
    "    <root/>\n" + 
    "    <degree>\n" + 
    "      <cn type=\"integer\"> 3 </cn>\n" + 
    "    </degree>\n" + 
    "    <ci> x </ci>\n" + 
    "  </apply>\n")
    self.N = libsbml.parseFormula("root(3, x)")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_MathMLFormatter_sin(self):
    expected = wrapMathML("  <apply>\n" + 
    "    <sin/>\n" + 
    "    <ci> x </ci>\n" + 
    "  </apply>\n")
    self.N = libsbml.parseFormula("sin(x)")
    self.S = libsbml.writeMathMLToString(self.N)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestWriteMathML))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
