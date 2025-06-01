a = 0
b = 10

try:
    print("Result:", b / a)
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")

print("Continuing with the rest of the program...")