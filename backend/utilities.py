import datetime

def convertDateToList(date):
    y = date[:4]
    m = date[4:6]
    d = date[6:]
    return [y, m, d]

def convertTimeToList(time):
    return [time[:2]]

def convertDateToWeekday(date):
    date_list = convertDateToList(date)
    return datetime.datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]), 0, 0, 0).weekday()

# start date = 2012 08 01
# end date = 2018 11 01
def isShoppingSunday(date):
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


print(convertDateToList('20180801'))
print(convertTimeToList('102906'))
print(convertDateToWeekday('20191026'))
print(isShoppingSunday('20181008'))
print(isShoppingSunday('20181007'))