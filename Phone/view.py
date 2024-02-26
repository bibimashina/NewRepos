import text

BORDER = "="


def show_main_menu() -> int:
    print("\t" + text.main_menu[0])
    for k, v in text.main_menu.items():
        if k:
            print(f"{k:>3} → {v}")
    print(BORDER * (len(text.choice_main_menu) + 1))  # под меню выводим границу
    while True:
        choice = input(text.choice_main_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return int(choice)
        print(text.mistake_input)


def show_contacts(phone_book: dict, error_message: str):
    if phone_book:
        headers = text.contact_discription
        print("\n" + BORDER * 65)
        print(
            f"{headers[0]:>3} {headers[1]:<12} {headers[2]:<17} {headers[3]:<12} {headers[4]:<12}"
        )
        print("-" * 65)
        for u_id, contact in phone_book.items():
            print(
                f"{u_id:>3}. {contact[0]:<10} | {contact[1]:<15} | {contact[2]:<10} | {contact[3]:<10}"
            )
        print(BORDER * 65 + "\n")
    else:
        show_message(error_message)


def show_message(message: str):
    print("\n" + BORDER * len(message))
    print(message)
    print(BORDER * len(message) + "\n")


def input_data(message) -> list[str] | str:
    if isinstance(message, str):
        return input("\n" + message)
    return [input(mess) for mess in message]
