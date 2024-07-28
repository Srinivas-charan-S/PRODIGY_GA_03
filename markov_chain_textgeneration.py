import random
import string
from collections import defaultdict, Counter

class MarkovChain:
    def __init__(self, order=1):
        self.order = order
        self.word_model = defaultdict(Counter)

    def clean_text(self, text):
        """
        Clean the text by removing punctuation and extra spaces.
        """
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = ' '.join(text.split())  # Remove extra spaces
        return text

    def build_word_chain(self, text):
        """
        Build the Markov chain model at the word level from the given text.
        """
        words = text.split()
        for i in range(len(words) - self.order):
            current_state = tuple(words[i:i + self.order])
            next_state = words[i + self.order]
            self.word_model[current_state][next_state] += 1

    def generate_word_text(self, length=100):
        """
        Generate text at the word level using the Markov chain model.
        Start with a random state and generate text of the given length.
        """
        current_state = random.choice(list(self.word_model.keys()))
        generated_text = ' '.join(current_state)

        while len(generated_text.split()) < length:
            if current_state in self.word_model:
                next_word = self._get_next_word(current_state)
                generated_text += ' ' + next_word
                current_state = tuple(generated_text.split()[-self.order:])
            else:
                break

        return generated_text

    def _get_next_word(self, current_state):
        """
        Helper function to get the next word based on probabilities.
        """
        transitions = self.word_model[current_state]
        total = sum(transitions.values())
        rand_num = random.randint(1, total)
        cumulative_prob = 0

        for word, count in transitions.items():
            cumulative_prob += count
            if rand_num <= cumulative_prob:
                return word


def main():
    # Read text from input file
    input_file = r"C:\Users\ssrin\input.txt"
    with open(input_file, 'r') as file:
        input_text = file.read()

    # Create Markov chain model
    markov_model = MarkovChain(order=2)  # Adjust the order for different levels of context
    cleaned_text = markov_model.clean_text(input_text)
    markov_model.build_word_chain(cleaned_text)

    # Generate text at word level
    generated_word_text = markov_model.generate_word_text(length=50)
    print("\nGenerated Word Level Text:")
    print(generated_word_text)
    # Wait for user input before closing
    input("\n")

if __name__ == "__main__":
    main()










