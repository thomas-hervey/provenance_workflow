from pprint import pprint

import rdflib.graph as g

import os

from provdoc import NAMESPACES, TwitterProvDoc
from utils import Reader, test_data
from encode import TwitterEncoder


def run_workflow(data):
    
    # create sample reader
    sample_reader = Reader()
    sample_reader.load_json_data(data)
    
    # create sample encoder
    sample_encoder = TwitterEncoder()
    sample_encoder.traverse_data(sample_reader.get_data())

    # create provenance document
    sample_twitter_document = TwitterProvDoc('sample_document_name', 'sample_query', NAMESPACES, 'sample_extra_value')

    # print sample_encoder.get_requirements()
    # print sample_encoder.get_requirements_met()
    
    sample_encoder.implement_requirements(sample_twitter_document)
    
    print "PROV-N: \n", sample_encoder.prov_document.get_prov()
    # print type(sample_encoder.prov_document.get_prov())
    
    # serialize document into turtle
    sample_encoder.prov_document.serialize('rdf', 'ttl')
    
    # save turtle serialization
    sample_encoder.write_serialization('test.ttl')

    from SPARQLWrapper import SPARQLWrapper, JSON
    import rdflib
    
    g = rdflib.Graph()
    result = g.parse('test.ttl', format='n3')
    # for stmt in g:
    #     pprint(stmt)
    
    sample_query = """
        SELECT ?label
        WHERE {
            ?compose
            rdfs:label ?label.
            ?compose
            prov:atLocation ?location.
            ?compose
            prov:wasAssociatedWith ?contributor.
            ?contributor
            prov:atLocation ?location2.
        }
        """
    qres = g.query(sample_query)
    for row in qres:
        print "hi"
        print(row)

run_workflow(test_data)
