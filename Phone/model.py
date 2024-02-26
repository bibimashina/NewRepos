phone_book = {}
first_book = {}
path = "Phone book/ver.2/phone_book.txt"  # Relative path!!!
SEPARATOR = ";"



def open_phone_book():
    global phone_book
    with open(path, "r", encoding="UTF-8") as book:
        data = book.readlines()
        data.sort()  # сортируем книгу по алфавиту при первом окрытии

    for u_id, contact in enumerate(data, 1):
        phone_book[u_id] = contact.strip().split(SEPARATOR)


def save_phone_book():
    global phone_book
    data = [SEPARATOR.join(contact) for contact in phone_book.values()]
    data = "\n".join(data)
    with open(path, "w", encoding="utf-8") as book:
        book.write(data)


def _next_id():
    global phone_book
    return max(phone_book) + 1 if phone_book else 1


def add_new_contact(new_contact: list[str]):
    global phone_book
    phone_book[_next_id()] = new_contact


def find_contact(search_word: str) -> dict[int, list[str]]:
    global phone_book
    result = {}
    for u_id, contact in phone_book.items():
        if search_word.lower() in " ".join(contact).lower():
            result[u_id] = contact
    return result


def edit_contact(u_id: int, contact_to_edit: list[str]):
    global phone_book
    curent_contact = phone_book[u_id]
    for i in range(len(curent_contact)):
        curent_contact[i] = (
            contact_to_edit[i] if contact_to_edit[i] else curent_contact[i]
        )
    phone_book[u_id] = curent_contact
    return curent_contact[0]


def delete_contact(u_id: int):
    global phone_book
    return phone_book.pop(u_id)[0]


def is_book_changed():
    global phone_book
    
    with open(path, "r", encoding="UTF-8") as book:
        first_data = book.readlines()
    for u_id, contact in enumerate(first_data, 1):
        first_book[u_id] = contact.strip().split(SEPARATOR)
    if first_book == phone_book:
        return True
    return False