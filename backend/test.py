import json
import unidecode
import pandas as pd

data = pd.read_csv('data/query.csv')
data['ZipCode'] = data['ZipCode'].apply(lambda x: '0'*(5-len(str(x))) + str(x))