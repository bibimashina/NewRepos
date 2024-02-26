import view
import model
import text


def find_contacts(message):
    search_word = view.input_data(message)
    result = model.find_contact(search_word)
    view.show_contacts(result, text.find_contact_no_result(search_word))
    return result if result else False


def start_app():
    while True:
        user_choice = view.show_main_menu()
        match user_choice:
            case 1:
                model.open_phone_book()
                view.show_message(text.phone_book_opened_successfully)
            case 2:
                model.save_phone_book()
                view.show_message(text.phone_book_saved_successfully)
            case 3:
                view.show_contacts(model.phone_book, text.empty_phone_book_error)
            case 4:
                new_contact = view.input_data(text.input_new_contact)
                model.add_new_contact(new_contact)
                view.show_message(text.added_new_contact(new_contact[0]))
            case 5:
                find_contacts(text.input_serach_word)
            case 6:
                # добавил проверку индекса для изменения контакта
                check_box = find_contacts(text.input_serach_word_for_edit)
                if check_box:
                    u_id = int(view.input_data(text.input_id_for_edit))
                    if u_id in check_box.keys():
                        edited_contact = view.input_data(text.edit_contact)
                        name = model.edit_contact(u_id, edited_contact)
                        view.show_message(text.edit_contact_successfully(name))
                    else:
                        view.show_message(text.mistake_input)
            case 7:
                # добавил проверку индекса для удаления контакта
                check_box = find_contacts(text.input_serach_word_for_delete)
                if check_box:
                    u_id = int(view.input_data(text.input_id_for_delete))
                    if u_id in check_box.keys():
                        name = model.delete_contact(u_id)
                        view.show_message(text.delete_contact_success(name))
                    else:
                        view.show_message(text.mistake_input)
            case 8:
                # добавил проверку изменения книги
                if not model.phone_book or model.is_book_changed():
                    break
                else:
                    close_book = view.input_data(text.book_has_changed)
                    if close_book == '1':
                        model.save_phone_book()
                        view.show_message(text.phone_book_saved_successfully)
                        break
                    else:
                        break
