def get_permutations(input_str, start=0):
    if start == len(input_str) - 1:
        print(''.join(input_str))
    else:
        for i in range(start, len(input_str)):
            input_str[start], input_str[i] = input_str[i], input_str[start]
            get_permutations(input_str, start + 1)
            input_str[start], input_str[i] = input_str[i], input_str[start]

get_permutations(list(input("Enter a string: ")))


def histogram(numbers):
    for num in numbers:
        print('*' * num)

histogram([4, 9, 7])


def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome(input()))
