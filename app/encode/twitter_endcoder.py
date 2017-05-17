from encoder import Encoder


class TwitterEncoder(Encoder):
    
    requirements = []
    
    def __init__( self, *args ):
        super(TwitterEncoder, self).__init__()
    
    def init_requirements(self):
        user_home = ('user', 'home_location')
        tweet_location = ('content', 'location')
        tweet_geotag = ('content', 'tagged_location')
        self.requirements.append(user_home)
        self.requirements.append(tweet_location)
        self.requirements.append(tweet_geotag)


# TODO: find a way to attach the type to the tuples so
        # TODO that I can determine which prov statement to encode the data with