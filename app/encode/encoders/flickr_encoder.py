from encoder import Encoder


class FlickrEncoder(Encoder):
    requirements = {}
    
    def __init__( self, *args ):
        super(FlickrEncoder, self).__init__()
    
    def _init_requirements( self ):
        self.requirements = {
            'agent_id'           : ('owner', 'nsid'),  # user id
            'agent_name'         : ('owner', 'realname'),  # user name
            'agent_location'     : ('owner', 'location'),  # user & bio location JSON attributes
            
            'activity_start_time': 'created_at',  # tweet creation time
            'activity_location'  : 'location',  # tweet & coordinates JSON attributes
            
            'entity_text'        : 'description',  # content body
            'entity_location'    : ('place', 'name')  # tweet & POI JSON attributes
        }
        
        
        # TODO: find a way to attach the type to the tuples so
        # TODO that I can determine which prov statement to encode the data with