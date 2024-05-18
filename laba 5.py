class Letter:
    def __init__(self, char):
        self.char = char

class Word:
    def __init__(self, word):
        self.letters = [Letter(char) for char in word]

class Sentence:
    def __init__(self, sentence):
        self.words = [Word(word) for word in sentence.split()]

    def swap_first_last_word(self):
        if len(self.words) >= 2:
            self.words[0], self.words[-1] = self.words[-1], self.words[0]

class Punctuation:
    def __init__(self, mark):
        self.mark = mark

class Text:
    def __init__(self, text):
        self.sentences = [Sentence(sentence) for sentence in text.split('. ')]

class Laba3:
    def __init__(self, text):
        self.text = text

    def process_text(self):
        processed_text = Text(self.text.replace('\t', ' ').replace('  ', ' '))
        for sentence in processed_text.sentences:
            sentence.swap_first_last_word()
        result = '. '.join([' '.join([''.join([letter.char for letter in word.letters]) for word in sentence.words]) for sentence in processed_text.sentences])
        return result

if __name__ == "__main__":
    text = " 3-тя окрема штурмова бригада. З'єднання Сухопутних військ ЗС України чисельністю в бригаду. Окремий полк спеціального призначення «Азов» "
    lab = Laba3(text)
    result = lab.process_text()
    print(result)
