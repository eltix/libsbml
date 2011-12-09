/**
 * \file    addingEvidenceCodes_2.cpp
 * \brief   adds evidence codes to a species in a model
 * \author  Sarah Keating
 * 
 * This file is part of libSBML.  Please visit http://sbml.org for more
 * information about SBML, and the latest version of libSBML.
 */

import org.sbml.libsbml.CVTerm;
import org.sbml.libsbml.SBMLDocument;
import org.sbml.libsbml.Species;
import org.sbml.libsbml.XMLAttributes;
import org.sbml.libsbml.XMLNamespaces;
import org.sbml.libsbml.XMLNode;
import org.sbml.libsbml.XMLToken;
import org.sbml.libsbml.XMLTriple;
import org.sbml.libsbml.libsbml;

public class addingEvidenceCodes_2 {
	public static int main(String[] args) {
		System.loadLibrary("sbmlj");

		if (args.length != 2) {
			System.out
					.println("  usage: addingEvidenceCodes_2 <input-filename> <output-filename>");
			System.out
					.println("  Adds controlled vocabulary term to a species");
			System.out.println();
			return 2;
		}

		SBMLDocument d = libsbml.readSBML(args[0]);
		long errors = d.getNumErrors();

		if (errors > 0) {
			System.out.println("Read Error(s):");
			d.printErrors();

			System.out.println("Correct the above and re-run.");
		} else {
			long n = d.getModel().getNumSpecies();

			if (n <= 0) {
				System.out
						.println("Model has no species.\n Cannot add CV terms\n");
			} else {
				Species s = d.getModel().getSpecies(0);

				/*
				 * check that the species has a metaid no CVTerms will be added
				 * if there is no metaid to reference
				 */
				if (!s.isSetMetaId())
					s.setMetaId("metaid_0000052");

				CVTerm cv1 = new CVTerm(libsbml.BIOLOGICAL_QUALIFIER);
				cv1.setBiologicalQualifierType(libsbml.BQB_OCCURS_IN);
				cv1.addResource("urn:miriam:obo.go:GO%3A0005764");

				s.addCVTerm(cv1);

				// now create the additional annotation

				// <rdf:Statement>
				// <rdf:subject rdf:resource="#metaid_0000052"/>
				// <rdf:predicate
				// rdf:resource="http://biomodels.net/biology-qualifiers/occursIn"/>
				// <rdf:object rdf:resource="urn:miriam:obo.go:GO%3A0005764"/>
				// <bqbiol:isDescribedBy>
				// <rdf:Bag>
				// <rdf:li rdf:resource="urn:miriam:obo.eco:ECO%3A0000004"/>
				// <rdf:li rdf:resource="urn:miriam:pubmed:7017716"/>
				// </rdf:Bag>
				// </bqbiol:isDescribedBy>
				// </rdf:Statement>

				/* attributes */
				XMLAttributes blank_att = new XMLAttributes();

				XMLAttributes resource_att = new XMLAttributes();

				/* create the outer statement node */
				XMLTriple statement_triple = new XMLTriple("Statement",
						"http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdf");

				XMLToken statement_token = new XMLToken(statement_triple,
						blank_att);

				XMLNode statement = new XMLNode(statement_token);

				/* create the subject node */
				XMLTriple subject_triple = new XMLTriple("subject",
						"http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdf");

				resource_att.clear();
				resource_att.add("rdf:resource", "#" + s.getMetaId());

				XMLToken subject_token = new XMLToken(subject_triple,
						resource_att);

				XMLNode subject = new XMLNode(subject_token);

				/* create the predicate node */
				XMLTriple predicate_triple = new XMLTriple("predicate",
						"http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdf");

				resource_att.clear();
				resource_att.add("rdf:resource",
						"http://biomodels.net/biology-qualifiers/occursIn");

				XMLToken predicate_token = new XMLToken(predicate_triple,
						resource_att);

				XMLNode predicate = new XMLNode(predicate_token);

				/* create the object node */
				XMLTriple object_triple = new XMLTriple("object",
						"http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdf");

				resource_att.clear();
				resource_att.add("rdf:resource",
						"urn:miriam:obo.go:GO%3A0005764");

				XMLToken object_token = new XMLToken(object_triple,
						resource_att);

				XMLNode object_ = new XMLNode(object_token);

				/* create the bqbiol node */
				XMLTriple bqbiol_triple = new XMLTriple("isDescribedBy",
						"http://biomodels.net/biology-qualifiers/", "bqbiol");

				XMLToken bqbiol_token = new XMLToken(bqbiol_triple, blank_att);

				XMLNode bqbiol = new XMLNode(bqbiol_token);

				/* create the bag node */
				XMLTriple bag_triple = new XMLTriple("Bag",
						"http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdf");

				XMLToken bag_token = new XMLToken(bag_triple, blank_att);

				XMLNode bag = new XMLNode(bag_token);

				/* create each li node and add to the bag */
				XMLTriple li_triple = new XMLTriple("li",
						"http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdf");

				resource_att.clear();
				resource_att.add("rdf:resource",
						"urn:miriam:obo.eco:ECO%3A0000004");

				XMLToken li_token = new XMLToken(li_triple, resource_att);
				li_token.setEnd();

				XMLNode li = new XMLNode(li_token);

				bag.addChild(li);

				resource_att.clear();
				resource_att.add("rdf:resource", "urn:miriam:pubmed:7017716");
				li_token = new XMLToken(li_triple, resource_att);
				li_token.setEnd();
				li = new XMLNode(li_token);

				bag.addChild(li);

				/* add the bag to bqbiol */
				bqbiol.addChild(bag);

				/* add subject, predicate, object and bqbiol to statement */
				statement.addChild(subject);
				statement.addChild(predicate);
				statement.addChild(object_);
				statement.addChild(bqbiol);

				/*
				 * create a top-level RDF element this will ensure correct
				 * merging
				 */

				XMLNamespaces xmlns = new XMLNamespaces();
				xmlns.add("http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdf");
				xmlns.add("http://purl.org/dc/elements/1.1/", "dc");
				xmlns.add("http://purl.org/dc/terms/", "dcterms");
				xmlns.add("http://www.w3.org/2001/vcard-rdf/3.0#", "vCard");
				xmlns.add("http://biomodels.net/biology-qualifiers/", "bqbiol");
				xmlns.add("http://biomodels.net/model-qualifiers/", "bqmodel");

				XMLTriple RDF_triple = new XMLTriple("RDF",
						"http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdf");

				XMLToken RDF_token = new XMLToken(RDF_triple, blank_att, xmlns);

				XMLNode annotation = new XMLNode(RDF_token);

				/* add the staement node to the RDF node */
				annotation.addChild(statement);

				s.appendAnnotation(annotation);

				libsbml.writeSBML(d, args[1]);
			}
		}

		return (int) errors;
	}
}
