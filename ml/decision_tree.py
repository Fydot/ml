#!/usr/bin/env python
# coding: utf8
from collections import Counter
from math import log
import sys
import random


def create_data_labels():
    data = [[0, 0, 0, 'x'],
            [0, 1, 1, 'y'],
            [0, 1, 0, 'y'],
            [0, 0, 1, 'y'],
            [1, 1, 1, 'x']]
    labels = ['A', 'B', 'A', 'B', 'C']
    return data, labels


def split_data(data, axis, value):
    ret_data = []
    for vec in data:
        if vec[axis] == value:
            reduced_vec = vec[:axis]
            reduced_vec.extend(vec[axis+1:])
            ret_data.append(reduced_vec)
    return ret_data


def calc_ent(data, col):
    kinds = Counter()
    entries_num = len(data)
    for vector in data:
        kinds[vector[col]] += 1
    ps = [kinds[kind] * 1.0 / entries_num for kind in kinds]
    return sum([-(p * log(p, 2)) for p in ps])


def choose_feature(data):
    length = len(data[0])
    ents = [(i, calc_ent(data, i)) for i in range(length)]
    ents = sorted(ents, key=lambda x: x[1])
    return ents[-1][0]


def create_tree(data, labels):
    if len(set(labels)) == 1:
        return labels[0]
    if len(data[0]) == 0:
        if len(labels) > 0:
            label_c = Counter()
            for label in labels:
                label_c[label] += 1
            return label_c.most_common(1)[0][0]
        else:
            return "unknown"

    best = choose_feature(data)
    tree = {best: {}}
    values = set([vec[best] for vec in data])
    for value in values:
        lbs = [label for label, vec in zip(labels, data) if vec[best] == value]
        tree[best][value] = create_tree(split_data(data, best, value), lbs)
    return tree


def show(step, tree):
    if type(tree) != dict:
        print step * " ", tree
        return
    for k in tree:
        print step * " ", k
        show(step + 1, tree[k])


def classify(vec, tree):
    root = tree.keys()[0]
    myt = tree
    while True:
        myt = myt[root][vec[root]]
        if type(myt) is not dict:
            return myt
        root = myt.keys()[0]


def gen_data(n, m):
    x = []
    for i in range(n):
        x.append([])
        for j in range(m):
            x[i].append(random.randint(1, 10))
    return x


def gen_label(m):
    return [random.randint(1, 10) for i in range(m)]


if __name__ == "__main__":
    # data = [[0, 0, 0, 'x'],
    #         [0, 1, 1, 'y'],
    #         [0, 1, 0, 'y'],
    #         [0, 0, 1, 'y'],
    #         [1, 1, 1, 'x']]
    # labels = ['A', 'B', 'A', 'B', 'C']
    print gen_data(100, 10), gen_label(10)



    tree = create_tree(gen_data(100, 10), gen_label(10))

    print classify(gen_label(10), tree)