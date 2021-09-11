run = True
while True:
    input_value = input("Enter year or type 'Exit' to quit:")
    if input_value.capitalize() == "Exit":
          break
    if input_value.capitalize() != "Exit" and input_value.isnumeric() == False:
        print("Invalid entry") 
    else:
      year = int(input("Enter year to be checked:"))
    if(year%4 == 0 and year%100 != 0):
                print("The year is a leap year!")
    else:
                print("The year isn't a leap year!")
    if(input_value).capitalize() == "Exit":
            break
    else:
                print("year out of range!")