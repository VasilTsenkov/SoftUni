text = input()

length = len(text)
points = 0

for char in range(0, length):
    if text[char] == 'a':
        points += 1
    elif text[char] == 'e':
        points += 2
    elif text[char] == 'i':
        points += 3
    elif text[char] == 'o':
        points += 4
    elif text[char] == 'u':
        points += 5

print(f"{points}")
