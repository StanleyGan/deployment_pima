from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class MissingNaNImputer(BaseEstimator, TransformerMixin):
    """Replace 0 values with NaN for specified columns

    Args:
        columns (A list of str or a str): Defaults to None
    """
    def __init__(self, columns=None):
        self.columns = columns

    def fit(self, X, y):
        """ To accommodate sklearn pipeline
        """
        return self

    def transform(self, X):
        """
        Args:
            X (A pd.DataFrame)
        """
        X_ = X.copy()
        for c in self.columns:
            X_.loc[X[c] == 0, c] = np.nan

        return X_
