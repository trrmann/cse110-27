#! python
with open("books.txt") as books_file:
    for line in books_file:
        if line.strip() != "": print(f"{line.strip()}")