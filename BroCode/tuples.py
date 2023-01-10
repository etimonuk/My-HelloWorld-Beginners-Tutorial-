# tuple = collection which is ordered and unchangeable
#           used to group together related data

students = ("Bro", 21, "male")

print(students.count("Bro"))
print(students.index("male"))

for x in students:
    print(x)

if "Bro" in students:
    print("Bro is here")

