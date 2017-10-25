from datetime import datetime
from unittest import TestCase

import os

from vocab_trainer.util import load_vocab, flatten_vocab, combine_lessons, load_times


class Test(TestCase):
    def test_load_vocab(self):
        filename = './test_load_vocab.txt'
        lines = ['something|etwas:hallo', "hello|hallo", "-W1", "more|mehr"]
        with open(filename, 'w') as f:
            for line in lines:
                f.write(line + "\n")
        vocab = load_vocab(filename)

        expected_vocab = {"W1": [(['something'], ['etwas', 'hallo']), (['hello'], ['hallo'])]}
        for key, value in expected_vocab.items():
            for li, l in enumerate(value):
                self.assertEqual(len(l), len(vocab[key][li]))
                self.assertEqual(len(l[0]), len(vocab[key][li][0]))
                self.assertEqual(len(l[1]), len(vocab[key][li][1]))
                for wi, w in enumerate(l):
                    self.assertEqual(w, vocab[key][li][wi])
        os.remove(filename)

    def test_flatten_vocab(self):
        vocab = {"W1": [(['something'], ['etwas', 'hallo']), (['hello'], ['hallo'])],
                 "W2": [(['somethong'], ['etwes', 'höllo']), (['hollo'], ['hillo'])]}
        expected_vocab = [['something', 'etwas', 'hallo'], ['hello', 'hallo'], ['somethong', 'etwes', 'höllo'],
                          ['hollo', 'hillo']]
        actual_vocab = flatten_vocab(vocab)
        for vi, v in enumerate(expected_vocab):
            self.assertEqual(v, actual_vocab[vi])

    def test_combine_lessons(self):
        vocab = {"W1": [(['something'], ['etwas', 'hallo']), (['hello'], ['hallo'])],
                 "W2": [(['somethong'], ['etwes', 'höllo']), (['hollo'], ['hillo'])]}
        expected_vocab = [(['something'], ['etwas', 'hallo']), (['hello'], ['hallo']),
                          (['somethong'], ['etwes', 'höllo']), (['hollo'], ['hillo'])]
        actual_vocab = combine_lessons(vocab)
        for vi, v in enumerate(expected_vocab):
            self.assertEqual(v, actual_vocab[vi])

    def test_load_times(self):
        filename = "./test_load_times.txt"
        with open(filename, "w") as f:
            f.write("20/10/2017:Park:8:c\n")
            f.write("20/10/2017:World:9:c\n")
            f.write("19/10/2017:World:7:c\n")

        times = load_times(filename)

        expected_times = {'Park': [(datetime(2017, 10, 20, 0, 0), 8, 'c')],
                          'World': [(datetime(2017, 10, 20, 0, 0), 9, 'c'), (datetime(2017, 10, 19, 0, 0), 7, 'c')]}

        for key, value in expected_times.items():
            self.assertTrue(key in times)
            self.assertEqual(value, times[key])

        os.remove(filename)
