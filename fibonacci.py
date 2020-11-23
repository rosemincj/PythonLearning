# Fibonacci series
def fibonacci_rec(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


n = int(input("Fibonacci series upto "))
print(fibonacci_rec(n))

num = int(input("Fibonacci series upto "))

n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if num == 1:
    print(n1)
else:
    while count < num:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
