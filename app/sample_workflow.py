import json
from pprint import pprint

from provdoc import *
from utils import Reader, test_data

namespaces = {
    'local': 'http://localhost/#',
    'prov' : 'https://www.w3.org/ns/prov/',
    'foaf' : 'http://xmlns.com/foaf/0.1/'
}

# create provenance document
sample_twitter_document = TwitterProvDoc('sample_document_name', 'sample_query', namespaces, 'sample_extra_value')

twitter_user = sample_twitter_document.new_agent('local:contributor',
                                                 {'prov:label'     : "a twitter user",
                                                  'prov:atLocation': "home location"})
tweet_posting = sample_twitter_document.new_activity('local:compose',
                                                     {'prov:label'     : "composing a tweet",
                                                      'prov:atLocation': "lat/lon"})
tweet = sample_twitter_document.new_entity('local:composition',
                                           {'prov:label'     : "a tweet",
                                            'prov:atLocation': "associated location"})

sample_twitter_document.new_wasGeneratedBy(tweet, tweet_posting)
sample_twitter_document.new_wasAssociatedWith(tweet_posting, twitter_user)
sample_twitter_document.new_wasAttributedTo(tweet, twitter_user)

# serialize provenance as rdf ttl
sample_twitter_document.serialize('rdf', 'ttl')

# query provenance serialization
serialization = sample_twitter_document.get_serialization()
print serialization
print sample_twitter_document.get_prov()

# grab sample data
data = test_data
pprint(data)



# reader = Reader()
# local_test_data = 'test_data.json'
# with open(local_test_data) as test_data_file:
#     reader.load_data(test_data_file)
#     reader.print_data()
