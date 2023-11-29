#!/usr/bin/env python3

class MyString:
    def __init__(self, value=None):
        self._value = None
        if value is not None:
            self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        sentences = self._value.replace(',', '.').split('.')
        return len([sentence for sentence in sentences if sentence.strip()])

pass
