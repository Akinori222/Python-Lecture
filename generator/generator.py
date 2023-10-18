import csv
import sys

range_nums = range(10)
# for i in range_nums:
#     print(i)

list_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_nums2 = list(range_nums)
# for i in list_nums:
#     print(i)
#
print(sys.getsizeof(range_nums))
print(sys.getsizeof(list_nums))
print(sys.getsizeof(list_nums2))

with open("example.csv") as f:
    reader = csv.DictReader(f)
    print(sys.getsizeof(reader))
    for line in reader:
        print(line)