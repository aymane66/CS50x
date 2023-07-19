height = 0

while height < 1 or height > 8:

    try:
        height = int(input("Height of pyramid (between 1 and 8): "))
        if height < 1 or height > 8:
            print("ERROR: Height must be between 1 and 8.")

    except Exception as e:
        print("ERROR: Invalid input. Please enter a valid integer.")

for i in range(1, height + 1):
    for j in range(height - i):
        print(" ", end="")
    for s in range(i):
        print("#", end="")
    print()