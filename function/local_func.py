# local variable, global variable

call_count = 0

def count_num():
    global call_count
    call_count += 1
    print(call_count)
    return

count_num()

count_num()
