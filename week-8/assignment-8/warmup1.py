while True:
    question = input("Enter a number: ")
    try:
        number= float(question)
    except ValueError:
        print("That's not a valid number. Try again.")
        continue
    print(f"You entered: {number}")
    break