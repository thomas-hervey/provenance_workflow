import json
import os
from pprint import pprint


class Reader(object):
    
    def __init__(self, name='Data Reader', data=None):
        self.name = name
        self.data = data
        self.json_data = {}
    
    def load_data_from_file(self, filepath):
        with open(filepath) as source_file:
            self._data_to_json(source_file)
    
    def _data_to_json(self, source_data):
        self.json_data = json.load(source_data)
    
    def get_data(self):
        return self.json_data
    
    def print_data( self ):
        pprint(self.json_data)
