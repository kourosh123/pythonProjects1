from math import *
numbers = [23,6,45,1.2,8.9]
products = ["pen", "paper", "glasses", "microphone"]
products[1] = "shoes"
print(products[2:])
print(products[1:3])
products.extend(numbers)
print(products)
products.append("class")
print(products)
products.insert(2,"yellow")
print(products)
products.remove("pen")
print(products)
products.pop()
print(products.count("shoes"))
products.clear()
print(products)
products.append("music")
products.append("play")
products.append("alpha")
products.sort()
print(products)
products.reverse()
print(products)
products2 = products.copy()
print(products2)
print(products2.count("play"))
products.extend(products2)
print(products)
print(products.count("play"))
coordinate = (4,5)
print(coordinate[0])
alex = [(3,4),(4,5),(6,7)]
print(alex)
print(alex[2])
alex.insert(3, (4,6))
print(alex)
def say_hi(name, age, color):
    print(" How are you " + name + " you are " + str(age) + " with " + color + " hair!")

say_hi("kourosh",33.6,"brown")

def cube(num):
    return num*num*num


print(cube(76))



