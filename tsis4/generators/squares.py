def squares(a, b):
    while a <= b:
        yield a * a
        a += 1

a = int(input("Input first value: "))
b = int(input("Input second value: "))
print("Squares between first and second values: ", end='')
x = squares(a, b)
for i in x:
    print(i, end=' ')