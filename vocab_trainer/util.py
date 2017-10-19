import os
from datetime import datetime


def load_vocab():
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


def load_times():
    times = {}

    if not os.path.exists('./times.txt'):
        return times

    with open('./times.txt', 'r') as f:
        for line in f.readlines():
            key, time, status = line.split(":")
            time = int(time)
            if key not in times:
                times[key] = []
            times[key].append((time, status[:-1]))
    return times


class Timer:
    """
    u := undefined
    c := correct
    i := incorrect
    """

    def __init__(self, element):
        self.start = None
        self.end = None
        self.element = element
        self.status = 'u'

    def __enter__(self):
        self.start = datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = datetime.now()
        time_diff = self.end - self.start
        with open('./times.txt', 'a') as f:
            f.write(self.element + ":" + str(time_diff.microseconds) + ":" + self.status + "\n")

    def correct(self):
        self.status = 'c'

    def incorrect(self):
        self.status = 'i'
