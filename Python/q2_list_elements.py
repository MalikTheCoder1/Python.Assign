lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for index, value in enumerate(lst, start=1):
    if index in [3, 5, 7]:
        print(f"Element at position {index}: {value}")
