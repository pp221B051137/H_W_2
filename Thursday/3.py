# n = str(input())
# s1 = 'abcdefghijklmnopqrstuvwxyz'
# s2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
# for i in s2:
#     for x in range(len(s1)):
#         if i == x:
#             s1[x] = i
# for  
n = input()
s = []
for i in n:
    if i == 'a' or i == "A": s.append(1)
    elif i == 'b' or i == 'B': s.append(2)
    elif i == 'c' or i == 'C': s.append(3)
    elif i == 'd' or i == 'D': s.append(4)
    elif i == 'e' or i == 'E': s.append(5)
    elif i == 'f' or i == 'F': s.append(6)
    elif i == 'g' or i == 'G': s.append(7)
    elif i == 'h' or i == 'H': s.append(8)
    elif i == 'i' or i == 'I': s.append(9)
    elif i == 'j' or i == 'J': s.append(10)
    elif i == 'k' or i == 'K': s.append(11)
    elif i == 'l' or i == 'L': s.append(12)
    elif i == 'm' or i == 'M': s.append(13)
    elif i == 'n' or i == 'N': s.append(14)
    elif i == 'o' or i == 'O': s.append(15)
    elif i == 'p' or i == 'P': s.append(16)
    elif i == 'q' or i == 'Q': s.append(17)
    elif i == 'r' or i == 'R': s.append(18)
    elif i == 's' or i == 'S': s.append(19)
    elif i == 't' or i == 'T': s.append(20)
    elif i == 'u' or i == 'U': s.append(21)
    elif i == 'v' or i == 'V': s.append(22)
    elif i == 'w' or i == 'W': s.append(23)
    elif i == 'x' or i == 'X': s.append(24)
    elif i == 'y' or i == 'Y': s.append(25)
    elif i == 'z' or i == 'Z': s.append(26) 
for x in s:
    print(x, end= " ")