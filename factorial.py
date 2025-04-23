try:
    n = int(input("Введіть число для знаходження факторіалу: "))
    if n < 0:
        print("Факторіал не визначено для від'ємних чисел.")
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        print(f"Факторіал числа {n} дорівнює {factorial}")
except ValueError:
    print("Будь ласка, введіть ціле число.")