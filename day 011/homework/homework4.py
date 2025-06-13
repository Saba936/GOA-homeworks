num1 = int(input())
num2 = int(input())
operation = input()
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/" and num2 != 0:
    print(num1 / num2)
