with open("writing file.text", mode="w+") as f:
    f.write("This is file\n")
    f.seek(0)
    print(f.read())