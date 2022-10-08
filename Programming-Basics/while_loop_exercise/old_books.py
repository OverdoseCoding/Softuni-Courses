book = str(input())
book_counter = 0
while True:
    all_books = str(input())

    if all_books == "No More Books":
        print('The book you search is not here!')
        print(f'You checked {book_counter} books.')
        break

    if all_books == book:
        print(f'You checked {book_counter} books and found it.')
        break
        
    book_counter += 1