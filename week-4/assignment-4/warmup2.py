student = {"name": "Aidan Chan", "grade": 12 , "subjects": ["AP Calculus", "AP Chemistry", "AP World History", "AP English Language"]}
#Print each key-value pair using .items in for loop
for key, value in student.items():
    print(key, ":", value)

#Adding a new key "Graduated" with the value False
student["graduated"] = False

#Print the updated dictionary
print(student)