#enter amount for denomination
Amount=int(input("Enter amount:"))
#calculating for hundred notes
h=int(Amount/100)
na=int(Amount%100)
#calculating for fifty notes
fif=int(na/50)
nna=int(na%50)
#calculating for ten
ten=int(nna/10)
#printing
print("Hundreds=",h)
print("fiftys=",fif)
print("ten=",ten)
