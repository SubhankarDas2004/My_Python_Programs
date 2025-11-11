num=int(input("enter a number:"))
n1=num//10000
r1=num%10000
n2=r1//1000
r2=r1%1000
n3=r2//100
r3=r2%100
n4=r3//10
r4=r3%10
n5=r4
nn1=(n1+1)%10
nn2=(n2+1)%10
nn3=(n3+1)%10
nn4=(n4+1)%10
nn5=(n5+1)%10
out_num=(nn1*10000)+(nn2*1000)+(nn3*100)+(nn4*10)+nn5
print("Output number is:",out_num)
