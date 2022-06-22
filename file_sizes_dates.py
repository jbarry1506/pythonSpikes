import os
import math
from datetime import datetime, date, timedelta

file_locations = [
    ".\\"
]


def date_compare(d):
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day

    today = date(year, month, day)
    delta = today - d
    return delta


for location in file_locations:
    file_list = os.listdir(location)
    # print(file_list)
    space_saved = 0

    for f in file_list:
        # creation_time = datetime.fromtimestamp(os.path.getctime(f)).strftime('%Y-%m-%d %H:%M:%S')
        creation_time = datetime.fromtimestamp(os.path.getctime(location+f)).date()
        file_size = os.path.getsize(location+f)
        print(f"{location+f}: \t{creation_time}\t{file_size}")
        days_since_creation = date_compare(creation_time)
        print(days_since_creation)
        if days_since_creation >= timedelta(days=60):
            print("this file should be deleted")
            space_saved = space_saved + file_size

    space_saved = space_saved / math.pow(1024,3)
    print(space_saved)
