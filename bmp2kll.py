#!/usr/bin/python3

import argparse

from controller.Scan.STLcd.bitmap2Struct import ImageToStruct

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename",
                        type=str,
                        required=True,
                        help="provide .bmp file")
    parser.add_argument("-s", "--size",
                        type=int,
                        required=False,
                        default=128,
                        help="provide the image width: '128' for default or '32' for layer image")
    args = parser.parse_args()
    filename = args.filename
    prep = ImageToStruct(filename)

    if args.size != 128:
        prep.max_width = args.size

    prep.preview()
    prep.output_image_fn()
    print("uint8_t array[] = {}".format(prep.getarray(string=True)))
