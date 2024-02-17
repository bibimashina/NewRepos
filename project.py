# phone_book = {}


# Добавление контакта
def add_contact():
    book = open("book.txt", "a+", encoding="utf-8")
    name_family = input("введите имя и фамилию: ")
    phone_number = input("введите номер телефона: ")
    comment = input("введите комментарий: ")
    book.write(phone_number + " " + name_family + " | " + comment + "\n")
    book.close()
    print("контакт добавлен")


# Просмотр всех контактов
def view_all_contact():
    with open("book.txt", "r", encoding="utf-8") as book:
        contacts = [line.strip() for line in book]
    return contacts


# Поиск контакта
def find_contact():
    all_contacts = view_all_contact()
    search = input("введите имя и фамилию или номер телефона: ")
    if search:
        found = False
        for contact in all_contacts:
            if search in contact:
                print("контакт найден")
                found = True
                break
        if not found:
            print("контакт не найден")
    else:
        print("Пожалуйста, введите имя и фамилию или номер телефона для поиска.")
        return find_contact()


#Перенос контакта
def copy_contact(source_file, destination_file):
    with open(source_file, "r", encoding="utf-8") as source:
        contacts = source.readlines()

    line_number = int(input("Введите номер строки для копирования: ")) - 1
    if 0 <= line_number < len(contacts):
        with open(destination_file, "a", encoding="utf-8") as destination:
            destination.write(contacts[line_number])
        print("Контакт скопирован успешно")
    else:
        print("Недопустимый номер строки")


def menu():
    while True:
        print("Меню:")
        print("1. Добавить контакт")
        print("2. Просмотреть все контакты")
        print("3. Найти контакт")
        print("4. Скопировать контакт в другой файл")
        print("5. Выход")

        choice = input("Выберите опцию: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            contacts = view_all_contact()
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. {contact}")
        elif choice == "3":
            find_contact()
        elif choice == "4":
            source_file = input("Введите имя файла из которого копировать: ")
            destination_file = input("Введите имя файла куда копировать : ")
            copy_contact(source_file, destination_file)
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверная опция. Пожалуйста, выберите снова.")


menu()
