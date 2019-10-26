import datetime
import requests
import pandas as pd
import json
import unidecode

# WEATHER DATA
json_file = open('history.city.list.json')
data = json.load(json_file)


def get_object_by_name(name):
    for dict in data:
        city_name = dict['city']['name'].lower()
        name = name.lower()
        name = unidecode.unidecode(name)
        if city_name == name:
            return dict


# https://openweathermap.org/history
def get_id_by_name(name):
    element = get_object_by_name(name)
    return element['id']


def get_coords_by_name(name):
    object = get_object_by_name(name)
    coords = object['city']['coord']
    return tuple(coords.values())


# UTILS FUNCTIONS
def convert_date_to_list(date):
    y = date[:4]
    m = date[4:6]
    d = date[6:]
    return [y, m, d]


def convert_time_to_list(time):
    return [time[:2]]


def convert_date_to_weekday(date):
    date_list = convert_date_to_list(date)
    return datetime.datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]), 0, 0, 0).weekday()


# start date = 2012 08 01
# end date = 2018 11 01
def is_shopping_sunday(date):
    if date == '20180805':
        return 1
    elif date == '20180826':
        return 1
    elif date == '20180902':
        return 1
    elif date == '20180930':
        return 1
    elif date == '20181007':
        return 1
    elif date == '20181028':
        return 1
    return 0


# POSTAL FUNCTIONS
BASE_POSTAL_URL = 'http://kodpocztowy.intami.pl/api/'


def get_location_from_postal_code(postal_code):
    response = requests.get(BASE_POSTAL_URL + str(postal_code))
    data = response.json()
    return data[0]['gmina'], data[0]['powiat']


ZABYTKI_FRAME = pd.read_csv('./data/zabytki.csv', delimiter=";", encoding="iso-8859-2")


def get_number_of_zabytki(powiat, gmina, miejscowosc):
    powiat = ZABYTKI_FRAME.loc[ZABYTKI_FRAME['POWIAT'] == powiat]
    gmina = powiat.loc[powiat['GMINA'] == gmina]
    miejscowosc = gmina.loc[gmina['MIEJSCOWOSC'] == miejscowosc]

    return powiat.count()['INSPIRE_ID'], gmina.count()['INSPIRE_ID'], miejscowosc.count()['INSPIRE_ID']


if __name__ == '__main__':
    # print(convert_date_to_list('20180801'))
    # print(convert_time_to_list('102906'))
    # print(convert_date_to_weekday('20191026'))
    # print(is_shopping_sunday('20181008'))
    # print(is_shopping_sunday('20181007'))
    # print(get_location_from_postal_code('55-050'))
    print(get_id_by_name('Wrocław')) #ID for API call
    print(get_number_of_zabytki('wrocławski', 'Żórawina', 'Żórawina'))
    print(get_coords_by_name('Wrocław'))
