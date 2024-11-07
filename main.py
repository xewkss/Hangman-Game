import os
import random

print("Привет, я загадал слово, твоя задача угадать его по буквам")
input("*Нажмите enter чтобы продолжить")
os.system('cls')
print("Поехали")
words = ["программист", "игра", "коммит", "итерация"]
word = random.choice(words)

letters = []

IsWin = True
hp = 10
while hp > 0:
    IsWin = True
    for symb in word:
        if symb in letters:
            print(symb, end=" ")
        else:
            print("*", end=" ")
            IsWin = False
    print()
    if IsWin:
        print("Ты угадал молодец!")
        break

    letter = input("Введите букву: ")
    letters.append(letter)
    os.system("cls")
    if letter not in word:
        hp -= 1
    print(f"Попыток осталось {hp}")
if hp <= 0:
    print(f"Ты проиграл, попытки закончились, этим словом было \"{word}\"")
