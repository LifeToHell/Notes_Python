
class Note(object):
    def __init__(self, note_id, title, data, text):
        self.id = note_id
        self.title = title
        self.data = data
        self.text = text

@property
def note_id(self):
    return self._note_id

@note_id.setter
def note_id(self, note_id):
    self._note_id = note_id


@property
def title(self):
    return self._title

@title.setter
def title(self, title):
    self._title = title


@property
def data(self):
    return self._data

@data.setter
def data(self, data):
    self._data = data


@property
def text(self):
    return self._text


@text.setter
def text(self, text):
    self._text = text

def __str__(self):
    return f"{self.note_id} {self.title} {self.data} {self.text}"





