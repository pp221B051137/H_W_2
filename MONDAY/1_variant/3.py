for i in range(100,999):
    n1 = int(i/100)
    n2 = int((i%100)/10)
    n3 = int((i%100)%10)
    if n1**3 + n2**3 + n3**3 == i:
        print(i)