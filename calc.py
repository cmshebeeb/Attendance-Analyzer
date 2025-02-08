import os
def calc(row, date_columns):
    present = 0
    absent = 0
    for date in date_columns:
        if row.get(date) == 'P':  # Use .get() to retrieve values from the dictionary
            present += 1
        elif row.get(date) == 'A':
            absent += 1
    return present, absent
