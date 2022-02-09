import digits
from classes import Neighbour, Test

# Number of nearest neighbours to evaluate
K = 5

# Location of the training samples
train_file = './inputs/train60000.in'

# Initialises a list of digit objects containing the training samples
training_samples = digits.initialise_training_samples(Neighbour, train_file)


def init(test_digit):
    test_sample = digits.initialise_testing_sample(Test, test_digit)
    print("Analyzing digit...")
    print(
        f"My guess is: {digits.find_most_common(training_samples, test_sample, K)}", end='')
