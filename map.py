# START
import random

# 3
random_list: list[int] = [random.randint(-50, 50) for i in range(20)]
print(random_list)

print(f"To the power of 3:{list(map(lambda num: num ** 3, random_list))}")
print(f"Ones:{list(map(lambda num: (num % 10 if num >= 0 else (num * -1) % 10), random_list))}")
print(f"Fahrenheit:{list(map(lambda num: (num * 1.8) + 32, random_list))}")
print(f"Negative or positive:{list(map(lambda num: ("positive" if num > 0 else "negative"), random_list))}")

# 4
fruit_list: list[str] = ["Mango", "Orange", "Banana", "Apple", "Strawberry", "Pineapple", "Grapes", "Watermelon"]
print(f"Reversed: {list(map(lambda fruit: fruit[::-1], fruit_list))} ")
print(f"First letter: {list(map(lambda fruit: fruit[0], fruit_list))}")
print(f"Middle letter: {list(map(lambda fruit: fruit[len(fruit) // 2], fruit_list))}")
print(f"Ends with s, add !: {list(map(lambda fruit: fruit + "!" if fruit.endswith("s") else fruit, fruit_list))}")

# 5
# global in a function means that there is a variable outside the function and using it means we want to do somthing
# with this variable.
# the disadvantage in using global is that it makes the code less readable, and also it may cause problems within the
# functions, because if there is an error in the code, it's more difficult to find the error itself.
# in the future using a global inside a code will cause the user difficulties especially if the code is long, because
# the user will have to go line by line in order to find an error, and he will have to coordinate between the functions
# in his code to make sure they all work based on the global.
x: int = 1
def foo():
    print(x)
x = 4
foo()
# the reason we will get an error is that we didn't mention that the x we want to print is global.
