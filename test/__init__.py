from prov.model import ProvDocument, PROV
import json
from pprint import pprint
from utils import objwalk

# Create a new provenance document
d1 = ProvDocument()  # d1 is now an empty provenance document

# Declaring namespaces for various prefixes used in the example
d1.add_namespace('local', 'http://localhost/#')
d1.add_namespace('prov', 'https://www.w3.org/ns/prov/')
d1.add_namespace('foaf', 'http://xmlns.com/foaf/0.1/')

# Entities
tweet = d1.entity('local:composition', {'prov:label': "a tweet", 'prov:atLocation': "associated location"})
# Activities
tweet_posting = d1.activity('local:compose', other_attributes={'prov:label': "composing a tweet", 'prov:atLocation': "lat/lon"})
# Agents
twitter_user = d1.agent('local:contributor', {'prov:label': "a twitter user", 'prov:atLocation': "not sure"})
# Relationships
d1.wasGeneratedBy(tweet, tweet_posting)
d1.wasAssociatedWith(tweet_posting, twitter_user)
d1.wasAttributedTo(tweet, twitter_user)

# load test data
local_test_data = '~/Projects/thesis/LOCATION_PROJECT/test/test_data.json'
with open(local_test_data) as test_data_file:
    test_data = json.load(test_data_file)
    pprint(test_data)


# serialize prov document
local_serialization = 'test2.json'
d1.serialize(local_serialization)
# read json data
with open(local_serialization) as serialized_data_file:
    data = json.load(serialized_data_file)
    
    for k, v in data.iteritems():
        print "key: ", k, "value: ", v
    
    if 'prov:agent' in data:
        print "true"
    # example_dict.get('key1', {}).get('key2')
    print data.get('entity', {}).get('local:composition', {}).get('prov:atLocation')
    
    # for path, value in objwalk(data):
    #     if "atLocation" in path[-1]:
    #         print 'path: ', path, '  value: ', value

# # print json data
# print("***************")
# pprint(data)
# print(type(data))
# print("***************")
#
#
# d2 = ProvDocument()
# d2_deserialized = d2.deserialize('test2.json')
# print(d2_deserialized)
#
# prov2 = d2_deserialized.get_provn()
# print(type(prov2))
# print(prov2)


# thing.serialize('test3.json')
# print(thing.get_provn())