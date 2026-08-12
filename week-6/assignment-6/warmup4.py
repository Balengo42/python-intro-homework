def is_valid_score(score):
    
    if score <=100 and score >=0 :
        return True 
    
    else:
        return False
        

score = int(input("What is you score: "))

if is_valid_score(score):
    print("Valid Score")
else:
    print("Invalid score - must be between - 0 and 100.")


