files = ["1.txt", "2.txt", "3.txt"]

for file in files:
    try:
        with open(file, "r") as f:
            print(f"{file} opened successfully.")
    except FileNotFoundError:
        print(f"{file} not found.")
