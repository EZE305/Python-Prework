def is_leap_year(a_year):

    # If a given year is divisible by 4 and also not divisible by 100; it is a leap year (True)
    if (a_year % 4 == 0) and (a_year % 100 != 0):
        leap = True
    #If the given year is divisible by 400; it is a leap year (True)
    elif (a_year % 400 == 0):
        leap = True
    #If the given year is divisible by 100, but not by 400 it is not a leap year (False)
    elif (a_year % 100 == 0) and (a_year % 400 != 0):
        leap = False
    # Any other number that does't meet any of these conditions is not a leap year (False)
    else: 
        leap = False
    return leap

print(is_leap_year(1940))