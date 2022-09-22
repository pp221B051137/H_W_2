n1 = int(input("UP "))
n2 =int(input("DOWN "))
n3 = int(input("LEFT "))
n4 = int(input("RIGHT "))
x = 0
y = 0
y = y+n1
y = y-n2
x = x-n3
x = x+n4
print(int(((x**2)+(y**2))**0.5))