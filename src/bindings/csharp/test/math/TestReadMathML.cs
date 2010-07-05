/// 
///  @file    TestReadMathML.cs
///  @brief   Read MathML unit tests
///  @author  Frank Bergmann (Csharp conversion)
///  @author  Akiya Jouraku (Csharp conversion)
///  @author  Ben Bornstein 
/// 
///  $Id$
///  $HeadURL$
/// 
///  This test file was converted from src/sbml/test/TestReadMathML.cpp
///  with the help of conversion sciprt (ctest_converter.pl).
/// 
/// <!---------------------------------------------------------------------------
///  This file is part of libSBML.  Please visit http://sbml.org for more
///  information about SBML, and the latest version of libSBML.
/// 
///  Copyright 2005-2010 California Institute of Technology.
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

  public class TestReadMathML {
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

    private string F;
    private ASTNode N;

    public string MATHML_FOOTER()
    {
      return "</math>";
    }

    public string MATHML_HEADER()
    {
      return "<math xmlns='http://www.w3.org/1998/Math/MathML'>\n";
    }

    public string XML_HEADER()
    {
      return "<?xml version='1.0' encoding='UTF-8'?>\n";
    }

    public bool isnan(double x)
    {
      return (x != x);
    }

    public string wrapMathML(string s)
    {
      string r = XML_HEADER();
      r += MATHML_HEADER();
      r += s;
      r += MATHML_FOOTER();
      return r;
    }

    public string wrapXML(string s)
    {
      string r = XML_HEADER();
      r += s;
      return r;
    }

  public bool util_isInf(double x)
  {
    return ( (x == util_PosInf()) ||  (x == util_NegInf()) );
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

    public void setUp()
    {
      N = null;
      F = null;
    }

    public void tearDown()
    {
      F = null;
    }

    public void test_element_abs()
    {
      string s = wrapMathML("<apply><abs/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "abs(x)" == F ));
    }

    public void test_element_and()
    {
      string s = wrapMathML("<apply> <and/> <ci>a</ci> <ci>b</ci> <ci>c</ci> </apply>"  
    );
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "and(a, b, c)" == F ));
    }

    public void test_element_arccos()
    {
      string s = wrapMathML("<apply><arccos/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "acos(x)" == F ));
    }

    public void test_element_arccosh()
    {
      string s = wrapMathML("<apply><arccosh/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "arccosh(x)" == F ));
    }

    public void test_element_arccot()
    {
      string s = wrapMathML("<apply><arccot/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "arccot(x)" == F ));
    }

    public void test_element_arccoth()
    {
      string s = wrapMathML("<apply><arccoth/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "arccoth(x)" == F ));
    }

    public void test_element_arccsc()
    {
      string s = wrapMathML("<apply><arccsc/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "arccsc(x)" == F ));
    }

    public void test_element_arccsch()
    {
      string s = wrapMathML("<apply><arccsch/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "arccsch(x)" == F ));
    }

    public void test_element_arcsec()
    {
      string s = wrapMathML("<apply><arcsec/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "arcsec(x)" == F ));
    }

    public void test_element_arcsech()
    {
      string s = wrapMathML("<apply><arcsech/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "arcsech(x)" == F ));
    }

    public void test_element_arcsin()
    {
      string s = wrapMathML("<apply><arcsin/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "asin(x)" == F ));
    }

    public void test_element_arcsinh()
    {
      string s = wrapMathML("<apply><arcsinh/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "arcsinh(x)" == F ));
    }

    public void test_element_arctan()
    {
      string s = wrapMathML("<apply><arctan/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "atan(x)" == F ));
    }

    public void test_element_arctanh()
    {
      string s = wrapMathML("<apply><arctanh/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "arctanh(x)" == F ));
    }

    public void test_element_bug_apply_ci_1()
    {
      string s = wrapMathML("<apply>" + 
    "  <ci> Y </ci>" + 
    "  <cn> 1 </cn>" + 
    "</apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_FUNCTION );
      assertTrue((  "Y" == N.getName() ));
      assertTrue( N.getNumChildren() == 1 );
      ASTNode c = N.getLeftChild();
      assertTrue( c != null );
      assertTrue( c.getType() == libsbml.AST_REAL );
      assertTrue( c.getReal() == 1 );
      assertTrue( c.getNumChildren() == 0 );
    }

    public void test_element_bug_apply_ci_2()
    {
      string s = wrapMathML("<apply>" + 
    "  <ci> Y </ci>" + 
    "  <csymbol encoding='text' " + 
    "   definitionURL='http://www.sbml.org/sbml/symbols/time'> t </csymbol>" + 
    "</apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_FUNCTION );
      assertTrue((  "Y" == N.getName() ));
      assertTrue( N.getNumChildren() == 1 );
      ASTNode c = N.getLeftChild();
      assertTrue( c != null );
      assertTrue( c.getType() == libsbml.AST_NAME_TIME );
      assertTrue((  "t" == c.getName() ));
      assertTrue( c.getNumChildren() == 0 );
    }

    public void test_element_bug_cn_e_notation_1()
    {
      string s = wrapMathML("<cn type='e-notation'> 2 <sep/> -8 </cn>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_REAL_E );
      assertTrue( N.getMantissa() == 2.0 );
      assertTrue( N.getExponent() == -8.0 );
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_bug_cn_e_notation_2()
    {
      string s = wrapMathML("<cn type='e-notation'> -3 <sep/> 4 </cn>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_REAL_E );
      assertTrue( N.getMantissa() == -3.0 );
      assertTrue( N.getExponent() == 4.0 );
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_bug_cn_e_notation_3()
    {
      string s = wrapMathML("<cn type='e-notation'> -6 <sep/> -1 </cn>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_REAL_E );
      assertTrue( N.getMantissa() == -6.0 );
      assertTrue( N.getExponent() == -1.0 );
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_bug_cn_integer_negative()
    {
      string s = wrapMathML("<cn type='integer'> -7 </cn>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_INTEGER );
      assertTrue( N.getInteger() == -7 );
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_bug_csymbol_1()
    {
      string s = wrapMathML("<apply>" + 
    "  <gt/>" + 
    "  <csymbol encoding='text' " + 
    "    definitionURL='http://www.sbml.org/sbml/symbols/time'>time</csymbol>" + 
    "  <cn>5000</cn>" + 
    "</apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_RELATIONAL_GT );
      assertTrue( N.getNumChildren() == 2 );
      ASTNode c = N.getLeftChild();
      assertTrue( c != null );
      assertTrue( c.getType() == libsbml.AST_NAME_TIME );
      assertTrue((  "time" == c.getName() ));
      assertTrue( c.getNumChildren() == 0 );
      c = N.getRightChild();
      assertTrue( c != null );
      assertTrue( c.getType() == libsbml.AST_REAL );
      assertTrue( c.getReal() == 5000 );
      assertTrue( c.getNumChildren() == 0 );
    }

    public void test_element_bug_csymbol_delay_1()
    {
      string s = wrapMathML("<apply>" + 
    "  <csymbol encoding='text' definitionURL='http://www.sbml.org/sbml/" + 
    "symbols/delay'> my_delay </csymbol>" + 
    "  <ci> x </ci>" + 
    "  <cn> 0.1 </cn>" + 
    "</apply>\n");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_FUNCTION_DELAY );
      assertTrue((  "my_delay" == N.getName() ));
      assertTrue( N.getNumChildren() == 2 );
      ASTNode c = N.getLeftChild();
      assertTrue( c != null );
      assertTrue( c.getType() == libsbml.AST_NAME );
      assertTrue((  "x" == c.getName() ));
      assertTrue( c.getNumChildren() == 0 );
      c = N.getRightChild();
      assertTrue( c != null );
      assertTrue( c.getType() == libsbml.AST_REAL );
      assertTrue( c.getReal() == 0.1 );
      assertTrue( c.getNumChildren() == 0 );
    }

    public void test_element_bug_math_xmlns()
    {
      string s = wrapXML("<foo:math xmlns:foo='http://www.w3.org/1998/Math/MathML'>" + 
    "  <foo:apply>" + 
    "    <foo:plus/> <foo:cn>1</foo:cn> <foo:cn>2</foo:cn>" + 
    "  </foo:apply>" + 
    "</foo:math>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "1 + 2" == F ));
    }

    public void test_element_ceiling()
    {
      string s = wrapMathML("<apply><ceiling/><cn> 1.6 </cn></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "ceil(1.6)" == F ));
    }

    public void test_element_ci()
    {
      string s = wrapMathML("<ci> x </ci>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_NAME );
      assertTrue((  "x" == N.getName() ));
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_ci_surrounding_spaces_bug()
    {
      string s = wrapMathML("  <ci> s </ci>  ");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_NAME );
      assertTrue((  "s" == N.getName() ));
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_cn_default()
    {
      string s = wrapMathML("<cn> 12345.7 </cn>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_REAL );
      assertTrue( N.getReal() == 12345.7 );
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_cn_e_notation()
    {
      string s = wrapMathML("<cn type='e-notation'> 12.3 <sep/> 5 </cn>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_REAL_E );
      assertTrue( N.getMantissa() == 12.3 );
      assertTrue( N.getExponent() == 5 );
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_cn_integer()
    {
      string s = wrapMathML("<cn type='integer'> 12345 </cn>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_INTEGER );
      assertTrue( N.getInteger() == 12345 );
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_cn_rational()
    {
      string s = wrapMathML("<cn type='rational'> 12342 <sep/> 2342342 </cn>"  
    );
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_RATIONAL );
      assertTrue( N.getNumerator() == 12342 );
      assertTrue( N.getDenominator() == 2342342 );
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_cn_real()
    {
      string s = wrapMathML("<cn type='real'> 12345.7 </cn>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_REAL );
      assertTrue( N.getReal() == 12345.7 );
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_constants_exponentiale()
    {
      string s = wrapMathML("<exponentiale/>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_CONSTANT_E );
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_constants_false()
    {
      string s = wrapMathML("<false/>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_CONSTANT_FALSE );
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_constants_infinity()
    {
      string s = wrapMathML("<infinity/>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_REAL );
      assertTrue( util_isInf(N.getReal()) == true );
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_constants_notanumber()
    {
      string s = wrapMathML("<notanumber/>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_REAL );
      assertEquals( true, isnan(N.getReal()) );
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_constants_pi()
    {
      string s = wrapMathML("<pi/>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_CONSTANT_PI );
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_constants_true()
    {
      string s = wrapMathML("<true/>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_CONSTANT_TRUE );
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_cos()
    {
      string s = wrapMathML("<apply><cos/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "cos(x)" == F ));
    }

    public void test_element_cosh()
    {
      string s = wrapMathML("<apply><cosh/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "cosh(x)" == F ));
    }

    public void test_element_cot()
    {
      string s = wrapMathML("<apply><cot/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "cot(x)" == F ));
    }

    public void test_element_coth()
    {
      string s = wrapMathML("<apply><coth/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "coth(x)" == F ));
    }

    public void test_element_csc()
    {
      string s = wrapMathML("<apply><csc/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "csc(x)" == F ));
    }

    public void test_element_csch()
    {
      string s = wrapMathML("<apply><csch/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "csch(x)" == F ));
    }

    public void test_element_csymbol_delay_1()
    {
      string s = wrapMathML("<csymbol encoding='text' " + "definitionURL='http://www.sbml.org/sbml/symbols/delay'> delay </csymbol>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_FUNCTION_DELAY );
      assertTrue((  "delay" == N.getName() ));
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_csymbol_delay_2()
    {
      string s = wrapMathML("<apply>" + 
    "  <csymbol encoding='text' definitionURL='http://www.sbml.org/sbml/" + 
    "symbols/delay'> my_delay </csymbol>" + 
    "  <ci> x </ci>" + 
    "  <cn> 0.1 </cn>" + 
    "</apply>\n");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "my_delay(x, 0.1)" == F ));
    }

    public void test_element_csymbol_delay_3()
    {
      string s = wrapMathML("<apply>" + 
    "  <power/>" + 
    "  <apply>" + 
    "    <csymbol encoding='text' definitionURL='http://www.sbml.org/sbml/" + 
    "symbols/delay'> delay </csymbol>" + 
    "    <ci> P </ci>" + 
    "    <ci> delta_t </ci>" + 
    "  </apply>\n" + 
    "  <ci> q </ci>" + 
    "</apply>\n");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "pow(delay(P, delta_t), q)" == F ));
    }

    public void test_element_csymbol_time()
    {
      string s = wrapMathML("<csymbol encoding='text' " + "definitionURL='http://www.sbml.org/sbml/symbols/time'> t </csymbol>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_NAME_TIME );
      assertTrue((  "t" == N.getName() ));
      assertTrue( N.getNumChildren() == 0 );
    }

    public void test_element_eq()
    {
      string s = wrapMathML("<apply> <eq/> <ci>a</ci> <ci>b</ci> <ci>c</ci> </apply>"  
    );
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "eq(a, b, c)" == F ));
    }

    public void test_element_exp()
    {
      string s = wrapMathML("<apply><exp/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "exp(x)" == F ));
    }

    public void test_element_factorial()
    {
      string s = wrapMathML("<apply><factorial/><cn> 5 </cn></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "factorial(5)" == F ));
    }

    public void test_element_floor()
    {
      string s = wrapMathML("<apply><floor/><cn> 1.2 </cn></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "floor(1.2)" == F ));
    }

    public void test_element_function_call_1()
    {
      string s = wrapMathML("<apply> <ci> foo </ci> <ci> x </ci> </apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "foo(x)" == F ));
    }

    public void test_element_function_call_2()
    {
      string s = wrapMathML("<apply> <plus/> <cn> 1 </cn>" + 
    "                <apply> <ci> f </ci> <ci> x </ci> </apply>" + 
    "</apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "1 + f(x)" == F ));
    }

    public void test_element_geq()
    {
      string s = wrapMathML("<apply> <geq/> <cn>1</cn> <ci>x</ci> <cn>0</cn> </apply>"  
    );
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "geq(1, x, 0)" == F ));
    }

    public void test_element_gt()
    {
      string s = wrapMathML("<apply> <gt/> <infinity/>" + 
    "              <apply> <minus/> <infinity/> <cn>1</cn> </apply>" + 
    "</apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "gt(INF, INF - 1)" == F ));
    }

    public void test_element_invalid_mathml()
    {
        string invalid = wrapMathML("<lambda definitionURL=\"http://biomodels.net/SBO/#SBO:0000065\">" + 
    "<bvar>" + 
    "<ci>c</ci>" + 
    "</bvar>" + 
    "<apply>" + 
    "  <ci>c</ci>" + 
    "</apply>" + 
    "</lambda>\n");
      N = libsbml.readMathMLFromString(null);
      assertTrue( N == null );
      N = libsbml.readMathMLFromString(invalid);
      assertTrue( N == null );
    }

    public void test_element_lambda()
    {
      string s = wrapMathML("<lambda>" + 
    "  <bvar> <ci>x</ci> </bvar>" + 
    "  <apply> <sin/>" + 
    "          <apply> <plus/> <ci>x</ci> <cn>1</cn> </apply>" + 
    "  </apply>" + 
    "</lambda>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "lambda(x, sin(x + 1))" == F ));
    }

    public void test_element_leq()
    {
      string s = wrapMathML("<apply> <leq/> <cn>0</cn> <ci>x</ci> <cn>1</cn> </apply>"  
    );
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "leq(0, x, 1)" == F ));
    }

    public void test_element_ln()
    {
      string s = wrapMathML("<apply><ln/><ci> a </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "log(a)" == F ));
    }

    public void test_element_log_1()
    {
      string s = wrapMathML("<apply> <log/> <logbase> <cn type='integer'> 3 </cn> </logbase>" + 
    "               <ci> x </ci>" + 
    "</apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "log(3, x)" == F ));
    }

    public void test_element_log_2()
    {
      string s = wrapMathML("<apply> <log/> <ci> x </ci> </apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "log10(x)" == F ));
    }

    public void test_element_lt()
    {
      string s = wrapMathML("<apply> <lt/> <apply> <minus/> <infinity/> <infinity/> </apply>" + 
    "              <cn>1</cn>" + 
    "</apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "lt(INF - INF, 1)" == F ));
    }

    public void test_element_math()
    {
      string s = wrapXML("<math xmlns='http://www.w3.org/1998/Math/MathML'/>"  
    );
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      assertTrue( N.getType() == libsbml.AST_UNKNOWN );
    }

    public void test_element_neq()
    {
      string s = wrapMathML("<apply> <neq/> <notanumber/> <notanumber/> </apply>"  
    );
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "neq(NaN, NaN)" == F ));
    }

    public void test_element_not()
    {
      string s = wrapMathML("<apply> <not/> <ci> TooShabby </ci> </apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "not(TooShabby)" == F ));
    }

    public void test_element_operator_plus()
    {
      string s = wrapMathML("<apply> <plus/> <cn> 1 </cn> <cn> 2 </cn> <cn> 3 </cn> </apply>"  
    );
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "1 + 2 + 3" == F ));
    }

    public void test_element_operator_times()
    {
      string s = wrapMathML("<apply> <times/> <ci> x </ci> <ci> y </ci> <ci> z </ci> </apply>"  
    );
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "x * y * z" == F ));
    }

    public void test_element_or()
    {
      string s = wrapMathML("<apply> <or/> <ci>a</ci> <ci>b</ci> <ci>c</ci> <ci>d</ci> </apply>"  
    );
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "or(a, b, c, d)" == F ));
    }

    public void test_element_piecewise()
    {
      string s = wrapMathML("<piecewise>" + 
    "  <piece>" + 
    "    <apply> <minus/> <ci>x</ci> </apply>" + 
    "    <apply> <lt/> <ci>x</ci> <cn>0</cn> </apply>" + 
    "  </piece>" + 
    "  <piece>" + 
    "    <cn>0</cn>" + 
    "    <apply> <eq/> <ci>x</ci> <cn>0</cn> </apply>" + 
    "  </piece>" + 
    "  <piece>" + 
    "    <ci>x</ci>" + 
    "    <apply> <gt/> <ci>x</ci> <cn>0</cn> </apply>" + 
    "  </piece>" + 
    "</piecewise>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "piecewise(-x, lt(x, 0), 0, eq(x, 0), x, gt(x, 0))" == F ));
    }

    public void test_element_piecewise_otherwise()
    {
      string s = wrapMathML("<piecewise>" + 
    "  <piece>" + 
    "    <cn>0</cn>" + 
    "    <apply> <lt/> <ci>x</ci> <cn>0</cn> </apply>" + 
    "  </piece>" + 
    "  <otherwise>" + 
    "    <ci>x</ci>" + 
    "  </otherwise>" + 
    "</piecewise>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "piecewise(0, lt(x, 0), x)" == F ));
    }

    public void test_element_power()
    {
      string s = wrapMathML("<apply><power/> <ci>x</ci> <cn>3</cn> </apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "pow(x, 3)" == F ));
    }

    public void test_element_root_1()
    {
      string s = wrapMathML("<apply> <root/> <degree> <cn type='integer'> 3 </cn> </degree>" + 
    "               <ci> a </ci>" + 
    "</apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "root(3, a)" == F ));
    }

    public void test_element_root_2()
    {
      string s = wrapMathML("<apply> <root/> <ci> a </ci> </apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "sqrt(a)" == F ));
    }

    public void test_element_sec()
    {
      string s = wrapMathML("<apply><sec/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "sec(x)" == F ));
    }

    public void test_element_sech()
    {
      string s = wrapMathML("<apply><sech/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "sech(x)" == F ));
    }

    public void test_element_sin()
    {
      string s = wrapMathML("<apply><sin/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "sin(x)" == F ));
    }

    public void test_element_sinh()
    {
      string s = wrapMathML("<apply><sinh/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "sinh(x)" == F ));
    }

    public void test_element_tan()
    {
      string s = wrapMathML("<apply><tan/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "tan(x)" == F ));
    }

    public void test_element_tanh()
    {
      string s = wrapMathML("<apply><tanh/><ci> x </ci></apply>");
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "tanh(x)" == F ));
    }

    public void test_element_xor()
    {
      string s = wrapMathML("<apply> <xor/> <ci>a</ci> <ci>b</ci> <ci>b</ci> <ci>a</ci> </apply>"  
    );
      N = libsbml.readMathMLFromString(s);
      assertTrue( N != null );
      F = libsbml.formulaToString(N);
      assertTrue((  "xor(a, b, b, a)" == F ));
    }

  }
}
