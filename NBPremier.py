def NBP(n: int):
    a: int = 2
    while a <= (n / 2) and n % a != 0:
        a += 1
    if a > (n / 2) and n > 1:
        print(n, " est un nombre premier")
    else:
        print(n, " n est pas un nombre premier")


i = int(input("saisir un nombre : "))

NBP(i)
