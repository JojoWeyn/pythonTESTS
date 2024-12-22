import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуйте угадать его.")

    while True:
        guess = int(input("Введите ваше предположение: "))
        attempts += 1

        if guess < number_to_guess:
            print("Слишком мало! Попробуйте еще раз.")
        elif guess > number_to_guess:
            print("Слишком много! Попробуйте еще раз.")
        else:
            print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempts} попыток.")
            print("Вы настоящий мастер угадывания чисел! 🎉")
            break

if __name__ == "__main__":
    guess_the_number()
