while True:

    try:  
        numerator = float(input("Enter the numerator: "))
        denominator= float(input("Enter the denominator: "))

        division = (numerator/denominator)
        print (f"{numerator} ÷ {denominator} = {division}")
        break
    except ZeroDivisionError:
        print("Can't divide by zero - please try a non-zero denominator.")
        continue
