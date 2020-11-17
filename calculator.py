def add(a, b):
    result = a + b
    return 'Sum of ' + str(a) + ' and ' + str(b) + ' is ' + str(result)


res = add(3, 4)
print(res)


def sub(a, b):
    result = a - b
    return 'Difference of ' + str(a) + ' and ' + str(b) + ' is ' + str(result)


res = sub(7, 4)
print(res)


def mul(a, b):
    result = a * b
    return 'Multiplication of ' + str(a) + ' with ' + str(b) + ' is ' + str(result)


res = mul(7, 4)
print(res)


def div(a, b):
    result = a / b
    return 'Division of ' + str(a) + ' by ' + str(b) + ' is ' + str(result)


res = div(7, 4)
print(res)


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


choice = input("Enter choice(1/2/3/4): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
            print(add(num1,num2))
elif choice == '2':
            print(sub(num1,num2))
elif choice == '3':
            print(mul(num1,num2))
elif choice == '4':
            print(div(num1,num2))