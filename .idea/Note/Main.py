import os
import json
import uuid
from datetime import datetime
from typing import List

class Note:
    def __init__(self, id: str, title: str, text: str, timestamp: str):
        self.id = id
        self.title = title
        self.text = text
        self.timestamp = timestamp

class Model:
    def add_note(self, note: Note):
        notes = self.get_notes()
        notes.append(note)
        self.write_notes_to_file(notes)

    def remove_note_at(self, index: int):
        notes = self.get_notes()
        if 0 <= index < len(notes):
            del notes[index]
            self.write_notes_to_file(notes)

    def get_notes(self) -> List[Note]:
        if not os.path.exists("notes.json"):
            return []
        with open("notes.json", "r") as file:
            data = json.load(file)
            return [Note(note['id'], note['title'], note['text'], note['timestamp']) for note in data]

    def write_notes_to_file(self, notes: List[Note]):
        data = [{'id': note.id, 'title': note.title, 'text': note.text, 'timestamp': note.timestamp} for note in notes]
        with open("notes.json", "w") as file:
            json.dump(data, file, indent=4)

class Controller:
    def __init__(self, model: Model):
        self.model = model

    def create_note(self):
        title = input("Введите заголовок заметки: ")
        text = input("Введите текст заметки: ")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = Note(str(uuid.uuid4()), title, text, timestamp)
        self.model.add_note(note)


    def read_note(self):
        index = int(input("Введите индекс заметки для прочтения: "))
        notes = self.model.get_notes()
        if 0 <= index < len(notes):
            print(f"Заголовок: {notes[index].title}")
            print(f"Текст: {notes[index].text}")
            print(f"Дата/время создания: {notes[index].timestamp}")
        else:
            print("Недопустимый индекс")

    def update_note(self):
        index = int(input("Введите индекс заметки для обновления: "))
        notes = self.model.get_notes()
        if 0 <= index < len(notes):
            new_text = input("Введите новый текст заметки: ")
            notes[index].text = new_text
            notes[index].timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.model.write_notes_to_file(notes)
        else:
            print("Недопустимый индекс")

    def delete_note(self, index: int):
        self.model.remove_note_at(index)

    def delete_all_notes(self):
        if input("Вы уверены, что хотите удалить все заметки? (да/нет): ").lower() == "да":
            with open("notes.json", "w") as file:
                file.write("[]")
            print("Все заметки удалены")
        else:
            print("Удаление отменено")

    def read_all_notes(self):
        notes = self.model.get_notes()
        for i, note in enumerate(notes):
            print(f"Заметка {i} - {note.title} ({note.timestamp})")


class View:
    def __init__(self, controller: Controller):
        self.controller = controller

    def menu(self):
        while True:
            print('1 - создать заметку\n'
                  '2 - прочитать заметку\n'
                  '3 - обновить заметку\n'
                  '4 - удалить заметку\n'
                  '5 - удалить все заметки\n'
                  '6 - прочитать все заметки\n'
                  '7 - выход\n')
            choice = input("Выберите опцию: ")
            if choice == "1":
                self.controller.create_note()
            elif choice == "2":
                self.controller.read_note()
            elif choice == "3":
                self.controller.update_note()
            elif choice == "4":
                if choice == "4":
                    while True:
                        try:
                            index = int(input("Введите индекс заметки для удаления: "))
                        except ValueError:
                            print("Ошибка: Введите корректный индекс (целое число).")
                        else:
                            self.controller.delete_note(index)
                            break
            elif choice == "5":
                self.controller.delete_all_notes()
            elif choice == "6":
                self.controller.read_all_notes()
            elif choice == "7":
                exit('Всего доброго')
            else:
                print("Некорректный ввод. Пожалуйста, выберите опцию от 1 до 7.")


def main():
    model = Model()
    controller = Controller(model)
    view = View(controller)
    view.menu()
    controller.create_note()
    controller.delete_note(0)

if __name__ == "__main__":
    main()