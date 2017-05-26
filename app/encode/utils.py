"""
source:
 http://tech.blog.aknin.name/2011/12/11/walking-python-objects-recursively/
"""
import os
from collections import Mapping, Set, Sequence

# dual python 2/3 compatability, inspired by the "six" library
string_types = (str, unicode) if str is bytes else (str, bytes)
iteritems = lambda mapping: getattr(mapping, 'iteritems', mapping.items)()


def objwalk( obj, path=(), memo=None ):
    if memo is None:
        memo = set()
    iterator = None
    if isinstance(obj, Mapping):
        iterator = iteritems
    elif isinstance(obj, (Sequence, Set)) and not isinstance(obj, string_types):
        iterator = enumerate
    if iterator:
        if id(obj) not in memo:
            memo.add(id(obj))
            for path_component, value in iterator(obj):
                for result in objwalk(value, path + (path_component,), memo):
                    yield result
            memo.remove(id(obj))
    else:
        yield path, obj


def save_to_file(output, file_name):
    # create output path for file
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__) + "/output/")
    dirPath = os.path.join(PROJECT_ROOT, file_name)

    # save input to file
    new_file = open(dirPath, 'w+')
    new_file.write(output)
    
    return dirPath
