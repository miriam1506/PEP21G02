#classes
class Note:
    text = 'Default text'

    def add_text(self):
        self.text =self.text + 'New text entry'

    def clear_text(self):
            self.text = ''

    note = Note()
    print(type(note))
    print(type(''))
    print('instance value: ', note.text)
    note.text = 'new text'
    print('instance value: ', note.text)
    note.add_text()
    print('instance value: ', note.text)
    note.clear_text()
    print('instance value: ', note.text)
    note.remove_text()
    print('instance value: ', note.text)
