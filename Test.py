def add_contact():
    name_family = input("введите имя и фамилию: ")
    phone_number = input("введите номер телефона: ")
    comment = input("введите комментарий: ")

    with open("book.txt", "r", encoding="utf-8") as book:
        for line in book:
            existing_phone_number = line.split(" ")[0]
            if phone_number == existing_phone_number:
                print("Такой номер уже существует в книге контактов")
                return
    book.close()

    with open("book.txt", "a", encoding="utf-8") as book:
        book.write(phone_number + " " + name_family + " | " + comment + "\n")
    print("контакт добавлен")