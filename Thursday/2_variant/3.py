s = input()
q = ''
for c in s:
    if c not in q:
        s_c = s.count(c)
        print(c,':', s_c)
        q += c