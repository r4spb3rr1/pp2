#ex 1
thistuple = ("apple", "banana", "cherry")
print(thistuple)


#ex 2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


#ex 3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


#ex 4
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


#ex 5
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


#ex 6
tuple1 = ("abc", 34, True, 40, "male")


#ex 7
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


#ex 8
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


#ex 9
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


#ex 10
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


#Ex 11
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


#ex 12
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#ex 13
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


#Ex 14
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


#ex 15
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")


#ex 16
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


#ex 17
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


#ex 18
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


#ex 19
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


#ex 20
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)


#ex 21
fruits = ("apple", "banana", "cherry")


#ex 22
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


#ex 23
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


#ex 24
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


#ex 25
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


#ex 26
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


#ex 27
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


#ex 28
  tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


#ex 29
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

