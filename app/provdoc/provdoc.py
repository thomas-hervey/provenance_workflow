from prov.model import ProvDocument
from prov.dot import prov_to_dot


class ProvDoc(object):
    """common prov doc class"""
    
    name = ''
    query = ''
    
    def __init__(self, name, query, ns):
        self.serialization = None
        self.name = name
        self.query = query
        self.provDocs = ProvDocument(namespaces=ns)

    """setup"""
    def add_namespaces(self, namespaces):
        self.provDocs.add_namespace(namespaces)
    
    """get attributes"""
    def get_name(self):
        return self.name
    
    def get_query(self):
        return self.query
    
    def get_prov(self):
        return self.provDocs.get_provn()
    
    """serializations"""
    def serialize(self, *args):
        # serialize with json, xml
        if len(args) == 1:
            self.serialization = self.provDocs.serialize(format=args[0])
        # serialize with rdf (ttl)
        elif len(args) == 2:
            self.serialization = self.provDocs.serialize(format=args[0], rdf_format=args[1])
        else:
            print 'cannot serialize prov with argument length: ', len(args), '| arguments: ', args
            return
    
    def get_serialization(self):
        return self.serialization
    
    """diagrams"""
    # TODO: figure out how to do file I/O from class method
    def generate_diagram(self, file_name, file_extension):
        dot = prov_to_dot(self.provDocs)
        if file_extension == 'png':
            file_name += '.png'
            dot.write_png(file_name)
        elif file_extension == 'jpg':
            file_name += '.jpg'
            dot.write_jpg(file_name)
        else:
            print('not jpg or png')
    
    """provenance"""
    def new_agent(self, id, *args):
        return self.provDocs.agent(identifier=id, other_attributes=args[0])
    
    def new_entity(self, id, *args):
        return self.provDocs.entity(identifier=id, other_attributes=args[0])
    
    def new_activity(self, id, *args):
        return self.provDocs.activity(identifier=id, other_attributes=args[0])
    
    def new_wasGeneratedBy(self, entity, activity):
        return self.provDocs.wasGeneratedBy(entity, activity)

    def new_wasAssociatedWith(self, activity, agent):
        return self.provDocs.wasAssociatedWith(activity, agent)

    def new_wasAttributedTo(self, entity, agent):
        return self.provDocs.wasAttributedTo(entity, agent)
    
    # # create initial provenance
    # def init_prov(self):
    #     self.new_agent('agent')
    #     self.new_entity('entity')
    #     self.new_activity('activity')
