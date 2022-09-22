a = map(int,input('Enter numbers: ').split())
l = list(a)
l.sort()
l_new = []
try:
    for x in range(len(l)):
        if l[x]%2 != 0:
            l_new.append(l[x])
    print('Output: ',l_new[0])

except:
    print('Output: ',"not found")