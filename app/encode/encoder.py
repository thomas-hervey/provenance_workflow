from utils import objwalk, save_to_file


class Encoder(object):
    
    def __init__( self ):
        self.requirements = []
        self.requirements_met = []

        self.prov_document = None

        self.agent = None
        self.activity = None
        self.entity = None

        self.was_generated_by = None
        self.was_attributed_to = None
        self.was_associated_with = None
        
        self.output_location = None
        
        self._init_requirements()
    
    def _init_requirements(self):
        pass

    def get_requirements( self ):
        return self.requirements

    def get_requirements_met( self ):
        return self.requirements_met
    
    def traverse_data(self, data):
        # look at path an values of dictionary
        for path, value in objwalk(data):
            # in the matching requirements
            for requirement in self.requirements:
                # check if path contains requirements
                requirement_results = self._path_contains_requirements(path, value, requirement)
                if requirement_results is not None:
                    self.requirements_met.append(requirement_results)
                    # print requirement_results
    
    def _path_contains_requirements(self, path, value, requirement):
        if set(requirement).issubset(set(path)):
            return path, value, requirement
        
    def implement_requirements( self, prov_document ):

        self.prov_document = prov_document

        # for each matched requirement of the data
        for requirement in self.get_requirements_met():

            print "REQUIREMENT MET: ", requirement

            # check if the requirement has been handled
            self._check_if_requirements_have_been_handled()

            self.check_requirement()

            if '1' in requirement[0]:
                if 'content' in requirement[0]:
                    if 'location' in requirement[0]:
                        self.activity = self.prov_document.new_activity('local:compose',
                                                                   {'prov:label'     : "composing a tweet",
                                                                    'prov:atLocation': requirement[1]})
                    elif 'tagged_location' in requirement[0]:
                        self.entity = self.prov_document.new_entity('local:composition',
                                                               {'prov:label'     : "a tweet",
                                                                'prov:atLocation': requirement[1]})
                    else:
                        print "CHECK AGAIN"
                elif 'user' in requirement[0]:
                    if 'home_location' in requirement[0]:
                        self.agent = self.prov_document.new_agent('local:contributor',
                                                             {'prov:label'     : "a twitter user",
                                                              'prov:atLocation': requirement[1]})
                    else:
                        print "CHECK AGAIN"

            self._check_if_requirements_have_been_handled()
    
    def implement_requirements(self, prov_document):
        self.prov_document = prov_document
    
    def _check_if_requirements_have_been_handled( self ):
        
        if self.activity is not None and self.entity is not None and self.was_generated_by is None:
            self.was_generated_by = self.prov_document.new_was_generated_by(self.entity, self.activity)
        if self.activity is not None and self.agent is not None and self.was_associated_with is None:
            self.was_associated_with = self.prov_document.new_was_associated_with(self.activity, self.agent)
        if self.entity is not None and self.agent is not None and self.was_attributed_to is None:
            self.was_attributed_to = self.prov_document.new_was_attributed_to(self.entity, self.agent)
    
    
    def check_requirement(self):
        pass
    
    def write_serialization(self, file_name):
        self.output_location = save_to_file(self.prov_document.get_serialization(), file_name)
