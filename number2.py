try:
    start = int(input("Введіть початкове число: "))
    end = int(input("Введіть кінцеве число: "))
    for i in range(start, end + 1):
        print(i, end=" ")
    print()
except ValueError:
    print("Будь ласка, введіть цілі числа.")