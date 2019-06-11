
# Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

def centuryFromYear(year):
    
    digits = list(str(year))

    if len(digits) < 3:
        return 1
    
    century = ""
    century = century.join(digits[:-2])
    
    if digits[-2:] == ['0', '0']:
        return int(century)

    return int(century) + 1


assert(centuryFromYear(1901) == 20)
assert(centuryFromYear(10) == 1)
assert(centuryFromYear(1234) == 13)
assert(centuryFromYear(1700) == 17)
