# writing a program to count letters in a sentence
sentence = "This is a common interview question"


class FreqNum:
    def __init__(self):
        self.letter_frequency = {}

    def freq(self, sent):
        strip_sent = sent.replace(" ", "")
        print(strip_sent)
        for letter in strip_sent:
            if letter in self.letter_frequency:
                self.letter_frequency[letter] += 1
            else:
                self.letter_frequency[letter] = 1
        print(self.letter_frequency)
        for items in self.letter_frequency.items():
            print(f"This item: {items[0]} appears {items[1]} times")


point = FreqNum()
point.freq("This is a common interview question")



