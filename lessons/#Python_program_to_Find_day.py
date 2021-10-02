# Python program to find day of the week for a given date
while True:
    import datetime
    import calendar
    def findDay(date):
        born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
        return (calendar.day_name[born])
 
# Driver program
    date = '04 07 1962'
    print(findDay(date))
    print("Python Program To Find Day Of The Week For A Given Date") 
    quit()