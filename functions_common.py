import csv
from datetime import datetime


def read_csv_as_list(filepath):
    with open(filepath, newline='') as f:
        return list(csv.reader(f, quoting=csv.QUOTE_NONNUMERIC))

def save_list_to_csv(filepath, data):
    with open(filepath, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def get_time_now():
    dt_now = datetime.now()
    dt_now_reformat_str = dt_now.strftime("%Y/%m/%d %H:%M:%S")
    dt_now_reformat_int = dt_now.strftime("%Y%m%d%H%M%S")

    return dt_now_reformat_str, dt_now_reformat_int
