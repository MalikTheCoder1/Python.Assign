num = int(input("Enter a number for multiplication table: "))
table = [num * i for i in range(1, 11)]
print("Multiplication Table:", table)
