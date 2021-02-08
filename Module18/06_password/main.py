while True:
    numbers = "1234567890"
    chek = 0
    password = input("Придумайте пароль: ")
    if not password.islower() and len(password) >= 8:
        for symbol in password:
            if symbol in numbers:
                chek += 1
        if chek >= 3:
            print("Пароль надежный")
            break
        else:
            print("Пароль ненадежный, поробуйте еще")
    else:
        print("Пароль ненадежный попробуйте еще")

# зачёт!
