import os
from datetime import datetime

TIME_FORMAT = "%d/%m/%Y"


def combine_lessons(vocab):
    result = []
    for v in vocab.values():
        result += v
    return result


def flatten_vocab(vocab: dict) -> list:
    all_lessons = combine_lessons(vocab)
    return list(map(lambda x: x[0] + x[1], all_lessons))


def load_vocab(filename: str = './vocab.txt') -> dict:
    vocab_table = {}
    current_table = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if line[0] == '-':
                key = line[1:].strip("\n")
                vocab_table[key] = current_table.copy()
                current_table.clear()
                continue

            japanese, german = line.split('|')

            def to_list(word):
                return list(map(str.strip, word.split(':')))

            japanese = to_list(japanese)
            german = to_list(german)
            current_table.append((japanese, german))
    return vocab_table


def load_times(filename: str = './times.txt'):
    times = {}

    if not os.path.exists(filename):
        return times

    with open(filename, 'r') as f:
        for line in f.readlines():
            date, key, time, status = line.split(":")
            time = float(time)
            date = datetime.strptime(date, TIME_FORMAT)
            if key not in times:
                times[key] = []
            times[key].append((date, time, status[:-1]))
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
        time_diff = (self.end - self.start).total_seconds()
        current_time = datetime.now().strftime(TIME_FORMAT)
        line = current_time + ":" + self.element + ":" + str(time_diff) + ":" + self.status + "\n"
        with open('./times.txt', 'a') as f:
            f.write(line)

    def correct(self):
        self.status = 'c'

    def incorrect(self):
        self.status = 'i'
