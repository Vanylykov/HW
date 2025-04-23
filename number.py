import random

secret_number = random.randint(1, 10)
attempts = 3

print("Вітаю у грі 'Вгадай число'!")
print("Я загадав число від 1 до 10. У вас є 3 спроби.")

for i in range(attempts):
    try:
        guess = int(input(f"Спроба {i + 1}: Введіть ваше число: "))
        if guess == secret_number:
            print("Вітаємо! Ви вгадали число!")
            break
        elif guess > secret_number:
            print("Менше")
        else:
            print("Більше")
    except ValueError:
        print("Будь ласка, введіть ціле число.")

else:
    print(f"На жаль, ви не вгадали. Загадане число було: {secret_number}")