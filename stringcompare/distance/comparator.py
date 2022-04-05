from abc import ABC, abstractmethod
import numpy as np
from typing import Generic, TypeVar, List

T = TypeVar("T")


class Comparator(ABC, Generic[T]):
    @abstractmethod
    def compare(s: T, t: T) -> float:
        """
        Comparison between two elements.

        Parameters
        ----------
        s:
            element to compare from.
        t:
            element to compare to.

        Returns
        -------
        Number indicating similarity level between the two elements. This is not necessarily normalized or symmetric.
        """
        pass

    def __call__(self, s: T, t: T) -> float:
        return self.compare(s, t)

    def pairwise(self, l1: List[T], l2: List[T]) -> np.ndarray:
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
        Matrix of dimension len(l1)xlen(l2), where each row corresponds to an
        element of l1 and each column corresponds to an element of l2.
        """
        return np.array([[self.compare(s, t, self.dmat) for t in l2] for s in l1])

    def elementwise(self, l1: List[T], l2: List[T]) -> np.ndarray:
        return np.array([self.compare(s, t, self.dmat) for s, t in zip(l1, l2)])


class StringComparator(Comparator[str]):
    pass


class NumericComparator(Comparator[float]):
    pass
