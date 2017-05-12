from provdoc import *
import rdflib

namespaces = {
   'local': 'http://localhost/#',
   'prov': 'https://www.w3.org/ns/prov/',
   'foaf': 'http://xmlns.com/foaf/0.1/'
}

# create provenance document
sample_twitter_document = TwitterProvDoc('sample_document_name', 'sample_query', namespaces, 'sample_extra_value')

twitter_user = sample_twitter_document.new_agent('local:contributor', {'prov:label': "a twitter user",
                                                        'prov:atLocation': "home location"})
tweet_posting = sample_twitter_document.new_activity('local:compose', {'prov:label'     : "composing a tweet",
                                                       'prov:atLocation': "lat/lon"})
tweet = sample_twitter_document.new_entity('local:composition', {'prov:label': "a tweet",
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


