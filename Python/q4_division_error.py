a = int(input("Enter numerator (a): "))
b = int(input("Enter denominator (b): "))

try:
    result = a / b
except ZeroDivisionError:
    result = "infinite"

print(f"Result of {a}/{b} = {result}")
