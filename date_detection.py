#! python3
#This program will check if a date that is inputted is valid. The date will be in
# DD/MM/YYYY format, check for years from 1000-2999, if it is a leap year, and if
# the date matches correctly with the month (ie. if the month has 30 or 31 days)


import re
import sys

# TODO: Create regex that for matching the date format DD/MM/YYYY

def date_input(data):

    date_regex = re.compile(r'''

    (\d\d) # Checks the day to see if it's in the correct format, either 0x or xx
    \/      # / symbol
    (\d\d)# Checks the month to see if it's in the correct format, either 0x or xx
    \/      # / symbol
    (\d\d\d\d)# checks the year if it's in the correct format either 1xxx or 2xxx

    ''', re.VERBOSE)

    while date_regex.search(data) == None:
        print('invalid. Please enter a new date in DD/MM/YYYY format')
        data = input()
    else:
        print('okay')
        print(date_regex.findall(data))
    raw_data = date_regex.findall(data)
    return raw_data
    




def store_data(data_match):
    
# Store the date into 3 variables (day, month, year) if the format is valid
    day = int(data_match[0][0])     #store day
    print('day : ' + str(day))
    month = int(data_match[0][1])   #store month
    print('month : ' + str(month))
    year = int(date_match[0][2])    #store year
    print('year : ' + str(year))


#Check the variables to see if they are a valid numbers in a calendar
    leap_year = 0    
    if (day > 31) or (month > 12) or (year < 1000 or year > 2999):  
        print("Sorry, the date you've chosen is out of the range")
        sys.exit()

#Check to see if the inputted date is a leap year        
    if (year%4 == 0 and year%100 != 0) or (year%400 ==0):
        print("this is a leap year")
        leap_year = 1
    else:
        print("this is not a leap year")

#Values corresponding to the different allowable dates depending on the month
    non_ly = 28
    pro_ly = 29
    long_months = [1,3,5,7,8,10,12]
    short_months = [2,4,6,9,11]
    
    print('the date: ' + str(day) + '/' + str(month) + '/' + str(year) + ' is a:')

#February checks
    if (month == 2) and (leap_year == 1) and (int(day) <= int(pro_ly)):
        print("Valid date!")
    elif (month == 2) and (leap_year == 0) and (day <= non_ly):
        print("Valid date!")
    elif (month == 2) and (day >= non_ly):
        print("Invalid date!")
#non-February checks
    elif (month in long_months) and (day <= 31):
        print("Valid date!")
    elif (month in short_months) and (day <= 30):
        print("Valid date!")
    else:
        print("Invalid date!!")


while True:
    date = input(r'input day in DD/MM/YYYY format between the year 1000 and 2999'+ '\n')
    if ((len(date) != 10) or
            (int(date[0]) > 1) or
            (int(date[3]) >= 1 and int(date[4]) > 3) or
            (int(date[6]) < 1 or int(date[6]) > 3)):
        print("Please input a real potential date")
        continue
    else:
        break
date_match = date_input(date)
store_data(date_match)
