from utils import objwalk


class Encoder(object):
    
    requirements = []
    
    def __init__( self ):
        self.init_requirements()
    
    def init_requirements(self):
        pass
    
    # def get_foundation(self, data):
    #     pass
    #
    # def get_foundation_agent(self):
    #     pass
    #
    # def get_foundation_activity(self):
    #     pass
    #
    # def get_foundation_entity(self):
    #     pass
    
    def traverse_data(self, data):
        # look at path an values of dictionary
        for path, value in objwalk(data):
            # in the matching requirements
            for requirement in self.requirements:
                # check if path contains requirements
                match = self.is_match(path, value, requirement)
                if match is not None:
                    print match
    
    def is_match(self, path, value, requirement):
        if set(requirement).issubset(set(path)):
            return path, value, requirement

