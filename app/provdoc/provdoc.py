from prov.model import ProvDocument
from prov.dot import prov_to_dot


class ProvDoc(object):
    """common prov doc class"""
    
    def __init__(self, name='', query='', ns=None):
        self.serialization = None
        self.name = name
        self.query = query
        if ns is None:
            self.namespaces = {}
        else:
            self.namespaces = ns
        
        # foundation provenance elements
        self.agent = None
        self.activity = None
        self.entity = None

        # foundation provenance element relations
        self.was_generated_by = None
        self.was_attributed_to = None
        self.was_associated_with = None
        
        self.provDocs = ProvDocument(namespaces=ns)
    
    """setup"""
    
    def add_namespaces( self, namespaces ):
        self.namespaces = namespaces
        self.provDocs.add_namespace(namespaces)
    
    """get attributes"""
    
    def get_name( self ):
        return self.name
    
    def get_query( self ):
        return self.query
    
    def get_prov( self ):
        return self.provDocs.get_provn()
    
    """provenance"""
    
    def new_agent( self, id, other_attributes=None):
        self.agent = self.provDocs.agent(identifier=id,
                                         other_attributes=other_attributes)
    
    def new_entity( self, id, other_attributes=None ):
        self.entity = self.provDocs.entity(identifier=id,
                                           other_attributes=other_attributes)
    
    def new_activity(self, id, start_time=None, end_time=None, other_attributes=None):
        self.activity = self.provDocs.activity(identifier=id,
                                               startTime=start_time,
                                               endTime=end_time,
                                               other_attributes=other_attributes)
    
    def new_was_generated_by( self, entity, activity, identifier=None, other_attributes=None ):
        self.was_generated_by = self.provDocs.wasGeneratedBy(entity, activity)
        print "thing"
    
    def new_was_associated_with( self, activity, agent, identifier=None, other_attributes=None ):
        self.was_associated_with = self.provDocs.wasAssociatedWith(activity, agent)
    
    def new_was_attributed_to( self, entity, agent, identifier=None, other_attributes=None ):
        self.was_attributed_to = self.provDocs.wasAttributedTo(entity, agent)
    
    """serializations"""
    
    def serialize( self, *args ):
        # serialize with json, xml
        if len(args) == 1:
            self.serialization = self.provDocs.serialize(format=args[0])
        # serialize with rdf (ttl)
        elif len(args) == 2:
            self.serialization = self.provDocs.serialize(format=args[0], rdf_format=args[1])
        # elif len(args) == 3:
        #     self.serialization = self.provDocs.serialize(format=args[0], rdf_format=args[1])
        #     self.provDocs.serialize(destination=args[2], format=args[0], rdf_format=args[1])
        else:
            print 'cannot serialize prov with argument length: ', len(args), '| arguments: ', args
            return

    def get_serialization( self ):
        return self.serialization

    """diagrams"""

    # TODO: figure out how to do file I/O from class method
    def generate_diagram( self, file_name, file_extension ):
        dot = prov_to_dot(self.provDocs)
        if file_extension == 'png':
            file_name += '.png'
            dot.write_png(file_name)
        elif file_extension == 'jpg':
            file_name += '.jpg'
            dot.write_jpg(file_name)
        else:
            print('not jpg or png')
