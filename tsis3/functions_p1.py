import math
import random

def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

def solve(num_heads, num_legs):
    for num_chickens in range(num_heads + 1):
        num_rabbits = num_heads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == num_legs:
            return num_chickens, num_rabbits
    return None

def filter_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return list(filter(lambda x: is_prime(x), numbers))

def get_permutations(input_str, start=0):
    if start == len(input_str) - 1:
        print(''.join(input_str))
    else:
        for i in range(start, len(input_str)):
            input_str[start], input_str[i] = input_str[i], input_str[start]
            get_permutations(input_str, start + 1)
            input_str[start], input_str[i] = input_str[i], input_str[start]


def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def spy_game(nums):
    code = [0, 0, 7]
    index = 0
    for num in nums:
        if num == code[index]:
            index += 1
            if index == len(code):
                return True
    return False

def sphere_volume(radius):
    volume = (4 / 3) * 3.141592653589793 * (radius ** 3)
    return volume

def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

def is_palindrome(word):
    return word == word[::-1]

def histogram(numbers):
    for num in numbers:
        print('*' * num)

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    num_guesses = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        num_guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
            break
    
