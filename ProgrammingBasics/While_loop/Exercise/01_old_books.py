target_book = input()

user_input = input()
books_searched = 0

while (user_input != "No More Books") and (user_input != target_book):
    books_searched += 1

    user_input = input()

if target_book == user_input:
    print(f"You checked {books_searched} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_searched} books.")
