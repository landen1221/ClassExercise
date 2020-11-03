"""Word Finder: finds random words from a dictionary."""
from random import randrange

class WordFinder:
    """
    Identifies number of words in a given document

    """

    def __init__(self, doc):
        self.doc = doc
        self.words = 0
        self.word_count()


    # def __repr__(self):
    #     return f'{self.word_count()} words read'

    def word_count(self):
        """
        counts all of the words in the document provided
        """
        with open(self.doc, 'r') as file:
            for line in file:
                self.words += 1
            file.close()
            return self.words

    def word_of_the_day(self):
        """
        Selects a random word to become the word of the day
        """
        x = randrange(self.words)

        with open(self.doc, 'r') as file:
            for i, line in enumerate(file):
                if i == x:
                    file.close()
                    return line


class SpecialWordFinder(WordFinder):
    def word_count(self):
        """
        Counts words, and avoids counting lines that are blank
        """
        with open(self.doc, 'r') as file:
            for line in file:
                if len(line) > 1:
                    self.words += 1




wf = SpecialWordFinder('words.txt')
print(wf.word_of_the_day())
