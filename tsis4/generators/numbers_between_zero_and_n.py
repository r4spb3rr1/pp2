def print_number_between_zero_and_n(n):
    a = 1
    while a < n - 1:
        yield a
        a += 1

n = int(input("Input the number: "))

x = print_number_between_zero_and_n(n)
print("Numbers between zero and your numbers: ", end='')
for i in x:
    print(i, end=',')
print(n - 1)