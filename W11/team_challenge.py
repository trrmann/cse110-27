#! python
import os

#! python
hr_data = []
with open("hr_system.txt") as books_file:
    for line in books_file:
        #print(line.strip())
        hr_data.append(line.strip().split(" "))
        #print(f"{hr_data[len(hr_data)-1][0]} (ID:  {hr_data[len(hr_data)-1][1]}), {hr_data[len(hr_data)-1][2]} - ${float(hr_data[len(hr_data)-1][3]):.2f}")
        #print(f"{hr_data[len(hr_data)-1][0]} (ID:  {hr_data[len(hr_data)-1][1]}), {hr_data[len(hr_data)-1][2]} - ${float(hr_data[len(hr_data)-1][3])/24:.2f}")
        if hr_data[len(hr_data)-1][2] == "Engineer":
            print(f"{hr_data[len(hr_data)-1][0]} (ID:  {hr_data[len(hr_data)-1][1]}), {hr_data[len(hr_data)-1][2]} - ${(float(hr_data[len(hr_data)-1][3])/24)+1000.0:.2f}")
        else:
            print(f"{hr_data[len(hr_data)-1][0]} (ID:  {hr_data[len(hr_data)-1][1]}), {hr_data[len(hr_data)-1][2]} - ${float(hr_data[len(hr_data)-1][3])/24:.2f}")
