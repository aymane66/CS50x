text = input("Insert text: ")


letters = 0
words = 1
sentences = 0

for l in range(len(text)):
    if text[l].isalpha():
        letters += 1
    elif text[l].isspace():
        words += 1
    elif text[l] == '.' or text[l] == '!' or text[l] == '?':
        sentences += 1

l = letters / words * 100
s = sentences / words * 100

index = 0.0588 * l - 0.29 * s - 15.8
index = round(index)

if index > 16:
    print("Grade 16+")
elif index > 1 and index < 17:
    print(f"Grade {index}")
else:
    print("Before Grade 1")
