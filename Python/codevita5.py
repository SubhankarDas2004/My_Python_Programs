t=int(input("Number of test cases:"))
while t!=0:
    n=int(input("number of boxes:"))
    b=input("Enter the number of candies in each box:").split()
    c=list(map(int,b))
    s=c[0]+c[1]
    v=s
    for i in range(2,n):
        s+=c[i]
        v+=s

    print(f"Minimum time required:{v} seconds")
    t-=1
