num = int(input("Enter a number to save its multiplication table: "))

with open("Tables.txt", "w") as f:
    f.write(f"Multiplication Table of {num}:
")
    for i in range(1, 11):
        f.write(f"{num} x {i} = {num * i}\n")

print("Multiplication table saved to Tables.txt.")
