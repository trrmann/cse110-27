#! python
import os
max_chapters = 0
max_chapters_book = ""
max_chapters_scripture = ""
with open("books_and_chapters.txt") as books_file:
    for line in books_file:
        line = line.strip()
        fields = line.split(":")
        book = fields[0].strip()
        chapters = int(fields[1].strip())
        scripture = fields[2].strip()
        print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")
        if chapters > max_chapters:
            max_chapters = chapters
            max_chapters_book = book
            max_chapters_scripture = scripture
print(f"\nThe book with the largest number of chapters is {max_chapters_book} with {max_chapters} chapters in the {max_chapters_scripture}.")