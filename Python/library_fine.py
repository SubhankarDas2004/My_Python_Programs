'''Q4. A library charges a fine for every book returned late. For first 5 days the fine is 50 paise, for 6-10
days fine is one rupee and above 10 days fine is 5 rupees. If you return the book after 30 days
your membership will be cancelled. Write a program to accept the number of days the member is
late to return the book and display the fine or the appropriate message'''

# Input number of late days
days = int(input("Enter the number of days late: "))

# Check fine conditions
if days <= 0:
    print("Invalid input. Days cannot be zero or negative.")
elif days <= 5:
    fine = days * 0.50
    print("Fine is ₹", fine)
elif days <= 10:
    fine = 5 * 0.50 + (days - 5) * 1
    print("Fine is ₹", fine)
elif days <= 30:
    fine = 5 * 0.50 + 5 * 1 + (days - 10) * 5
    print("Fine is ₹", fine)
else:
    print("Your membership has been cancelled due to late return.")
