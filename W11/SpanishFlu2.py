low_entity = ""
low_year = ""
low_data = 1000
high_entity = ""
high_year = ""
high_data = -1
min_year = 5000
max_year = 0
target_year = int(input(f"Enter the year of interest: "))
total = 0
count = 0
max_entity = ""
max_data = -1
min_entity = ""
min_data = 1000
with open("life-expectancy.csv") as data_file:
    for line in data_file: #Entity, Code, Year, Life expectancy (years)
        parser = line.strip().split(",")
        if parser[0] == "Entity" and parser[1] == "Code" and parser[2] == "Year" and parser[3] =="Life expectancy (years)": pass
        else:
            entity = parser[0]
            code = parser[1]
            year = int(parser[2])
            expectancy = float(parser[3])
            if low_data > expectancy:
                low_data = expectancy
                low_entity = entity
                low_year = year
            if high_data < expectancy:
                high_data = expectancy
                high_entity = entity
                high_year = year
            if year==target_year:
                total += expectancy
                count += 1
                if min_data > expectancy:
                    min_data = expectancy
                    min_entity = entity
                if max_data < expectancy:
                    max_data = expectancy
                    max_entity = entity
if count==0:  average = 0
else:  average = total / count

print(f"\nThe overall max life expectancy is: {high_data} from {high_entity} in {high_year}")
print(f"The overall min life expectancy is: {low_data} from {low_entity} in {low_year}")
print(f"\nFor the year {target_year}: ")
print(f"The average life expectancy across all countries was {average:.2f}")
print(f"The max life expectancy was in {max_entity} with {max_data}")
print(f"The min life expectancy was in {min_entity} with {min_data}")
