def check_number(n):
    a = 1
    while a < n:
        if a % 3 == 0 and a % 4 == 0:
            yield a
        a += 1

n = int(input("Input the value: "))
x = check_number(n)
print("Numbers between zero and your value, which divisible by 3 and 4: ", end='')
for i in x:
    print(i, end=' ')