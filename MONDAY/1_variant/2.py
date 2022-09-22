n = int(input())

n1 = int(n/100)
n2 = int((n%100)/10)
n3 = int(((n%100)%10))

if n1 < n2 and n2 < n3:
    print("Yes")
else:
    print("NO")