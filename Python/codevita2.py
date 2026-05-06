p=int(input("enter principal:"))
t=int(input("enter tenure:"))
n1=int(input("enter slabs of bank1:"))
#for bank A
emiA=0
for a in range(n1):
    #bank A details
    yearA=float(input("enter year:"))
    iA=float(input("enter interest:"))
    emi=p*iA/(1-1/(1+iA)**(yearA*12))
    emiA=emiA+emi
print(p)

n2=int(input("enter slabs of bank2:"))
emiB=0
for a in range(n2):
    #bank B details
    yearB=float(input("enter year:"))
    iB=float(input("enter interest:"))
    emi1=p*iB/(1-1/(1+iB)**(yearB*12))
    emiB=emiB+emi1

print(emiA)
print(emiB)
if(emiB>emiA):
    print("bank A")
else:
    print("bank B")
