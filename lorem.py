#! /usr/bin/env python


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eget augue at felis faucibus tristique ac nec tortor. Vivamus ac eros facilisis, fringilla lectus vitae, tincidunt nisi. Integer vel dolor libero. Praesent vestibulum pretium turpis, a dignissim ligula ultricies ut. Nunc sem nulla, maximus a mattis non, gravida vitae eros. Donec euismod porta quam. Morbi rutrum, dolor id viverra aliquet, purus enim iaculis libero, sed cursus mauris massa a velit. Ut nec consequat dolor. "

import argparse

parser = argparse.ArgumentParser(description="Print Lorem Ipsum text to the terminal.")

parser.add_argument('-n', '--number', type=int, help="How many times the lorem ipsum text will be printed", default=1, required=False)

args = parser.parse_args()

if 0 <= args.number <= 20:
    for i in range(args.number):
        print(text + "\n")
if args.number > 20:
    for i in range(20):
        print(text + "\n")
