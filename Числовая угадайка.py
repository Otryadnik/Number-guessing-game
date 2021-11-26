from random import randint

print('Добро пожаловать в числовую угадайку')
print('Угадай число от 1 до 100')
# ввод и провека в заданном диапозоне, введеного числа
def is_valid(num):
    return 1 <= num <= 100

restart = 'да'
while restart.lower() == 'да':
    numbers = randint(1, 100)
    number_of_attempts = 1
    while True:
        number = int(input())
        if is_valid(number) == True:
            number = int(number)
            if numbers > number:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                number_of_attempts += 1
            elif numbers < number:
                print('Ваше число больше загаданного, попробуйте еще разок')
                number_of_attempts += 1
            else:
                if number_of_attempts == 1 or number_of_attempts > 2:
                    print('Вы угадали c', number_of_attempts, 'попытки, поздравляем!')
                else:
                    print('Вы угадали cо второй попытки, поздравляем!')

                restart = input('Спасибо, что играли в числовую угадайку. Хотите сыграть ещё раз (введите да или нет):')
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

