n = int(input())
def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)
sum_all = 0
for i in range(3,n+1):
    sum = i*2*fac(i)
    sum_all = sum_all+sum
print(3+sum_all)

