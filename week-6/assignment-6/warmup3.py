def adding(numb):
    total = numb + 10 
    print(total)

adding(5)

# print (total)
# NameError: name 'total' is not defined


def adding_fix(numb):
    total = numb + 10
    return f"This is the total: {total}"

the_total= adding_fix(4)
print(the_total)
