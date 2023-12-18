import json
import os
from datetime import datetime


class Controller:
    def __init__(self, model):
        self.model = model
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.notes = []

    def create_note(self, Notes):
        notes = []
        title = input('Введите название заметки: ')
        data = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        note_id = len(notes) + 1
        text = input('Введите текст заметки: ')
        note = {"id": note_id, "title": title, "data": data, "text": text}

        notes.append(note)
        save_notes()
        print('Заметка создана')

    def save_notes():
        with open(self.path + '/notes.json', 'w') as f:
            json.dump(notes, f)

    def read_note():
        for note in notes:
            if note.id == int(input('Введите ID заметки: ')):
                print(f'ID : {note.id} Заголовок : {note.title} Дата : {note.data} Текст:  {note.text};n')
            else: print("Заметка не найдена")

    def update_note():
        for note in notes:
            if note.id == int(input('Введите ID заметки: ')):
                title = input('Введите название заметки: ')
                data = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                text = input('Введите текст заметки: ')
                note.title = title
                note.data = data
                note.text = text
                save_notes()
                print('Заметка обновлена')
            else: print("Заметка не найдена")

    def delete_note(self,note_id):
        for note in notes:
            if note.id == int(input('Введите ID заметки: ')):
                notes.remove(note)
                save_notes()
                print('Заметка удалена')
            else: print("Заметка не найдена")


    def load_notes(self):
        with open(self.path + '/notes.json', 'r') as f:
            notes = json.load(f)
        for note_data in notes_data:
            note = Note(
                note_id=note_data['id'],
                title=note_data['title'],
                data=note_data['data'],
                text=note_data['text']
            )
            self.notes.append(note)

    def delete_all_notes():
        notes.clear()
        save_notes()
        print('Все заметки удалены')

    def read_all_notes():
        for note in notes:
            print(f'ID : {note.id} Заголовок : {note.title} Дата : {note.data} Текст:  {note.text};n')