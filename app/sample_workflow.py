import json
from pprint import pprint

import rdflib.graph as g

import os

from provdoc import NAMESPACES, TwitterProvDoc
from utils import Reader, test_data
from encode import TwitterEncoder


def run_workflow(filepath):
    
    # create sample reader
    sample_reader = Reader('Trump Reader')   # also capable of taking in data not from file
    sample_reader.load_data_from_file(filepath)
    
    # print sample_reader.get_data()
    
    # create sample encoder
    sample_encoder = TwitterEncoder()
    sample_encoder.look_for_requirements(sample_reader.get_data())

    print "GET REQUIREMENTS: \n", sample_encoder.get_requirements()

    # create provenance document
    sample_twitter_prov_doc = TwitterProvDoc('sample_document_name', 'sample_query', NAMESPACES, 'sample_extra_value')
    
    sample_encoder.add_prov_doc(sample_twitter_prov_doc)
    sample_encoder.implement_requirements()
#
    print "PROV-N: \n", sample_encoder.prov_document.get_prov()
#     # print type(sample_encoder.prov_document.get_prov())
#
#     # serialize document into turtle
#     sample_encoder.prov_document.serialize('rdf', 'ttl')
#
#     # save turtle serialization
#     sample_encoder.write_serialization('test.ttl')
#
#     from SPARQLWrapper import SPARQLWrapper, JSON
#     import rdflib
#
#     g = rdflib.Graph()
#     result = g.parse('test.ttl', format='n3')
#     # for stmt in g:
#     #     pprint(stmt)
#
#     sample_query = """
#         SELECT ?label
#         WHERE {
#             ?compose
#             rdfs:label ?label.
#             ?compose
#             prov:atLocation ?location.
#             ?compose
#             prov:wasAssociatedWith ?contributor.
#             ?contributor
#             prov:atLocation ?location2.
#         }
#         """
#     qres = g.query(sample_query)
#     for row in qres:
#         print "hi"
#         print(row)
#
#



# file_name = 'test_data.json'
file_name = 'trump_tweets.json'
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
dirPath = os.path.join(PROJECT_ROOT, '..')
filepath = os.path.join(dirPath, 'data/', file_name)

run_workflow(filepath)
