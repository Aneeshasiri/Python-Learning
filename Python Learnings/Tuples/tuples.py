# Tuples = Collection which is ordered and unchangeable used to group together related data

student = ("Aneesha", 25, "female")

print(student.count("Aneesha"))
print(student.index("female"))

for x in student:
    print(x)

if "Bro" in student:
    print("Aneesha is here")