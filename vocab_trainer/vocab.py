from random import randrange

from cement.core.exc import CaughtSignal

from .util import Timer, load_vocab


def select_random(arr):
    index = randrange(len(arr))
    return arr[index], index


def select_vocab(vocab_table, lang):
    rand_vocab, v_index = select_random(vocab_table)

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


def training(lang):
    vocab_table = load_vocab()

    while True:

        word, translations = select_vocab(vocab_table, lang)

        if ask_word(word, translations) == 'break':
            break


def test(lang):
    vocab_table = load_vocab()

    num_correct = 0
    num_incorrect = 0

    while len(vocab_table) > 0:

        word, translations = select_vocab(vocab_table, lang)

        rem = None
        for v in vocab_table:
            if translations in v:
                rem = v
                break
        vocab_table.remove(rem)

        status = ask_word(word, translations)
        if status == 'break':
            break
        elif status == 'correct':
            num_correct += 1
        elif status == 'incorrect':
            num_incorrect += 1

    print('Correct: ' + str(num_correct) + " | Incorrect: " + str(num_incorrect))
