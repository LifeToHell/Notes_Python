
import json
import os

from Notes import Note
from Controller import Controller
import datetime

def functions():
    notes = []

    c = Controller(Note)
    command = input('1 - создать заметку\n'
                    '2 - прочитать заметку\n'
                    '3 - обновить заметку\n'
                    '4 - удалить заметку\n'
                    '5 - удалить все заметки\n'
                    '6 - прочитать все заметки\n'
                    '7 - выход\n' +
                    'Сделайте Ваш выбор: ')
    if command == '7':
        exit('Всего хорошего')
    if command == '1':
        c.create_note(notes)
    elif command == '2':
        c.read_note()
    elif command == '3':
        c.update_note()
    elif command == '4':
        c.delete_note(Note,note_id)
    elif command == '5':
        c.delete_all_notes()
    elif command == '6':
        c.read_all_notes()
    else:
        print("Команда не найдена")
        return










