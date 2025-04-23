try:
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    operation = input("Введіть математичну операцію (+, -, *, /): ")

    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        if b == 0:
            print("Ділення на нуль!")
        else:
            result = a / b
            print(f"Результат: {result}")
    else:
        print("Невірна операція.")
    if 'result' in locals():
        print(f"Результат: {result}")

except ValueError:
    print("Будь ласка, введіть числа.")