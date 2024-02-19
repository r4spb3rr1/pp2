import math
#Area = (number of sides × length of one side × apothem)/2,
# Apothem = [(length of one side)/{2 ×(tan(180/number of sides))}].
n = int(input("Input nuber of sides: "))
a = int(input("Input the lenght of a side: "))
print("The area of the polygon is:", n * a * a / (2 * round(math.tan(math.pi / n))) / 2)
