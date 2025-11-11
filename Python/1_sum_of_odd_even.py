#initializing
i=1
sum1=0
sum2=0
#applying condition
while i<=10:
    #taking input
    num=int(input("enter number:"))
    #checking for even 
    if(num%2==0):
        sum1=num+sum1
    #checking for odd
    else:
        sum2=num+sum2
    i=i+1
#displaying output
print("Sum of even integers",sum1)
print("sum of odd integers",sum2)
