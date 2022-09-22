n = int(input())
a_1 = n /1000
a_2 = int((n / 100)%10)
if int(n/1000) == int(n%1000)%100%10 and int((n /100)%10) == int((n % 100)/10):
    print(("yes"))
else:
    print("no")
