n=int(input("enter limit:"))
i=1
c=0
k=int(input("enter the number u want to check multiple:"))
while i<=n:
    num=int(input("enter number:"))
    if(num%k==0):
        c=c+1
        if(c==1):
            print("only one multiple")
        else:
            print("multiples of",k,"are",num)
    else:
        print("no such multiples")
    i=i+1
