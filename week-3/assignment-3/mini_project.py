Day = input("What day is it? ").capitalize()
Time = input("What time of day? ").capitalize()
 
valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
valid_times = ["Morning", "Afternoon", "Evening"]
 
Suggestion = ""
 
if Day not in valid_days:
    Suggestion = "Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday..."
elif Time not in valid_times:
    Suggestion = "Sorry, I don't recognize that time. Try: morning, afternoon, or evening..."
 
elif Day == "Saturday" or Day == "Sunday":
    if Time == "Morning":
        Suggestion = "Sleep in a little, and have a good breakfast."
    elif Time == "Afternoon":
        Suggestion = "Go out with some friends!"
    elif Time == "Evening":
        Suggestion = "Perfect time for a movie or trying a new recipe."
 
elif Day == "Monday" or Day == "Tuesday":
    if Time == "Morning":
        Suggestion = "Time for class!"
    elif Time == "Afternoon":
        Suggestion = "This is time to study or work on projects."
    elif Time == "Evening":
        Suggestion = "Wind down and set yourself up for tomorrow."
 
elif Day == "Wednesday" or Day == "Thursday":
    if Time == "Morning":
        Suggestion = "Start with a few quiet minutes to meditate."
    elif Time == "Afternoon":
        Suggestion = "Take a walk!"
    elif Time == "Evening":
        Suggestion = "Catch up with friends over a call!"
 
elif Day == "Friday":
    if Time == "Morning":
        Suggestion = "Get a good breakfast to start the day!"
    elif Time == "Afternoon":
        Suggestion = "Wrap up any work left over!"
    elif Time == "Evening":
        Suggestion = "Celebrate as the weekend begins!"
 
print("Suggestion:", Suggestion)