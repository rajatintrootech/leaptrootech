def get_leap_year(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        return True

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        return False


def get_range_leap_year(start, end):
    res = []
    for i in range(start, end):
        data = get_leap_year(i)
        if data:
            res.append(i)
    return res
