"""Module for a simple bar graph frequency analysis"""
from collections import defaultdict


class SimpleBar:
    """Class that can analyise sentences and print out a basic 'bar graph' of the letters used
    in the sentence and their frequency"""

    _ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self):
        self._data = defaultdict(list)

    def analyise(self, user_input):
        """
        Take the user input and parse it into the frequency graph.

        :param user_input: The string to analise.
        """
        if user_input == "":
            return
        for letter in user_input:
            letter = letter.lower()
            if letter in self._ALPHABET:
                self._data[letter].append(letter)

    def format_output(self):
        """
        Format the output into a frequency graph.

        :return: The formatted information as a string.
        """
        output = ""
        for key in self._data.keys():
            values = self._data.get(key)
            formatted_values = ', '.join(values)
            output += key + ": " + formatted_values + "\n"

        return output
