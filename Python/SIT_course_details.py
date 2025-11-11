# SIT Course Fee Calculator using Nested If-Else

# Taking inputs
course_code = int(input("Enter course code (1-7): "))
TIGans = int(input("Is the student from Techno India Group? (1-Yes / 0-No): "))
entrance_test = int(input("Has the student qualified the entrance test? (1-Yes / 0-No): "))
Male = int(input("Enter gender (1-Male / 0-Female): "))

# Assigning course details
if course_code == 1:
    course_name, sem, admission, remaining, type_ = "BTech", 8, 100000, 75000, "UG"

elif course_code == 2:
    course_name, sem, admission, remaining, type_ = "BCA", 8, 70000, 50000, "UG"

elif course_code == 3:
    course_name, sem, admission, remaining, type_ = "BBA", 8, 70000, 50000, "UG"

elif course_code == 4:
    course_name, sem, admission, remaining, type_ = "BHHA", 6, 60000, 45000, "UG"

elif course_code == 5:
    course_name, sem, admission, remaining, type_ = "BSc", 6, 50000, 30000, "UG"

elif course_code == 6:
    course_name, sem, admission, remaining, type_ = "MBA", 4, 140000, 100000, "PG"

elif course_code == 7:
    course_name, sem, admission, remaining, type_ = "MCA", 4, 120000, 80000, "PG"

else:
    print("Invalid course code!")
    exit()

# Now calculating total fees
if TIGans == 1:
    # Student is from Techno India Group
    if type_ == "UG":
        per_sem_scholar = 10000
    else:
        per_sem_scholar = 15000

    admission_fee = admission - per_sem_scholar
    remaining_fee = (sem - 1) * (remaining - per_sem_scholar)
    total_fee = admission_fee + remaining_fee

else:
    # Student is NOT from TIG
    admission_fee = admission
    remaining_fee = (sem - 1) * remaining

    # Check entrance test qualification
    if entrance_test == 1:
        admission_fee = admission_fee - 15000
        # Check gender for additional scholarship
        if Male == 0:
            admission_fee = admission_fee - 10000
        else:
            admission_fee = admission_fee
    else:
        # No entrance scholarship
        if Male == 0:
            admission_fee = admission_fee - 10000
        else:
            admission_fee = admission_fee

    total_fee = admission_fee + remaining_fee

# Displaying final result
print("\n--- SIT Course Fee Details ---")
print("Course Name:", course_name)
print("Course Type:", type_)
print("Total Semesters:", sem)
#print("Total Course Fee: ₹", format(total_fee, ",.2f"))
print("Total Course Fee: ₹",total_fee)
