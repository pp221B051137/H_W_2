d = True
while(d):
    n = int(input("Guess: "))
    if n > 76:
        print("The number is fewer")
    elif n < 76:
        print("The number is more")
    elif n == 76:
        print("BINGO!")
        d = False