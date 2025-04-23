try:
    n = int(input("Введіть число n: "))
    for i in range(n - (n % 2), 0, -2):
        print(i, end=" ")
    print()
except ValueError:
    print("Будь ласка, введіть ціле число.")