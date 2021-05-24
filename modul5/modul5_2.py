#classes
class Note:
    text = 'Default text'

    def add_text(self , text_to_add):
        self.text =self.text + text_to_add
    def clear_text(self):
        self.text = ''
    def remove_text(self, text_to_remove):
        self.text = self.text.replace('text_to_remove','')
    def count_line(self):
        count = len(self.text.splitlines())
        return count
note = Note()
print(type(note))
print(type(''))
print('instance value: ', note.text)
note.text = 'new text'
print('instance value: ', note.text)
note.add_text('new random text')
print('instance value: ', note.text)
note.remove_text('New')
print('instance value: ', note.text)
note.clear_text()
print('instance value: ', note.text)
note.add_text("First line    \n     second line    ")
print(note.count_line())
