# Sebastian Raschka 2016-2017
#
# ann is a supporting package for the book
# "Introduction to Artificial Neural Networks and Deep Learning:
#  A Practical Guide with Applications in Python"
#
# Author: Sebastian Raschka <sebastianraschka.com>
#
# License: MIT

import unittest
import os
import inspect
import numpy as np
from ann.np.perceptron import perceptron_train
from ann.np.perceptron import perceptron_predict


class TestPerceptron(unittest.TestCase):

    this_dir = os.path.dirname(os.path.abspath(inspect.getfile(
                               inspect.currentframe())))
    iris_fname = os.path.join(this_dir, 'iris_binary.csv')
    data = np.genfromtxt(fname=iris_fname, delimiter=',')
    X, y = data[:, :4], data[:, 4]

    def test_zero_weights(self):

        X, y = self.X, self.y
        model_mparams = perceptron_train(X, y, mparams=None, zero_weights=True)

        assert model_mparams['weights'][0] == 7.

        for _ in range(5):
            _ = perceptron_train(X, y, mparams=model_mparams)

        errors = np.sum(perceptron_predict(X, model_mparams) != y)

        assert errors == 0
        assert round(model_mparams['weights'][0], 1) == -1.1

    def test_random_weights(self):

        X, y = self.X, self.y
        model_mparams = perceptron_train(X, y, mparams=None,
                                         zero_weights=False, seed=1)

        assert round(model_mparams['weights'][0], 1) == 2.1

        for _ in range(5):
            _ = perceptron_train(X, y, mparams=model_mparams)

        errors = np.sum(perceptron_predict(X, model_mparams) != y)

        assert errors == 0
        assert round(model_mparams['weights'][0], 1) == -1.1


if __name__ == '__main__':
    unittest.main()
