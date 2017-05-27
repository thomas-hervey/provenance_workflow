from encoder import Encoder


class TwitterEncoder(Encoder):
    
    requirements = {}
    
    def __init__( self, *args ):
        super(TwitterEncoder, self).__init__()

    def _init_requirements(self):
        
        self.requirements = {
            'agent_id'           : ('user', 'id'),  # user id
            'agent_name'         : ('user', 'name'),  # user name
            'agent_location'     : ('user', 'location'),  # user & bio location JSON attributes
    
            'activity_start_time': 'created_at',  # tweet creation time
            'activity_location'  : 'coordinates',  # tweet & coordinates JSON attributes
    
            'entity_text'        : 'text',  # content body
            'entity_location'    : ('place', 'name')  # tweet & POI JSON attributes
        }


# TODO: find a way to attach the type to the tuples so
        # TODO that I can determine which prov statement to encode the data with