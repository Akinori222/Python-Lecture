f = open("pep8")

# try:
#     for line in f:
#         print(line, end="")
#
# finally:
#     f.close()

with open("pep8") as f:
    for line in f:
        print(line, end="")