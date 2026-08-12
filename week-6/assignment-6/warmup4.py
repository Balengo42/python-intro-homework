def is_valid_score(score):
    
    if score >= 0 and score <= 100:
        return True 
    else:
        return False
        

score = int(input("What is you score: "))

if is_valid_score(score):
    print("Valid Score.")
else:
    print("Invalid score — must be between 0 and 100.")


