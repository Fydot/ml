#!/usr/bin/env python
# coding: utf8
from collections import Counter


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
        else: print "the word: %s is not in my Vocabulary!" % word
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
                if point[i] == 1:
                    label_feature_cnt[label][i] += 1

    label_feature_p = {}
    for label in label_feature_cnt:
        label_feature_p[label] = []
        for i in range(len(data[0])):
            count = sum([label_feature_cnt[label][i] for i in label_feature_cnt[label]])
            label_feature_p[label].append(label_feature_cnt[label][i] * 1.0 / count)

    return label_feature_p, {label: len(labels_idx[label]) * 1.0 / len(labels) for label in labels_idx}


if __name__ == "__main__":
    posts, labels = load_data_set()
    features = get_featurs(posts)
    data = [words2vec(features, post) for post in posts]
    p_feature, p_label = train_nb(data, labels)
    print features, p_feature, p_label