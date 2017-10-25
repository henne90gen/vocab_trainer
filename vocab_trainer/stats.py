from .util import load_times, load_vocab, flatten_vocab
from matplotlib import pyplot as plt


def average_answer_time():
    times = load_times()
    vocab = load_vocab()
    vocab = flatten_vocab(vocab)

    data = []
    for v in vocab:
        data.append([])
        for w in v:
            if w in times:
                data[-1] = data[-1] + times[w]

    def average(x):
        if len(x) == 0:
            return 0
        return sum(x) / len(x)

    # selecting time differences from the  available data and averaging times
    data = list(map(average, map(lambda arr: [x[1] for x in arr], data)))

    indices = range(len(vocab))

    # sorting data ascending by average time
    combined_data = zip(vocab, data)
    combined_data = sorted(combined_data, key=lambda x: x[1])
    vocab, data = zip(*combined_data)

    plt.bar(x=indices, height=data)

    plt.xticks(indices, vocab, rotation=90)
    plt.ylabel("Average time")
    plt.subplots_adjust(bottom=0.3, top=0.975, left=0.1, right=0.975)
    plt.show()


def total_asked():
    times = load_times()
    vocab = load_vocab()
    vocab = flatten_vocab(vocab)
    correct_data = []
    incorrect_data = []

    for v in vocab:
        correct_data.append(0)
        incorrect_data.append(0)
        for w in v:
            if w in times:
                arr = list(map(lambda x: x[2], times[w]))
                num_correct = len(list(filter(lambda x: x == 'c', arr)))
                num_incorrect = len(list(filter(lambda x: x == 'i', arr)))
                correct_data[-1] += num_correct
                incorrect_data[-1] += num_incorrect

    combined_data = zip(vocab, correct_data, incorrect_data)
    combined_data = sorted(combined_data, key=lambda x: x[1])
    combined_data = sorted(combined_data, key=lambda x: x[2])
    vocab, correct_data, incorrect_data = zip(*combined_data)

    indices = range(len(vocab))

    plt.bar(x=indices, height=correct_data, bottom=incorrect_data, color='g')
    plt.bar(x=indices, height=incorrect_data, color='r')

    plt.xticks(indices, vocab, rotation=90)
    plt.ylabel("Average time")
    plt.subplots_adjust(bottom=0.3, top=0.975, left=0.1, right=0.975)
    plt.show()
