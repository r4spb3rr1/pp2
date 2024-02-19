def down_to_n(n):
    while n != -1:
        yield n
        n -=1

n = int(input("Input value: "))
x = down_to_n(n)
print("Values from n to zero: ", end='')
for i in x:
    print(i, end=' ')