#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
            return
        self._value = value
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        # Replace all sentence-ending punctuation with periods
        # to normalize the string
        text = self.value
        text = text.replace('!', '.')
        text = text.replace('?', '.')
        
        # Split on periods and filter out empty strings
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        
        return len(sentences)
