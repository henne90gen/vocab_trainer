from random import randrange

from cement.core.exc import CaughtSignal

from .util import Timer

syllable_table = ['a', 'ka', 'ga', 'sa', 'za', 'ta', 'da', 'na', 'ha', 'ba', 'pa', 'ma', 'ra',  #
                  'i', 'ki', 'gi', 'shi', 'ji', 'chi', 'di', 'ni', 'hi', 'bi', 'pi', 'mi', 'ri',  #
                  'u', 'ku', 'gu', 'su', 'zu', 'tsu', 'du', 'nu', 'hu', 'bu', 'pu', 'mu', 'ru',  #
                  'e', 'ke', 'ge', 'se', 'ze', 'te', 'de', 'ne', 'he', 'be', 'pe', 'me', 're',  #
                  'o', 'ko', 'go', 'so', 'zo', 'to', 'do', 'no', 'ho', 'bo', 'po', 'mo', 'ro',  #
                  'ya', 'kya', 'gya', 'sha', 'ja', 'cha', 'dya', 'nya', 'hya', 'bya', 'pya', 'mya', 'rya',  #
                  'yu', 'kyu', 'gyu', 'shu', 'ju', 'chu', 'dyu', 'nyu', 'hyu', 'byu', 'pyu', 'myu', 'ryu',  #
                  'yo', 'kyo', 'gyo', 'sho', 'jo', 'cho', 'dyo', 'nyo', 'hyo', 'byo', 'pyo', 'myo', 'ryo',  #
                  'wa', 'wo', 'n']


def get_choice_table(sign_choice: str) -> list:
    result = []
    for sign in syllable_table:
        if sign[0] in sign_choice:
            result.append(sign)
    return result


def signs(sign_choice: str):
    while True:
        if not sign_choice:
            index = randrange(len(syllable_table))
            syllable = syllable_table[index]
        else:
            table = get_choice_table(sign_choice)
            index = randrange(len(table))
            syllable = table[index]

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
