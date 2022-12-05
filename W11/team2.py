#!python
with open("hr_system.txt") as file:
    for line in file:
        fields = line.strip().split(" ")
        name = fields[0]
        id = fields[1]
        title = fields[2]
        salary = float(fields[3])/24
        if title.lower() == "engineer": salary += 1000
        print(f"{name} (ID:  {id}), {title} - ${salary:.2f}")
