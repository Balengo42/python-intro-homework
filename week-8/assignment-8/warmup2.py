while True:
    numerator = float(input("Enter the numerator: "))
    denominator= float(input("Enter the denominator: "))
    try: 
        division = (numerator/denominator)
        print (f"{numerator} ÷ {denominator} = {division}")
        break
    except ZeroDivisionError:
        print("Cant't divide by zero - please try a non-zero denominator")
        continue
