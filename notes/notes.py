import json
import os
from datetime import datetime


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_notes(filename):
    notes = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            notes = json.load(file)
    return notes


def save_notes(notes, filename):
    with open(filename, 'w') as file:
        json.dump(notes, file, indent=4)


def add_note(notes, title, body):
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }
    notes.append(note)
    return notes


def edit_note(notes, note_id, new_title, new_body):
    for note in notes:
        if note["id"] == note_id:
            note["title"] = new_title
            note["body"] = new_body
            note["timestamp"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            return True
    return False


def delete_note(notes, note_id):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return True
    return False


def filter_notes_by_date(notes, date):
    filtered_notes = [
        note for note in notes if note["timestamp"].startswith(date)]
    return filtered_notes


def print_notes(notes):
    print("Все заметки:\n")
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['body']}")
        print(f"Дата и время: {note['timestamp']}")
        print("--------------------")


def start():
    filename = "notes.json"
    notes = load_notes(filename)

    while True:
        clear_console()
        print_notes(notes)
        print("1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Фильтровать заметки по дате")
        print("5. Показать все заметки")
        print("6. Выход")

        choice = input("\nВыберите пункт меню: ")

        if choice == "1":
            clear_console()
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            notes = add_note(notes, title, body)
            save_notes(notes, filename)
            print("\nЗаметка успешно добавлена!")
            input("\nНажмите Enter, чтобы продолжить...")
            clear_console()
            print_notes(notes)
            input("\nНажмите Enter, чтобы продолжить...")

        elif choice == "2":
            clear_console()
            print_notes(notes)
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок: ")
            new_body = input("Введите новый текст: ")
            if edit_note(notes, note_id, new_title, new_body):
                save_notes(notes, filename)
                print("Заметка успешно отредактирована!")
            else:
                print("Заметка не найдена!")
            input("\nНажмите Enter, чтобы продолжить...")

        elif choice == "3":
            clear_console()
            note_id = int(input("Введите ID заметки для удаления: "))
            if delete_note(notes, note_id):
                save_notes(notes, filename)
                print("Заметка успешно удалена!")
            else:
                print("Заметка не найдена!")
            input("\nНажмите Enter, чтобы продолжить...")

        elif choice == "4":
            clear_console()
            date = input("Введите дату (ДД-ММ-ГГГГ): ")
            filtered_notes = filter_notes_by_date(notes, date)
            if filtered_notes:
                print("Отфильтрованные заметки:")
                print_notes(filtered_notes)
            else:
                print("Заметки не найдены для указанной даты!")
            input("\nНажмите Enter, чтобы продолжить...")

        elif choice == "5":
            clear_console()
            print("Все заметки:")
            print_notes(notes)
            input("\nНажмите Enter, чтобы продолжить...")

        elif choice == "6":
            break

        else:
            clear_console()
            print("Неверный выбор! Пожалуйста, выберите правильную опцию.")
            input("\nНажмите Enter, чтобы продолжить...")


start()
