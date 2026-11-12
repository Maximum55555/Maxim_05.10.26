password = input("Введите пароль: ")

while len(password) < 8:
    print("Минимум 8 символов.")
    password = input("Введите пароль еще раз: ")

print("Пароль принят.")
