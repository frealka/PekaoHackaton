import json
import unidecode
import pandas as pd
import utilities

data = pd.read_csv('data/query.csv')
data['ZipCode'] = data['ZipCode'].apply(lambda x: '0'*(5-len(str(x))) + str(x))
data['ZipCode'] = data['ZipCode'].apply(lambda x: x[0:2] + '-' + x[2:])
data['LocCity'] = data['LocCity'].apply(utilities.get_city_from_longname)
data['month'] = data['date'].apply(lambda x: (utilities.convert_date_to_list(str(x))[1]))
data['day'] = data['date'].apply(lambda x: int(utilities.convert_date_to_list(str(x))[2]))
data['week_day'] = data['date'].apply(lambda x: int(utilities.convert_date_to_weekday(str(x))))
data['business_sunday'] = data['date'].apply(lambda x: int(utilities.is_shopping_sunday(str(x))))
data['longitude'] = data['LocCity'].apply(lambda x: utilities.get_coords_by_name(x))
data.to_csv('pre.csv')

print(data.head())
