import datetime

last_id = 0

class Note:
    '''Represent a note in the notebook. Match against a
    string in searches and store tags for each note.'''
    def __init__(self, memo: str, tags: list=''):
        '''Initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.

        >>> note1 = Note("hello first")
        >>> note2 = Note("hello again")
        >>> note1.id
        1
        >>> note2.id
        2
        >>> note1.memo
        'hello first'
        >>> note2.memo
        'hello again'
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter: str) -> bool:
        '''Determine if this note matches the filter
        text. Return True if it matches, False otherwise.

        Search is case sensitive and matches both text and
        tags.

        >>> note1 = Note("hello first")
        >>> note2 = Note("hello again")
        >>> note1.match('hello')
        True
        >>> note2.match('second')
        False
        '''
        return filter in self.memo or filter in self.tags


class Notebook:
    '''Represent a collection of notes that can be tagged,
    modified, and searched.'''
    def __init__(self):
        '''Initialize a notebook with an empty list.
        
        >>> notebook = Notebook()
        >>> notebook.notes
        []
        '''
        self.notes = []

    def new_note(self, memo: str, tags: list=''):
        '''Create a new note and add it to the list.

        >>> notebook = Notebook()
        >>> notebook.new_note("hello world")
        >>> notebook.new_note("hello again")
        >>> list(map(lambda x: x.memo,notebook.notes))
        ['hello world', 'hello again']
        >>> notebook.notes[0].memo
        'hello world'
        '''
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        '''Locate the note with the given id.'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id: int, memo: str) -> bool:
        '''Find the note with the given id and change its
        memo to the given value.

        >>> notebook = Notebook()
        >>> notebook.new_note("hello world")
        >>> n_id = notebook.notes[0].id
        >>> notebook.modify_memo(n_id, "hi world")
        True
        >>> notebook.notes[0].memo
        'hi world'
        '''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id: int, tags: str) -> bool:
        '''Find the note with the given id and change its
        tags to the given value.

        >>> notebook = Notebook()
        >>> notebook.new_note("hello world", "tag")
        >>> n_id = notebook.notes[0].id
        >>> notebook.modify_tags(n_id, "new tags")
        True
        >>> notebook.notes[0].tags
        'new tags'
        '''
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def search(self, filter: str) -> list:
        '''Find all notes that match the given filter
        string.
        
        >>> notebook = Notebook()
        >>> notebook.new_note("hello world")
        >>> notebook.new_note("hello again")
        >>> list(map(lambda x: x.memo, notebook.search("hello")))
        ['hello world', 'hello again']
        >>> list(map(lambda x: x.memo, notebook.search("world")))
        ['hello world']
        '''
        return [note for note in self.notes if
                note.match(filter)]


import doctest
doctest.testmod()