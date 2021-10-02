while True:
    def CheckYear(year):
        if (year % 4) == 0:
            if (year % 100) == 0:
             if (year % 400) == 0:
                return True
        else:
                return False
        else:
                return True
        else:
                return False
            year = 3200
            if(CheckYear(year)):
                print("Leap Year")
                else:
                    print("It is not a Leap Year")