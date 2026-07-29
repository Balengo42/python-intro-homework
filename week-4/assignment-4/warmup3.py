programming_languages_1= ["Python", "Java", "C++", "JavaScript", "Ruby"]
programming_languages_2= ["Go", "Java", "Kotlin", "C++", "TypeScript"]

set_1= set(programming_languages_1)
set_2= set(programming_languages_2)

union= set_1.union(set_2)
intersection= set_1.intersection(set_2)
difference= set_1.difference(set_2)

print("Union: ", union)
print("Intersection: ", intersection)
print("Difference: ", difference)
