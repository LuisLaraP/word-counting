#! /usr/bin/env python3

import argparse
import string
import sys

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
    parser.add_argument('--stemmer',
        choices=['on', 'off'],
        default='on',
        help='(default: %(default)s) '
             'turn the Porter stemmer on or off'
    )
    parser.add_argument('--syn-file',
        help='path to the synonyms file. '
             'If it is not given, no synonym replacement will be done'
    )
    parser.add_argument('--stopwords-file',
        help='path to the stopwords file. '
             'If it is not given, no stopwords will be removed'
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

    # Synonym replacement
    if args.syn_file is not None:
        try:
            # Read synonyms file
            synonyms = {}
            with open(args.syn_file, 'r') as infile:
                for line in infile:
                    target, _,  terms = line.partition(':')
                    target = target.strip()
                    terms = terms.split(',')
                    for term in terms:
                        synonyms[term.strip()] = target

            # Replace synonyms
            for i in range(len(document)):
                new_line = document[i]
                for term, repl in synonyms.items():
                    new_line = new_line.replace(term, repl)
                document[i] = new_line
        except FileNotFoundError:
            print(f"ERROR: Synonyms file '{args.syn_file}' not found.", file=sys.stderr)
            exit()

    # Read stopwords file
    if args.stopwords_file is not None:
        try:
            with open(args.stopwords_file, 'r') as infile:
                stopwords = {line.strip() for line in infile if line}
        except FileNotFoundError:
            print(f"ERROR: Stopwords file '{args.stopwords_file}' not found.", file=sys.stderr)
            exit()
    else:
        stopwords = set()

    # Initialize Porter stemmer
    if args.stemmer == 'on':
        stemmer = nltk.stem.porter.PorterStemmer()

    # Count words
    word_counts = {}
    for line in document:
        for word in line.split():
            if args.stemmer == 'on':
                stem = stemmer.stem(word)
            else:
                stem = word
            if stem in stopwords:
                continue
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
