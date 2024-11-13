# write a factorial function, given n, you return n!
def factorial(n):
    result = 1
    while n > 0:
        result *=n
        n -=1
    return result
print(factorial(5000))