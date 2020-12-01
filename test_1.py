# -*- coding: utf-8 -*-
"""Morse Code Translator"""
import doctest


LETTER_TO_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": " ",
}

MORSE_TO_LETTER = {morse: letter for letter, morse in LETTER_TO_MORSE.items()}


def encode(message: str) -> str:
    """
    Кодирует строку в соответствие с таблицей азбуки Морзе
    >>> encode('SOS')
    '... --- ...'
    >>> encode('CHECK') # doctest: +ELLIPSIS
    '-.-...-.-'
    >>> encode('.-.') # doctest: +NORMALIZE_WHITESPACE
    '.-.-.-  -....-      .-.-.-'
    >>> encode('help')
    Traceback (most recent call last):
      File "...doctest.py", line 1329, in __run
        compileflags, 1), test.globs)
      File "<doctest test_1.encode[3]>", line 1, in <module>
        encode('help')
      File "...test_1.py", line 43, in encode
        LETTER_TO_MORSE[letter] for letter in message
      File "...test_1.py", line 43, in <listcomp>
        LETTER_TO_MORSE[letter] for letter in message
    KeyError: 'h'
    """
    encoded_signs = [LETTER_TO_MORSE[letter] for letter in message]

    return " ".join(encoded_signs)


def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """
    decoded_letters = [MORSE_TO_LETTER[letter] for letter in morse_message.split()]

    return "".join(decoded_letters)


if __name__ == "__main__":
    doctest.testmod()
