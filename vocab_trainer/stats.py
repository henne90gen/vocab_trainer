from .util import load_times, load_vocab


def stats():
    times = load_times()
    vocab = load_vocab()
    print(times)
    print(vocab)
