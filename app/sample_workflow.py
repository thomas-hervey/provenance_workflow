from pprint import pprint

from provdoc import NAMESPACES, TwitterProvDoc, ProvDoc
from utils import Reader, test_data
from encode import TwitterEncoder

# create sample reader
sample_reader = Reader()
sample_reader.load_json_data(test_data)

# create sample encoder
sample_encoder = TwitterEncoder()
sample_encoder.traverse_data(sample_reader.get_data())

#
#
# # #reading in from file
# # filepath = "../../data/test_data.json"
# # sample_reader.load_data(filepath)
# # sample_reader.print_data()
#
#
# # create provenance document
# sample_twitter_document = TwitterProvDoc('sample_document_name', 'sample_query', NAMESPACES, 'sample_extra_value')
#
# twitter_user = sample_twitter_document.new_agent('local:contributor',
#                                                  {'prov:label'     : "a twitter user",
#                                                   'prov:atLocation': "home location"})
# tweet_posting = sample_twitter_document.new_activity('local:compose',
#                                                      {'prov:label'     : "composing a tweet",
#                                                       'prov:atLocation': "lat/lon"})
# tweet = sample_twitter_document.new_entity('local:composition',
#                                            {'prov:label'     : "a tweet",
#                                             'prov:atLocation': "associated location"})
#
# sample_twitter_document.new_was_generated_by(tweet, tweet_posting)
# sample_twitter_document.new_was_associated_with(tweet_posting, twitter_user)
# sample_twitter_document.new_was_attributed_to(tweet, twitter_user)
#
# print "PROV:\n", sample_twitter_document.get_prov()
#
# # serialize provenance as rdf ttl
# sample_twitter_document.serialize('rdf', 'ttl')
#
# # query provenance serialization
# serialization = sample_twitter_document.get_serialization()
# print "SERIALIZATION:\n", serialization
