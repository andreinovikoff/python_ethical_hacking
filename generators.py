import random


class ListGenerator:
    def __init__(self, lines):
        """Generator initialization"""
        self.i = 0
        self.lines = lines

    def reset(self):
        self.i = 0

    def next(self):
        """Get next line"""
        if self.i >= len(self.lines):
            return None

        line = self.lines[self.i]
        self.i += 1
        return line


class FileLinesGenerator(ListGenerator):
    def __init__(self, filepath):
        self.i = 0
        with open(filepath) as f:
            file_data = f.read()
        lines = file_data.split('\n')
        super().__init__(lines)


class BadPasswordGenerator(FileLinesGenerator):
    def __init__(self, filepath='bad_passwords.txt'):
        super().__init__(filepath)


class GoodPasswordGenerator:
    def __init__(self, alphabet='1234567890qwertyuiopasdfghjklzxcvbnm'
                                'QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+'):
        """Generator initialization"""
        self.alphabet = alphabet

    def reset(self):
        pass

    def next(self, length=10):
        """Get next password"""
        password = ''
        for i in range(length):
            c = random.choice(self.alphabet)
            password += c
        return password


class BruteForceGenerator:
    def __init__(self, alphabet='1234567890qwertyuiopasdfghjklzxcvbnm', min_length=0):
        """Generator initialization"""
        self.alphabet = alphabet
        self.base = len(alphabet)
        self.min_length = min_length
        self.length = min_length
        self.counter = 0

    def reset(self):
        self.length = self.min_length
        self.counter = 0

    def next(self):
        result = ''
        number = self.counter
        while number > 0:
            rest = number % self.base
            result = self.alphabet[rest] + result
            number = number // self.base

        while len(result) < self.length:
            result = self.alphabet[0] + result

        if self.alphabet[-1] * self.length == result:
            # met the last password for the current length
            self.length += 1
            self.counter = 0
        else:
            self.counter += 1

        return result
