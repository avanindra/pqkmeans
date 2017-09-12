import typing
import numpy
import sklearn

import _pqkmeans


class PQKMeans(sklearn.base.BaseEstimator, sklearn.base.ClusterMixin):
    def __init__(self, encoder, k, iteration=10, verbose=False):
        super().__init__()
        self._impl = _pqkmeans.PQKMeans(encoder.codewords, k, iteration, verbose)

    def predict_generator(self, x_test: typing.Iterable[typing.Iterable[numpy.uint8]]):
        print("!!!!!!!!predict_generator")
        for vec in x_test:
            yield self._impl.predict_one(vec)

    def fit(self, x_train: numpy.array):
        print("!!!!!!!!fit")
        assert len(x_train.shape) == 2
        self._impl.fit(x_train)

    def predict(self, x_test: numpy.array):
        assert len(x_test.shape) == 2
        print("!!!!!!!!!!predict")
        return numpy.array(list(self.predict_generator(x_test)))

    @property
    def labels_(self):
        return self._impl.labels_

    @property
    def cluster_centers_(self):
        return self._impl.cluster_centers_

