from prov.model import ProvDocument


class ProvDoc:
    """common prov doc class"""
    
    name = ''
    query = ''
    
    def __init__(self, name, query):
        self.name = name
        self.query = query
        self.provDoc = ProvDocument()

    def display_name(self):
        print "Name : ", self.name
    
    def display_query(self):
        print "Name : ", self.query
    
    def display_prov(self):
        print "Name : ", self.provDoc.get_provn()
    
