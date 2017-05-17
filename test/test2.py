import os

from app.encode import load_data, to_json
from utils.data import test_data



dir = os.path.dirname(__file__)
filename = os.path.join(dir, '../data/test_data.json')

parsed_data = load_data(filename)


