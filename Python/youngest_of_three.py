'''Q2. If the ages of Ram, Shyam and Ajay are input through the keyboard, write a program to determine
the youngest of the three.'''
# Input ages
ram = int(input("Enter  Ram's age: "))
shyam = int(input("Enter Shyam's age: "))
ajay = int(input("Enter Ajay's age: "))

# Compare ages
if ram < shyam and ram < ajay:
    print("Ram is the youngest")
elif shyam < ram and shyam < ajay:
    print("Shyam is the youngest")
elif ajay < ram and ajay < shyam:
    print("Ajay is the youngest")
else:
    print("Two or more people have the same youngest age.")
