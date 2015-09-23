#!/usr/bin/env python
# coding: utf8
from collections import Counter
import random
import math


def load_data_set():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]    #1 is abusive, 0 not
    return postingList,classVec


def get_featurs(dataSet):
    vocabSet = set([])  #create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document) #union of the two sets
    return list(vocabSet)


def words2vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word: %s is not in my Vocabulary!" % word
    return returnVec


def train_nb(data, labels):
    labels_idx = {}
    for i in range(len(labels)):
        if labels[i] not in labels_idx:
            labels_idx[labels[i]] = []
        labels_idx[labels[i]].append(i)

    label_feature_cnt = {}
    for label in labels_idx:
        label_feature_cnt[label] = Counter()
        for idx in labels_idx[label]:
            point = data[idx]
            for i in range(len(point)):
                label_feature_cnt[label][i] += point[i]

    label_feature_p = {}
    for label in label_feature_cnt:
        label_feature_p[label] = []
        for i in range(len(data[0])):
            count = sum([label_feature_cnt[label][i] for i in label_feature_cnt[label]]) + 2
            label_feature_p[label].append(math.log((label_feature_cnt[label][i] + 1) * 1.0 / count, 2))

    return label_feature_p, {label: len(labels_idx[label]) * 1.0 / len(labels) for label in labels_idx}


def classify(features_p, label_p, vector):
    def mult(v1, v2):
        return [x * y for x, y in zip(v1, v2)]

    return [(label, sum(mult(vector, features_p[label])) + math.log(label_p[label], 2)) for label in features_p]


def gen_data(m, n):
    data = []
    for i in range(m):
        data.append([])
        for j in range(n):
            data[i].append(int(random.randint(1, 10) >= 5))
    return data

def gen_labels(n):
    return [map(chr, range(65, 91))[random.randint(1, 100000) % 10] for i in range(n)]

if __name__ == "__main__":
    # posts, labels = load_data_set()
    # features = get_featurs(posts)
    # data = [words2vec(features, post) for post in posts]
    # p_feature, p_label = train_nb(data, labels)
    data = gen_data(100, 10)
    labels = gen_labels(100)
    p_feature, p_label = train_nb(data, labels)

    # for label, vector in zip(labels, data):
    #     print label, vector

    vector = gen_data(1, 10)[0]
    print vector, sorted(classify(p_feature, p_label, vector), key=lambda x: x[1])[-1][0]