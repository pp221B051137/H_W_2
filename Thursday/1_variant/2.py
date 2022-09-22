n = int(input())
num = []
n1 = int(n/10000)
n2 = int((n%10000)/1000)
n3 = int(((n%10000)%1000)/100)
n4 = int((((n%10000)%1000)%100)/10)
n5 = int(((((n%10000)%1000)%100)%10))
num.append(n1)
num.append(n2*2)
num.append(n3)
num.append(n4*2)
num.append(n5)
for i in num:
    print(i, end ='')