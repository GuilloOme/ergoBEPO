#!/usr/bin/python3
import argparse
from random import randrange

# set of valid key usable for password generation
KEY_SET = [
    "1", "4", "5", "Equals", "Minus", "6", "7", "8", "9", "0",
    "BackTick", "Q", "E", "R", "RBrace", "U", "I", "O", "P", "LBrace",
    "A", "S", "D", "F", "G", "H", "J", "K", "L", "SEMICOLON", "QUOTE",
    "X", "C", "V", "B", "N", "M", "COMMA", "PERIOD", "SLASH",
]

STROKE_FORMAT = 'U"{}"'


def generate_key_stroke(length):
    seed = [randrange(len(KEY_SET)) for _ in range(length)]
    return " + ".join([STROKE_FORMAT.format(KEY_SET[i]) for i in seed])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length",
                        type=int,
                        required=False,
                        default=8,
                        help="length of the keystrokes")
    parser.add_argument("-n", "--number",
                        type=int,
                        required=False,
                        default=1,
                        help="number of keystrokes")
    args = parser.parse_args()
    password_length = args.length
    number = args.number

    for _ in range(number):
        print(": "+generate_key_stroke(password_length)+"; # ")
