# 再帰関数：関数内で自身の関数をcallする

# 階乗(factorial)
# n! = n * (n-1)!

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(9))

# challenge1
def fibonacci_recursive(n):
    if n < 2:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(fibonacci_recursive(8))


# challenge2
def fibonacci(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(n-1):
            result = n_1 + n_2
            n_2 = n_1
            n_1 = result
        return result

print(fibonacci(8))


for i in range(50):
    # print(i, fibonacci_recursive(i))
    print(i, fibonacci(i))