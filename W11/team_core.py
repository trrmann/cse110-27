#! python
hr_data = []
with open("hr_system.txt") as books_file:
    for line in books_file:
        print(line.strip())
        hr_data.append(line.strip().split(" "))
        print(f"Name:  {hr_data[len(hr_data)-1][0]}, Title:  {hr_data[len(hr_data)-1][2]}")
