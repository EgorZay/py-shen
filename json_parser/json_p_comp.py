import json
import csv

# parse .json to .csv

with open('filename.json', encoding="UTF-8") as json_p:
    x = json.load(json_p)

f = csv.writer(open("filename.csv", "w"))
f.writerow(['...'])  # type a list of rownames

for x in x:
    f.writerow([x[...]]) # type the same list of rownames

# erase redundant rows from any .csv

with open('filename_with_redundant_rows.csv') as input, open('new_csv_without_excess_rows.csv', 'w', newline='') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)
