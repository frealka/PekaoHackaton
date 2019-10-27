import json
import unidecode
import pandas as pd
import utilities
from tqdm import tqdm
import numpy as np

already_calculated = {}

temp = [np.arange(-20,5), np.arange(-20, 5), np.arange(-5, 10), np.arange(0, 15), np.arange(5, 20), np.arange(10, 25), np.arange(15, 35), np.arange(15, 35), np.arange(7, 20), np.arange(0, 17), np.arange(-5, 15), np.arange(-5, 10)]

clouds = np.arange(0., 1.05, 0.05)

rain = np.array([0, 0, 0, 0, 10, 25, 50])*1e-2

# mock weather data
get_temp = lambda x: np.random.choice(temp[x-1])
get_clouds = lambda x: np.random.choice(clouds)
get_rain = lambda x: np.random.choice(rain)

MAX_MCC = 9399
MIN_MCC = 4121


def normalize(value, min_val, max_val):
    # min-max normalization
    return (value - min_val)/(max_val-min_val)


def getDefaultData():
    data = pd.read_csv('data/query.csv')

    data['ZipCode_float'] = data['ZipCode'].apply(lambda x: float(x)*1e-5)
    data['ZipCode'] = data['ZipCode'].apply(lambda x: '0'*(5-len(str(x))) + str(x))
    data['ZipCode'] = data['ZipCode'].apply(lambda x: x[0:2] + '-' + x[2:])

    data['LocCity'] = data['LocCity'].apply(utilities.get_city_from_longname)
    data['month'] = data['date'].apply(lambda x: int(utilities.convert_date_to_list(str(x))[1]))
    data['day'] = data['date'].apply(lambda x: int(utilities.convert_date_to_list(str(x))[2]))
    data['week_day'] = data['date'].apply(lambda x: int(utilities.convert_date_to_weekday(str(x))))
    data['business_sunday'] = data['date'].apply(lambda x: int(utilities.is_shopping_sunday(str(x))))

    data['temperature'] = data['month'].apply(lambda x: normalize(get_temp(x), -20, 35))
    data['overcast'] = data['month'].apply(get_clouds)
    data['precipitation'] = data['month'].apply(get_rain)

    # normalize date
    data['month'] = data['month']/12
    data['day'] = data['day']/31
    data['week_day'] = data['week_day']/7

    #normalize MCC
    data['MCC_norm'] = data['MCC'].apply(lambda x: normalize(x, MIN_MCC, MAX_MCC))
    data.to_csv('data/pre_landmarks.csv')
    
    data = data.head(20000)
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

    data.to_csv('dane/processed.csv')
    return data
