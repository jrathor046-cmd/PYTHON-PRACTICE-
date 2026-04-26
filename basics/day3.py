# Day 3 - If-Else Conditions

# Example 1: Check even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Example 2: Check positive, negative or zero
num2 = int(input("Enter another number: "))

if num2 > 0:
    print("Positive number")
elif num2 < 0:
    print("Negative number")
else:
    print("Zero")


# Example 3: Age check
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


# Example 4: Largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("A is greater")
elif b > a:
    print("B is greater")
else:
    print("Both are equal")
