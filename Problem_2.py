
# Write a python program to calculate the number of days between two dates
from datetime import date

def dateinput(string : str):
    try:
        user_date = input("Enter your %s " %(string))
        year = user_date[0:4]
        month = user_date[3:6]
        day = user_date[6:]
        return year,month,day
    except:
        print("Enter format is not correct . it should in yyyymmdd")


date1 = dateinput("First date")
date2 = dateinput("second date")
date1 = date(int(date1[0]),int(date1[1]),int(date1[2]))
date2 = date(int(date2[0]),int(date2[1]),int(date2[2]))
difference = date2 - date1
print("Difference Between Entered days are %s" %(difference.days))










