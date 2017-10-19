from random import randrange

from cement.core.exc import CaughtSignal

from .util import Timer, load_vocab


def select_random(arr):
    index = randrange(len(arr))
    return arr[index]


def select_vocab(vocab_table):
    def rand(arr):
        index = randrange(len(arr))
        return arr[index], index

    rand_vocab, v_index = rand(vocab_table)
    rand_language, l_index = rand(rand_vocab)

    if l_index == 0:
        translations = rand_vocab[1]
    else:
        translations = rand_vocab[0]

    word, w_index = rand(rand_language)

    return word, translations


def vocab():
    vocab_table = load_vocab()

    while True:

        word, translations = select_vocab(vocab_table)

        with Timer(word) as t:
            try:
                input_word = input(word + '\n')

                input_word = input_word.strip()

                if input_word == ':q':
                    break
                if input_word == ':r':
                    vocab_table = load_vocab()

                if input_word in translations:
                    t.correct()
                    print('Correct!')
                else:
                    t.incorrect()
                    msg = 'Incorrect: '
                    for ind, w in enumerate(translations):
                        msg = msg + w
                        msg = msg + ', '
                    print(msg[:-2])

            except KeyboardInterrupt:
                break
            except CaughtSignal:
                break
