# C3 = str, C17 = 3132 % 17 = 4
class Laba3:
    def swap_first_last_word(self, sentence):
        words = sentence.split()
        if len(words) >= 2:
            words[0], words[-1] = words[-1], words[0]
            return ' '.join(words)
        else:
            return sentence

    def main(self):
        text = " 3-тя окрема штурмова бригада. З'єднання Сухопутних військ ЗС України чисельністю в бригаду. Окремий полк спеціального призначення «Азов» "
        sentences = text.split('. ')  # Розділяємо текст на речення за крапкою
        for i in range(len(sentences)):
            sentences[i] = self.swap_first_last_word(sentences[i])
        result = '. '.join(sentences)
        print(result)


if __name__ == "__main__":
    lab = Laba3()
    lab.main()
