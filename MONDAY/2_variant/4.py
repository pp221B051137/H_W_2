import re
password = list(input().split(','))
empty = []
for w in password:
    x = re.findall("[a-zA-Z]",w)
    y = re.findall("[0-9]",w)
    z = re.findall("[$#@]",w)
    if x != empty and y!= empty and z!= empty and len(w) >= 6 and len(w) <=12:
        print(w)