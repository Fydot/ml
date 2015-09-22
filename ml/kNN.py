#!/usr/bin/env python
# coding: utf8
import numpy
from collections import Counter


def create_data_set():
    group = numpy.random.rand(100, 20)
    labels = numpy.random.rand(100)
    labels = [label >= 0.5 for label in labels]
    return group, labels


def classify(X, data_set, labels, k):
    def o_dis_square(X, Y):
        return sum([(x - y) ** 2 for x, y in zip(X, Y)])

    distances = [(labels[idx], o_dis_square(X, Y)) for idx, Y in zip(range(len(data_set)), data_set)]
    distances = sorted(distances, key=lambda c: c[1])[:k]
    labels_counter = Counter()
    for idx, _ in distances:
        labels_counter[idx] += 1
    return labels_counter.most_common(1)[0][0]


if __name__ == "__main__":
    group, labels = create_data_set()
    X = numpy.random.rand(20)
    print X, classify(X, group, labels, 20)