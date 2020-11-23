# Factorial of a number

def factorial(n):
    if n == 0:
        return 1
    else:
        res = 1
        while n > 1:
            res *= n
            n -= 1
        return res


print(factorial(5))


def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_rec(n - 1)


print(factorial_rec(5))
