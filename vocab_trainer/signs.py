from random import randrange

from cement.core.exc import CaughtSignal

from .util import Timer

syllable_table = ['a', 'i', 'u', 'e', 'o',  #
                  'ka', 'ga', 'sa', 'za', 'ta', 'da', 'na',  #
                  'ki', 'gi', 'shi', 'ji', 'chi', 'di', 'ni',  #
                  'ku', 'gu', 'su', 'zu', 'tu', 'du', 'nu',  #
                  'ke', 'ge', 'se', 'ze', 'te', 'de', 'ne',  #
                  'ko', 'go', 'so', 'zo', 'to', 'do', 'no']


def signs():
    while True:
        index = randrange(len(syllable_table))
        syllable = syllable_table[index]

        with Timer(syllable) as t:
            try:
                command = input(syllable)

                if command == 'q':
                    break
                elif command == 'c':
                    t.correct()
                elif command == 'i':
                    t.incorrect()

            except KeyboardInterrupt:
                break
            except CaughtSignal:
                break


def generate_syllable_table():
    vowels = ['a', 'i', 'u', 'e', 'o']
    consonants = ['k', 'g', 's', 'z', 't', 'd', 'n']

    table = vowels.copy()
    for vowel in vowels:
        for consonant in consonants:
            con_letter = consonant + vowel
            table.append(con_letter)
    return table
