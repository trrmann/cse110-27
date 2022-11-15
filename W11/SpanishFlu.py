#! python
data = {}
low = {"Entity":"", "Year":"", "Data":1000}
high = {"Entity":"", "Year":"", "Data":-1}
min_year = 5000
max_year = 0
with open("life-expectancy.csv") as data_file:
    for line in data_file: #Entity, Code, Year, Life expectancy (years)
        parser = line.strip().split(",")
        if parser[0] == "Entity" and parser[1] == "Code" and parser[2] == "Year" and parser[3] =="Life expectancy (years)": pass
        elif parser[0] in data.keys():
            if data[parser[0]]["Code"] == parser[1]:
                data[parser[0]]["Data"][int(parser[2])] = float(parser[3])
                if low["Data"] > float(parser[3]):
                    low["Data"] = float(parser[3])
                    low["Entity"] = parser[0]
                    low["Year"] = int(parser[2])
                if high["Data"] < float(parser[3]):
                    high["Data"] = float(parser[3])
                    high["Entity"] = parser[0]
                    high["Year"] = int(parser[2])
                if int(parser[2]) > max_year: max_year = int(parser[2])
                if int(parser[2]) < min_year: min_year = int(parser[2])
            else:
                raise Exception(f"Unexpected Data - Code {parser[1]} does not match previous code{data[parser[0]]['Code']} for entity {parser[0]}!")
        else:
            data[parser[0]] = {}
            data[parser[0]]["Code"] = parser[1]
            data[parser[0]]["Data"] = {}
            data[parser[0]]["Data"][int(parser[2])] = float(parser[3])
            if low["Data"] > float(parser[3]):
                low["Data"] = float(parser[3])
                low["Entity"] = parser[0]
                low["Year"] = int(parser[2])
            if high["Data"] < float(parser[3]):
                high["Data"] = float(parser[3])
                high["Entity"] = parser[0]
                high["Year"] = int(parser[2])
target_year = min_year - 1
while target_year < min_year or target_year > max_year:
    try:
        target_year = int(input(f"Enter the year of interest (from {min_year} to {max_year}): "))
        err = None
    except ValueError as vErr:
        err = vErr
        if str(vErr) == "invalid literal for int() with base 10: ''": target_year = max_year
    except KeyboardInterrupt:
        target_year = max_year
        print()
    finally:
        if (target_year < min_year or target_year > max_year) and err == None:  print(f"No data is available for {target_year}")

print(f"\nThe overall max life expectancy is: {high['Data']} from {high['Entity']} in {high['Year']}")
print(f"The overall min life expectancy is: {low['Data']} from {low['Entity']} in {low['Year']}")

total = 0
count = 0
max = {"Entity":"", "Data":-1}
min = {"Entity":"", "Data":1000}
improved = {"best" : {"fromLast" : {"Entity":"", "Data":-1000},
                 "toNext" : {"Entity":"", "Data":-1000}},
            "worst" : {"fromLast" : {"Entity":"", "Data":1000},
                 "toNext" : {"Entity":"", "Data":1000}}
           }

for index, key in enumerate(data):
    code = data[key]["Code"]
    years = data[key]["Data"]
    for yr_index, year in enumerate(years):
        expect = data[key]["Data"][year]
        if year==target_year:
            total += expect
            count += 1
            if min["Data"] > expect:
                min["Data"] = expect
                min["Entity"] = key
            if max["Data"] < expect:
                max["Data"] = expect
                max["Entity"] = key
        elif (year==(target_year-1)) and (target_year in data[key]["Data"].keys()):
            improve = (data[key]["Data"][target_year] - expect)
            if improve > improved["best"]["fromLast"]["Data"]:
                improved["best"]["fromLast"]["Data"] = improve
                improved["best"]["fromLast"]["Entity"] = key
            if improve < improved["worst"]["fromLast"]["Data"]:
                improved["worst"]["fromLast"]["Data"] = improve
                improved["worst"]["fromLast"]["Entity"] = key
        elif (year==(target_year+1)) and (target_year in data[key]["Data"].keys()):
            improve = (expect - data[key]["Data"][target_year])
            if improve > improved["best"]["toNext"]["Data"]:
                improved["best"]["toNext"]["Data"] = improve
                improved["best"]["toNext"]["Entity"] = key
            if improve < improved["worst"]["toNext"]["Data"]:
                improved["worst"]["toNext"]["Data"] = improve
                improved["worst"]["toNext"]["Entity"] = key
        #print(index, key, code, yr_index, year, expect)

if count==0:  average = 0
else:  average = total / count

print(f"\nFor the year {target_year}: ")
print(f"The average life expectancy across all countries was {average:.2f}")
print(f"The max life expectancy was in {max['Entity']} with {max['Data']}")
print(f"The min life expectancy was in {min['Entity']} with {min['Data']}")
if improved['best']['fromLast']['Entity'] != "": print(f"The greatest improved life expectancy over the previous year was in {improved['best']['fromLast']['Entity']} with {improved['best']['fromLast']['Data']:.2f}")
if improved['best']['toNext']['Entity'] != "": print(f"The greatest improved life expectancy to the next year was in {improved['best']['toNext']['Entity']} with {improved['best']['toNext']['Data']:.2f}")
if improved['worst']['fromLast']['Entity'] != "": print(f"The worst improved life expectancy over the previous year was in {improved['worst']['fromLast']['Entity']} with {improved['worst']['fromLast']['Data']:.2f}")
if improved['worst']['toNext']['Entity'] != "": print(f"The worst improved life expectancy to the next year was in {improved['worst']['toNext']['Entity']} with {improved['worst']['toNext']['Data']:.2f}")