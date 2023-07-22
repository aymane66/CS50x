dollars = 0

while True:
    try:
        dollars = float(input("Change owed: "))
        if dollars < 0:
            print("Please insert a positive integer! ")
        else:
            break
    except Exception as e:
        print("ERROR: Please insert a number! ")

change = round(int(dollars * 100))

total = 0
while change > 0:
    if change >= 25:
        change -= 25
        total += 1
    elif change >= 10:
        change -= 10
        total += 1
    elif change >= 5:
        change -= 5
        total += 1
    else:
        change -= 1
        total += 1

print(total)