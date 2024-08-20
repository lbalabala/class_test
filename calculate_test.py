# 定义一个函数来执行基本的算术运算
def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2
    else:
        return "Invalid operation"

# 获取用户输入
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# 确保用户输入的是有效的操作
while True:
    operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()
    if operation in ['add', 'subtract', 'multiply', 'divide']:
        break
    else:
        print("Invalid operation. Please try again.")

# 执行运算并打印结果
result = calculate(num1, num2, operation)
print(f"The result is: {result}")
