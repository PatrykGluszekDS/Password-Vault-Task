import random
import string

class PasswordGenerator:
    def __init__(self, length=12, use_digits=True, use_symbols=True):
        self.length = length
        self.use_digits = use_digits
        self.use_symbols = use_symbols

    def generate(self):
        characters = string.ascii_letters
        if self.use_digits:
            characters += string.digits
        if self.use_symbols:
            characters += string.punctuation

        return ''.join(random.choice(characters) for _ in range(self.length))
