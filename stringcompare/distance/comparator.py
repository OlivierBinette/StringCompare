from abc import ABC, abstractmethod
import numpy as np


class Comparator(ABC):

    @abstractmethod
    def compare(e1, e2):
        """
        Comparison between two elements.

        Parameters
        ----------
        e1:
            element to compare from.
        e1:
            element to compare to.

        Returns
        -------
        Number indicating similarity level between the two elements. This is not necessarily normalized or symmetric.
        """
        pass

    def __call__(self, e1, e2):
        return self.compare(e1, e2)

    def pairwise(self, l1, l2):
        """
        Pairwise comparisons between two lists.

        Parameters
        ----------
        l1: list
            List of elements to compare from.
        l2: list
            List of elements to compare to.

        Returns
        -------
        Matrix of dimension len(l1)xlen(l2), where each row corresponds to an element of l1 and each column corresponds to an element of l2.
        """
        return np.array([[self.compare(s, t, self.dmat) for t in l2] for s in l1])

    def elementwise(self, l1, l2):
        return np.array([self.compare(s, t, self.dmat) for s, t in zip(l1, l2)])


class StringComparator(Comparator):
    pass


class NumericComparator(Comparator):
    pass
