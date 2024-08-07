#https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
#calendar-module
#code
import calendar
def find_day(date):
    month, day, year = map(int, date.split())
    day_index = calendar.weekday(year, month, day)
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    return days[day_index]
date = input().strip()
print(find_day(date))