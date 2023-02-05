#! /usr/bin/env python3

import argparse
import string

import nltk

if __name__ == '__main__':
    # Argument parser
    parser = argparse.ArgumentParser(
        prog='count_words',
        description='Count words in a text document'
    )
    parser.add_argument('filename',
        help='text file that contains the text to be analyzed'
    )
    parser.add_argument('--sort',
        choices=['alpha', 'freq'],
        default='freq',
        help='(default: %(default)s) '
             'sort order in which the results are to be returned'
    )
    args = parser.parse_args()

    # Read document
    with open(args.filename, 'r') as infile:
        document = infile.readlines()

    # Basic preprocessing
    for i in range(len(document)):
        new_line = document[i].translate(str.maketrans('', '', string.punctuation))
        new_line = new_line.strip().lower()
        document[i] = new_line

    # Initialize Porter stemmer
    stemmer = nltk.stem.porter.PorterStemmer()

    # Count words
    word_counts = {}
    for line in document:
        for word in line.split():
            stem = stemmer.stem(word)
            if stem not in word_counts:
                word_counts[stem] = 0
            word_counts[stem] += 1

    # Output result
    if args.sort == 'freq':
        sort_key = lambda x: (-x[1], x[0])
    else:
        sort_key = lambda x: (x[0], -x[1])
    for word, cnt in sorted(word_counts.items(), key=sort_key):
        print(f'{cnt:4d} - {word}')
