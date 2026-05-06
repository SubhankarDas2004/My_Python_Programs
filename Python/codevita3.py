s,r=map(int,input().split())
l=list(map(int,input().split()))
output=[]
for i in range(r):
    low,high=map(int,input().split())
    c=0
    for e in l:
        if low<= e <=high:
            c=c+1

    output.append(str(c))
print(' '.join(output))
