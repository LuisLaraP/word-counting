#! /usr/bin/env python3

import string
import sys

if __name__ == '__main__':
    filename = sys.argv[1]

    # Read document
    with open(filename, 'r') as infile:
        document = infile.readlines()

    # Basic preprocessing
    for i in range(len(document)):
        new_line = document[i].translate(str.maketrans('', '', string.punctuation))
        new_line = new_line.strip().lower()
        document[i] = new_line
    print(document)

    # Count words
    word_counts = {}
    for line in document:
        for word in line.split():
            if word not in word_counts:
                word_counts[word] = 0
            word_counts[word] += 1

    # Output result
    for word, cnt in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
        print(f'{cnt:4d} - {word}')
