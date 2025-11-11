#input the basic salary
bs=float(input("basic salary:"))
#finding dearness allowances
d_al=bs*(40/100)
#finding house rent
hrent=bs*(20/100)
#calculating gross salary
gs=bs+d_al+hrent
#printing
print("Gross salary is:",gs)
