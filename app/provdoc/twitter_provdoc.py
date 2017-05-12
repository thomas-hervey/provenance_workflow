from provdoc import ProvDoc


class TwitterProvDoc(ProvDoc):

    def __init__(self, name, query, namespaces, *args):
        super(TwitterProvDoc, self).__init__(name, query, namespaces)

