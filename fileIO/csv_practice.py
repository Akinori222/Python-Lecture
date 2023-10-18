import csv

# csv.reader
# with open("example.csv") as f:
#     reader = csv.reader(f)
#     for line in reader:
#         print(line{1})

# csv.Dictreader
with open("example.csv") as f:
    reader = csv.DictReader(f)
    for line in reader:
        print(line["First Name"])

