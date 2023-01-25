import numpy as np

# CONSTANTS

REFERENCE_YEAR = 1000
JAN_01_REF = 2

# Returns the first day of the week of the given year
def first_day_year(year):
    year_delta = year - REFERENCE_YEAR
    days_from_ref = 365 * year_delta + int(year_delta/4) - int(year_delta/100) + int(year_delta/400)
    if not ((year%4 == 0 and year%100 != 0) or year%400 == 0):
         days_from_ref += 1
    return (days_from_ref + JAN_01_REF) % 7

# Returns the difference from 30 days of each month, taking leap years into account
def get_deltas_of_months(year):
    deltas = {0 : 1, 1 : -2, 2 : 1, 3 : 0, 4 : 1, 5 : 0, 6 : 1, 7 : 1, 8 : 0, 9 : 1, 10 : 0, 11 : 1}
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        deltas[1] += 1
    return deltas

# Returns the day of the week given a starting day and a delta in days
def weekday_delta(start, delta):
    return (start + delta) % 7

if __name__ == '__main__':
    pass
