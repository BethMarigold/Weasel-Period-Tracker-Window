def wpt(user_input, user_input2, user_input3, user_input4):
    length3 = user_input
    month3, day3, year3 = length3.split("/")
    month3 = int(month3)
    day3 = int(day3)
    year3 = int(year3)
    length3Time = 0

    length2 = user_input2
    month2, day2, year2 = length2.split("/")
    month2 = int(month2)
    day2 = int(day2)
    year2 = int(year2)
    length2Time = 0

    length1 = user_input3
    month1, day1, year1 = length1.split("/")
    month1 = int(month1)
    day1 = int(day1)
    year1 = int(year1)
    length1Time = 0

    length0 = user_input4
    month0, day0, year0 = length0.split("/")
    month0 = int(month0)
    day0 = int(day0)
    year0 = int(year0)
    length0Time = 0

    def monthFinder(length3Time, year, month3, day3):
        is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        if month3 == 1:
            length3Time += day3
        elif month3 == 2:
            length3Time += 31
            length3Time += day3
        elif month3 == 3:
            length3Time += 60 if is_leap else 59
            length3Time += day3
        elif month3 == 4:
            length3Time += 91 if is_leap else 90
            length3Time += day3
        elif month3 == 5:
            length3Time += 121 if is_leap else 120
            length3Time += day3
        elif month3 == 6:
            length3Time += 152 if is_leap else 151
            length3Time += day3
        elif month3 == 7:
            length3Time += 182 if is_leap else 181
            length3Time += day3
        elif month3 == 8:
            length3Time += 213 if is_leap else 212
            length3Time += day3
        elif month3 == 9:
            length3Time += 244 if is_leap else 243
            length3Time += day3
        elif month3 == 10:
            length3Time += 274 if is_leap else 273
            length3Time += day3
        elif month3 == 11:
            length3Time += 305 if is_leap else 304
            length3Time += day3
        elif month3 == 12:
            length3Time += 335 if is_leap else 334
            length3Time += day3
        return length3Time

    length3Time = monthFinder(length3Time, year3, month3, day3)
    length2Time = monthFinder(length2Time, year2, month2, day2)
    length1Time = monthFinder(length1Time, year1, month1, day1)
    length0Time = monthFinder(length0Time, year0, month0, day0)

    if year3 == year2:
        distance32 = length3Time-length2Time
    elif year3 > year2:
        if year2 % 4 == 0 and (year2 % 100 != 0 or year2 % 400 == 0):
            distance32 = (length3Time + 366) - length2Time
        else:
            distance32 = (length3Time + 365) - length2Time
    else:
        distance32 = length3Time - length2Time

    if year2 == year1:
        distance21 = length2Time-length1Time
    elif year2 > year1:
        if year1 % 4 == 0 and (year1 % 100 != 0 or year1 % 400 == 0):
            distance21 = (length2Time + 366) - length1Time
        else:
            distance21 = (length2Time + 365) - length1Time
    else:
        distance21 = length2Time - length1Time

    if year1 == year0:
        distance10 = length1Time-length0Time
    elif year1 > year0:
        if year0 % 4 == 0 and (year0 % 100 != 0 or year0 % 400 == 0):
            distance10 = (length1Time + 366) - length0Time
        else:
            distance10 = (length1Time + 365) - length0Time
    else:
        distance10 = length1Time - length0Time

    total = distance32+distance21+distance10
    average = total/3

    print("The average is", int(average))
    next = length3Time+average

    nextYear = year3+1

    if next > 365:
        next -= 365
        result = (f"Project your next one to Weasel on 1/{int(next)}/{int(nextYear)}")
    elif next > 334:
        next -= 334
        result = (f"Project your next one to Weasel on 12/{int(next)}/{int(year3)}")
    elif next > 304:
        next -= 304
        result = (f"Project your next one to Weasel on 11/{int(next)}/{int(year3)}")
    elif next > 273:
        next -= 273
        result = (f"Project your next one to Weasel on 10/{int(next)}/{int(year3)}")
    elif next > 243:
        next -= 243
        result = (f"Project your next one to Weasel on 09/{int(next)}/{int(year3)}")
    elif next > 212:
        next -= 212
        result = (f"Project your next one to Weasel on 08/{int(next)}/{int(year3)}")
    elif next > 181:
        next -= 181
        result = (f"Project your next one to Weasel on 07/{int(next)}/{int(year3)}")
    elif next > 151:
        next -= 151
        result = (f"Project your next one to Weasel on 06/{int(next)}/{int(year3)}")
    elif next > 120:
        next -= 120
        result = (f"Project your next one to Weasel on 05/{int(next)}/{int(year3)}")
    elif next > 90:
        next -= 90
        result = (f"Project your next one to Weasel on 04/{int(next)}/{int(year3)}")
    elif next > 59:
        next -= 59
        result = (f"Project your next one to Weasel on 03/{int(next)}/{int(year3)}")
    elif next > 31:
        next -= 31
        result = (f"Project your next one to Weasel on 02/{int(next)}/{int(year3)}")
    return result