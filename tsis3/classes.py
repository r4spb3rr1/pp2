#ex1
import math

class work_with_print:
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str)

wwp = work_with_print()
wwp.getString()
wwp.printString()


class Shape:
    def printArea(area = 0):
        print(area)

class Square(Shape):
    def __init__(self, lenght):
        self.lenght = lenght
        self.area = lenght * lenght
    def printArea(self):
        print(self.area)

class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
        self.area = lenght * width
    def printArea(self):
        print(self.area)


sq = Square(2)
sq.printArea()
sq = Rectangle(2, 3)
sq.printArea()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("x =", self.x, "y =", self.y)
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, another_point):
        print(math.sqrt((self.x - another_point.x) * (self.x - another_point.x) + (self.y - another_point.y) * (self.y - another_point.y)))

p1 = Point(3, 4)
p2 = Point(0, 0)
p1.dist(p2)

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount.")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 15] # some list of numbers
prime_numbers = list(filter(lambda x: is_prime(x), numbers))