import json
import os
from pprint import pprint

class Reader(object):
    json_data = {}
    
    def __init__( self, test_param=None ):
        self.test_param = test_param
    
    def load_data_from_file(self, relative_filepath):
        current_directory = os.path.dirname(__file__)
        filename = os.path.join(current_directory, relative_filepath)
        with open(filename) as source_file:
            self._to_json(source_file)
    
    def load_json_data(self, source_data):
        self.json_data = source_data
    
    def _to_json( self, source_file ):
        self.json_data = json.load(source_file)
    
    def get_data(self):
        return self.json_data
    
    def print_data( self ):
        pprint(self.json_data)
