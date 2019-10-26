import json
import unidecode

json_file = open('history.city.list.json')
data = json.load(json_file)


def get_object_by_name(name):
    for dict in data:
        city_name = dict['city']['name'].lower()
        name = name.lower()
        name = unidecode.unidecode(name)
        if city_name == name:
            return dict
        # if dict['city']
            # print(dict)
            # return dict

result = get_object_by_name('Wrocław')
print(result)