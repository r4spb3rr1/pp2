#ex 1
thisset = {"apple", "banana", "cherry"}
print(thisset)


#ex 2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


#ex 3
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)


#ex 4
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)


#ex 5
thisset = {"apple", "banana", "cherry"}

print(len(thisset))


#ex 6
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


#ex 7
set1 = {"abc", 34, True, 40, "male"}


#ex 8
myset = {"apple", "banana", "cherry"}
print(type(myset))


#ex 9
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


#ex 10
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


#ex 11
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


#ex 12
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


#ex 13
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


#ex 14
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


#ex 15
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


#ex 16
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


#ex 17
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)


#ex 18
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


#ex 19
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)


#ex 20
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


#ex 21
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


#ex 22
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


#ex 23
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)


#ex 24
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


#ex 25
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)


#ex 26
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)


#ex 27
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)