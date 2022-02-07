import digits
from classes import Neighbour, Test

K = 5

train_file = './inputs/train60000.in'
training_samples = digits.initialise_training_samples(Neighbour, train_file)


def init(test_digit):
    test_sample = digits.initialise_testing_sample(Test, test_digit)
    print("Analyzing digit...")
    print(digits.find_most_common(training_samples, test_sample, K), end='')
