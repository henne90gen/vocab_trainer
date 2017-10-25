from random import randrange

from cement.core.exc import CaughtSignal

from .util import Timer, load_vocab, combine_lessons


def select_vocab(vocab_list, lang):
    def select_random(arr):
        index = randrange(len(arr))
        return arr[index], index

    rand_vocab, v_index = select_random(vocab_list)

    if lang == 0 or lang == 1:
        rand_language = rand_vocab[lang]
        l_index = int(lang)
    else:
        rand_language, l_index = select_random(rand_vocab)

    translations = rand_vocab[int(not l_index)]

    word, w_index = select_random(rand_language)

    return word, translations


def ask_word(word, translations):
    with Timer(word) as t:
        try:
            input_word = input(word + '\n')

            input_word = input_word.strip()

            if input_word == ':q':
                return 'break'

            if input_word in translations:
                t.correct()
                print('Correct!')
                return 'correct'
            else:
                t.incorrect()
                msg = 'Incorrect: '
                for ind, w in enumerate(translations):
                    msg = msg + w
                    msg = msg + ', '
                print(msg[:-2])
                return 'incorrect'

        except KeyboardInterrupt:
            return 'break'
        except CaughtSignal:
            return 'break'


def valid_lesson(vocab_table: dict, lesson: str) -> list:
    if lesson and lesson not in vocab_table:
        print("This lesson doesn't exist. Choose one of the following")
        print(', '.join(vocab_table.keys()))
        return []

    if not lesson:
        return combine_lessons(vocab_table)

    return vocab_table[lesson]


def training(lesson: str = None, lang: int = -1):
    vocab_table = load_vocab()

    vocab_list = valid_lesson(vocab_table, lesson)
    if len(vocab_list) == 0:
        return

    while True:

        word, translations = select_vocab(vocab_list, lang)

        if ask_word(word, translations) == 'break':
            break


def test(lesson: str = None, lang: int = -1):
    vocab_table = load_vocab()

    vocab_list = valid_lesson(vocab_table, lesson)
    if len(vocab_list) == 0:
        return

    num_correct = 0
    num_incorrect = 0

    while len(vocab_list) > 0:

        word, translations = select_vocab(vocab_list, lang)

        rem = None
        for v in vocab_list:
            if translations in v:
                rem = v
                break
        vocab_list.remove(rem)

        status = ask_word(word, translations)
        if status == 'break':
            break
        elif status == 'correct':
            num_correct += 1
        elif status == 'incorrect':
            num_incorrect += 1

    print('Correct: ' + str(num_correct) + " | Incorrect: " + str(num_incorrect))
