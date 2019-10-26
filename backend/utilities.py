import datetime
import requests
import json

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


BASE_POSTAL_URL = 'http://kodpocztowy.intami.pl/api/'


def get_location_from_postal_code(postal_code):
    response = requests.get(BASE_POSTAL_URL + str(postal_code))
    data = response.json()
    return data[0]['gmina'], data[0]['powiat']


if __name__ == '__main__':
    # print(convert_date_to_list('20180801'))
    # print(convert_time_to_list('102906'))
    # print(convert_date_to_weekday('20191026'))
    # print(is_shopping_sunday('20181008'))
    # print(is_shopping_sunday('20181007'))
    print(get_location_from_postal_code('55-050'))
