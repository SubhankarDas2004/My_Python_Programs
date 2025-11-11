'''Q1. If cost price and selling price of an item is input through the keyboard, write a program to
determine whether the seller has made profit or incurred loss. Also determine how much profit he
made or loss he incurred'''

# Input cost price and selling price
cp=float(input("Enter Cost Price: "))
sp=float(input("Enter Selling Price: "))

# Check conditions
if sp > cp:
    profit = sp - cp
    print("The seller made a profit of ₹", profit)
elif cp > sp:
    loss = cp - sp
    print("The seller incurred a loss of ₹", loss)
else:
    print("No profit, no loss.")
