import json
from pprint import pprint
from search import objwalk


class Reader(object):
    raw_data = {}
    
    def __init__( self, test_param=None ):
        self.test_param = test_param
    
    def load_data( self, data_source ):
        self.raw_data = json.load(data_source)
    
    def print_data( self ):
        pprint(self.raw_data)
    
    def find_item( self, item ):
        for path, value in objwalk(self.raw_data):
            print path, value
