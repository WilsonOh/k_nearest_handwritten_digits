from collections import Counter

import numpy as np


def initialise_training_samples(cls, file):
    """Creates a list of Neighbour objects and initialises
        reads in their label and digit matrix from the triaining
        sample file"""
    with open(file) as f:
        n = int(f.readline()[:-1])
        obj_list = [cls() for _ in range(n)]
        for digit in obj_list:
            digit.read_digits(f)
    return obj_list


def initialise_testing_sample(cls, grid):
    """Same function as the one for training samples
        except it's the digit matrix is being read in
        from user input"""
    test = cls()
    test.read_digits(grid)
    return test


def get_diff(digit1, digit2) -> np.ndarray:
    """Returns the number of differing pixels between two digit matrices"""
    return np.sum(digit1 != digit2)


def find_most_common(training_samples, test_sample, K):
    """Return the most common label within the list of K
        nearest neighbours"""
    for training_sample in training_samples:
        training_sample.distance = get_diff(test_sample.ar, training_sample.ar)
    return Counter(find_k_nearest(training_samples, K)).most_common(1)[0][0]


def find_k_nearest(training_samples, K):
    """Returns a list of K neighbours that have the smallest distance
        to the test digit"""
    k_nearest = np.sort(training_samples)[:K]
    return [digit.label for digit in k_nearest]
