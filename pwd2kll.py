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

TRIGGER_SET = ["W", "E", "R",
               "S", "D", "F",
               "X", "C", "V"
               ]


def generate_key_stroke(length):
    seed = [randrange(len(KEY_SET)) for _ in range(length)]
    stroke = []
    for i in seed:
        if randrange(2):
            stroke.append(STROKE_FORMAT.format(KEY_SET[i]))
        else:
            stroke.append(" + ".join([STROKE_FORMAT.format("LShift"), STROKE_FORMAT.format(KEY_SET[i])]))
    return ", ".join(stroke)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length",
                        type=int,
                        required=False,
                        default=8,
                        help="length of the keystrokes")

    args = parser.parse_args()
    password_length = args.length

    for t in TRIGGER_SET:
        print(STROKE_FORMAT.format(t) + " : " + generate_key_stroke(password_length) + "; # ")
