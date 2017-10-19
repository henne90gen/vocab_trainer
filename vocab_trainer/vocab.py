from random import randrange

from cement.core.exc import CaughtSignal

from .util import Timer


def read_vocab():
    vocab_table = []
    with open('./vocab.txt', 'r') as f:
        for line in f.readlines():
            japanese, german = line.split('|')

            def to_list(word):
                return list(map(str.strip, word.split(':')))

            japanese = to_list(japanese)
            german = to_list(german)
            vocab_table.append((japanese, german))
    return vocab_table


def select_random(arr):
    index = randrange(len(arr))
    return arr[index]


def select_vocab(vocab_table):
    v_index = randrange(len(vocab_table))
    rand_vocab = vocab_table[v_index]

    l_index = randrange(len(rand_vocab))
    rand_language = rand_vocab[l_index]
    if l_index == 0:
        translations = rand_vocab[1]
    else:
        translations = rand_vocab[0]

    w_index = randrange(len(rand_language))
    word = rand_language[w_index]

    return word, translations


def vocab():
    vocab_table = read_vocab()

    while True:

        word, translations = select_vocab(vocab_table)

        with Timer(word) as t:
            try:
                input_word = input(word + '\n')

                input_word = input_word.strip()

                if input_word == ':q':
                    break
                if input_word == ':r':
                    vocab_table = read_vocab()

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
