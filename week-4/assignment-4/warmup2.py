student = {"Name": "Aidan Chan", "Grade": 12 , "Subjects": ["AP Calculus", "AP Chemistry", "AP World History", "AP English Language"]}
#Print each key-value pair using .items in for loop
for key, value in student.items():
    print(key, ":", value)

#Adding a new key "Graduated" with the value False
student["Graduated"] = False

#Print the updated dictionary
print(student)