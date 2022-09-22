import math
x = int(input('x = '))
y = int(input('y = '))

try:
    s = math.sqrt(x-y)
    s_1 = round(s,3)
    print('Output:',s_1)
except:
    print('Output: plz enter valid numbers')