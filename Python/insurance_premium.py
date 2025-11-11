'''Q5. An Insurance company follows following rules to calculate premium.
● If a person’s health is excellent and the person is between 25 and 35 years of age and lives in a
city and is a male then the premium is Rs. 4 per thousand and his policy amount cannot exceed
Rs. 2 lakhs.
● If a person satisfies all the above conditions except that the sex is female then the premium is
Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 lakh.
● If a person’s health is poor and the person is between 25 and 35 years of age and lives in a village
and is a male then the premium is Rs. 6 per thousand and his policy cannot exceed Rs. 10,000.
● In all other cases the person is not insured.
Write a program to output whether the person should be insured or not, his/her premium rate and
maximum amount for which he/she can be insured.'''

# Input details
health = input("Enter health condition (excellent/poor): ")
age = int(input("Enter age: "))
location = input("Enter location (city/village): ")
sex = input("Enter sex (male/female): ")

# Check conditions
if health == "excellent" and 25 <= age <= 35 and location == "city" and sex == "male":
    print("The person is insured.")
    print("Premium rate: ₹4 per thousand")
    print("Maximum policy amount: ₹200000")
    coverage = int(input("Enter coverage amount: "))
    premium = 4 * (coverage//1000)
    print("Premium amount is: ", premium)

elif health == "excellent" and 25 <= age <= 35 and location == "city" and sex == "female":
    print("The person is insured.")
    print("Premium rate: ₹3 per thousand")
    print("Maximum policy amount: ₹100000")
    coverage = int(input("Enter coverage amount: "))
    premium = 3 * (coverage//1000)
    print("Premium amount is: ", premium)

elif health == "poor" and 25 <= age <= 35 and location == "village" and sex == "male":
    print("The person is insured.")
    print("Premium rate: ₹6 per thousand")
    print("Maximum policy amount: ₹10000")
    coverage = int(input("Enter coverage amount: "))
    premium = 6 * (coverage//1000)
    print("Premium amount is: ", premium)

else:
    print("The person is not insured based on the given conditions.")
