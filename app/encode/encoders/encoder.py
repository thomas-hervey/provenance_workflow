from ..utils import objwalk, save_to_file


class Encoder(object):
    
    def __init__( self, data=None ):
        
        # input data
        self.data = data
        
        # items to look for in data
        self.requirements = {
    
            'agent_id'           : None,  # user id
            'agent_name'         : None,  # user name
            'agent_location'     : None,  # user & bio location JSON attributes
    
            'activity_start_time': None,  # tweet creation time
            'activity_location'  : None,  # tweet & coordinates JSON attributes
    
            'entity_text'        : None,  # content body
            'entity_location'    : None  # tweet & POI JSON attributes
        }
        
        # provenance document class
        self.prov_document = None
        
        # serialization output location
        self.serialization_output_location = None
        
        # initialize foundation element requirements to look for
        self._init_requirements()
    
    def _init_requirements(self):
        # child classes init specific requirements
        pass
    
    def add_prov_doc(self, prov_doc):
        self.prov_document = prov_doc
    
    """get attributes"""

    def get_requirements( self ):
        return self.requirements
    
    """requirements"""
    
    def look_for_requirements( self, data ):
        # if user hasn't provided data, use class data added on instantiation
        if data is None:
            data = self.data
        
        # look at path an values of input data (as a dictionary)
        for path, value in objwalk(data):
            
            # look at requirements (specific to SNS source)
            for k, v in self.requirements.iteritems():
                
                # check if path contains requirements
                requirement_result = self._is_requirement_in_path(path, value, v)
                
                # if so, and it's not None
                if requirement_result is not None:
                    # update the requirement value with found value
                    self.requirements[k] = requirement_result
    
    @staticmethod
    def _is_requirement_in_path( path, value, requirement ):
        # if both requirement and path are tuples
        if isinstance(requirement, tuple) and isinstance(path, tuple):
            # if the set of the path contains the requirement
            if set(requirement).issubset(set(path)):
                return path, value, requirement
        # otherwise, if requirement is a string
        elif isinstance(requirement, str):
            # if the path contains the requirement
            if requirement in path:
                # TODO: make this temp fix more flexible
                # if the path is a tuple of only the first element in a tree
                if len(path) == 1:
                    return path, value, requirement
    
    """ add provenance information """

    def set_prov_core_elements( self ):
    
        # attribute lists to be passed to prov elements on creation
        agent_attributes = {}
        activity_attributes = {}
        entity_attributes = {}
        activity_start_time = None
    
        # for each matched requirement of the data, add to respective attribute lists
        for k, v in self.get_requirements().iteritems():
            path, value, requirement = v
            value = str(value)
        
            if k is 'agent_id':
                agent_attributes['prov:id'] = value
            elif k is 'agent_name':
                agent_attributes['foaf:name'] = value
            elif k is 'agent_location':
                agent_attributes['prov:atLocation'] = value
            elif k is 'activity_start_time':
                activity_start_time = value
            elif k is 'activity_location':
                activity_attributes['prov:atLocation'] = value
            elif k is 'entity_text':
                entity_attributes['prov:value'] = value
            elif k is 'entity_location':
                entity_attributes['prov:atLocation'] = value
            else:
                print "ERROR, couldn't figure out how to handle this error"
    
        if len(agent_attributes) != 0:
            self.prov_document.new_agent('local:contributor', other_attributes=agent_attributes)
        if len(activity_attributes) != 0:
            self.prov_document.new_activity('local:compose', start_time=activity_start_time,
                                            other_attributes=activity_attributes)
        if len(entity_attributes) != 0:
            self.prov_document.new_entity('local:composition', other_attributes=entity_attributes)
        
        self.set_prov_core_relations()
    
    def set_prov_core_relations( self ):
        if self.prov_document.activity and self.prov_document.entity and not self.prov_document.was_generated_by:
            self.prov_document.new_was_generated_by(self.prov_document.entity, self.prov_document.activity)
        if self.prov_document.activity and self.prov_document.agent and not self.prov_document.was_associated_with:
            self.prov_document.new_was_associated_with(self.prov_document.activity, self.prov_document.agent)
        if self.prov_document.entity and self.prov_document.agent and not self.prov_document.was_attributed_to:
            self.prov_document.new_was_attributed_to(self.prov_document.entity, self.prov_document.agent)
    
    def write_serialization(self, file_name):
        self.serialization_output_location = save_to_file(self.prov_document.get_serialization(), file_name)
