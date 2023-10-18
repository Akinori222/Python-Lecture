from functools import lru_cache
import time


# .time() 1970/1/1~ 秒数が表示
@lru_cache()
def fibonacci_recursive(n):
    print(f"fibonacci with {n} is running...")
    if n < 2:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

before = time.time()
print(fibonacci_recursive(20))
after = time.time()
print(f"{after - before:.2f}sec")


# .ctime() 今のローカル時間を文字列で返す
print(time.ctime())

# .localtime() 構造化データで返す
localtime = time.localtime()
print(localtime.tm_year)
print(f"今の時刻は{localtime.tm_year}年{localtime.tm_mon}月{localtime.tm_mday}日{localtime.tm_hour}時{localtime.tm_min}分です。")
print("今の時刻は{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分です。".format(localtime))