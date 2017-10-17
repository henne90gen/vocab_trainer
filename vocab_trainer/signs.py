from random import randrange
from datetime import datetime

import os


def signs():
    syllable_table = ['a', 'i', 'u', 'e', 'o', 'ka', 'ga', 'sa', 'za', 'ki', 'gi', 'si', 'zi', 'ku', 'gu', 'su', 'zu',
                      'ke', 'ge', 'se', 'ze', 'ko', 'go', 'so', 'zo']

    times = []

    while True:
        index = randrange(len(syllable_table))
        syllable = syllable_table[index]
        start = datetime.now()
        try:
            command = input(syllable)

            if command == 'q':
                break

            end = datetime.now()
            time_diff = end - start
            times.append((syllable, time_diff.microseconds))
        except KeyboardInterrupt:
            break

    append_times(times)
    print()


def generate_syllable_table():
    vowels = ['a', 'i', 'u', 'e', 'o']
    consonants = ['k', 'g', 's', 'z']

    syllable_table = vowels.copy()
    for vowel in vowels:
        for consonant in consonants:
            con_letter = consonant + vowel
            syllable_table.append(con_letter)
    return syllable_table


def load_times():
    times = {}

    if not os.path.exists('./times.txt'):
        return times

    with open('./times.txt', 'r') as f:
        for line in f.readlines():
            key, time = line.split(":")
            time = int(time)
            if key not in times:
                times[key] = []
            times[key].append(time)
    return times


def append_times(times):
    with open('./times.txt', 'a') as f:
        for elem in times:
                f.write(elem[0] + ":" + str(elem[1]) + "\n")
