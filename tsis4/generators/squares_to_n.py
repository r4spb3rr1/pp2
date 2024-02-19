def squaeres_to_n(n):
    a = 1
    while a <= n:
        yield a * a
        a += 1

n = int(input("Input the number: "))
x = squaeres_to_n(n)
for i in x:
    print("Square -", i)
    