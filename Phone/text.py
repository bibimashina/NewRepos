main_menu = {  ## заменил на словарь
    0: "Главное меню",
    1: "Открыть книгу",
    2: "Сохранить книгу",
    3: "Показать все контакты",
    4: "Создать новый контакт",
    5: "Найти контакт",
    6: "Изменить контакт",
    7: "Удалить контакт",
    8: "Выйти из программы",
}
# переменная для вывода в таблице
contact_discription = ["id", "ФИО", "Номер телефона", "Комментарий", "Город"]

choice_main_menu = f"Выберите пункт меню (от 1 до {len(main_menu)-1}): "
mistake_input = "Неверный ввод, попробуйте снова!"


phone_book_opened_successfully = "Телефонная книга отркыта успешно!"
phone_book_saved_successfully = "Телефонная книга сохранена успешно!"


empty_phone_book_error = "Телефонная книга пуста или не открыта!"


input_new_contact = [
    "Введите имя контакта: ",
    "Введите номер контакта: ",
    "Введите комментарий для контакта: ",
    "Введите город контакта: ",
]

input_serach_word = "Введите то, что будем искать: "
input_serach_word_for_edit = "Введите слово для контакта, который хотите изменить: "
input_serach_word_for_delete = "Введите слово для контакта, который хотите удалить: "
input_id_for_edit = "Введите ID контакта, который хотите изменить: "
input_id_for_delete = "Введите ID контакта, который хотите удалить: "

no_changes = "Или нажмите ENTER, чтобы оставить без изменений"

edit_contact = [
    f"Введите новое имя ({no_changes}): ",
    f"Введите новый номер ({no_changes}): ",
    f"Введите новый комментарий ({no_changes}): ",
    f"Введите новый город ({no_changes}): ",
]

book_has_changed = "Телефонная книга была изменена, сохранить изменения? (1 - да, 2 - нет): "


def edit_contact_successfully(name: str) -> str:
    return f'Контакт "{name}" изменён!'


def added_new_contact(contact: str) -> str:
    return f"Новый контакт '{contact}' добавлен успешно!"


def find_contact_no_result(word: str) -> str:
    return f'Контакты содеражащие "{word}" не найдены!'


def delete_contact_success(name: str) -> str:
    return f'Контакт "{name}" удалён!'
