from encoder import Encoder


class TwitterEncoder(Encoder):
    
    def __init__( self, *args ):
        super(TwitterEncoder, self).__init__()

    def _init_requirements(self):
        user_home = ('user', 'location')  # user & bio location JSON attributes
        tweet_location = 'coordinates'  # tweet & coordinates JSON attributes
        tweet_geotag = ('place', 'name')  # tweet & POI JSON attributes
        self.requirements.append(user_home)
        self.requirements.append(tweet_location)
        self.requirements.append(tweet_geotag)
    


# TODO: find a way to attach the type to the tuples so
        # TODO that I can determine which prov statement to encode the data with