import json
import unidecode
import pandas as pd
import utilities
from tqdm import tqdm

already_calculated = {}

def getDefaultData():
    data = pd.read_csv('data/query.csv')
    data['ZipCode'] = data['ZipCode'].apply(lambda x: '0'*(5-len(str(x))) + str(x))
    data['ZipCode'] = data['ZipCode'].apply(lambda x: x[0:2] + '-' + x[2:])
    data['LocCity'] = data['LocCity'].apply(utilities.get_city_from_longname)
    data['month'] = data['date'].apply(lambda x: (utilities.convert_date_to_list(str(x))[1]))
    data['day'] = data['date'].apply(lambda x: int(utilities.convert_date_to_list(str(x))[2]))
    data['week_day'] = data['date'].apply(lambda x: int(utilities.convert_date_to_weekday(str(x))))
    data['business_sunday'] = data['date'].apply(lambda x: int(utilities.is_shopping_sunday(str(x))))
    data['landmarks_close'] = 0
    data['landmarks_middle'] = 0
    data['landmarks_far'] = 0
    for i, row in tqdm(data.iterrows()):
        p,g,m = already_calculated.get((row['ZipCode'], row['LocCity']), (None, None, None))
        if not p:
            p,g,m = utilities.get_locations(row['ZipCode'], row['LocCity'])
            already_calculated[(row['ZipCode'], row['LocCity'])] = (p,g,m)

        data.landmarks_close.iloc[i] = m
        data.landmarks_middle.iloc[i] = g
        data.landmarks_far.iloc[i] = p

    data.to_csv('processed.csv')

getDefaultData()