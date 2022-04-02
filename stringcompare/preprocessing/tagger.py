from abc import ABC, abstractmethod


class Tagger(ABC):
    @property
    @classmethod
    @abstractmethod
    def LABELS(cls):
        pass

    def __call__(self, obj):
        return self.tag(obj)

    @abstractmethod
    def tag(self, obj):
        pass

    def batch_tag(self, objs):
        return [self.tag(obj) for obj in objs]


class DeepparseAddressTagger(Tagger):

    LABELS = [
        "StreetNumber",
        "StreetName",
        "Unit",
        "Municipality",
        "Province",
        "PostalCode",
        "Orientation",
        "GeneralDelivery",
    ]

    def __init__(self, deepparse_handle):
        assert (
            deepparse_handle.__class__.__name__ == "AddressParser"
        ), "deepparse_handle should be an AddressParser instance."
        self.deepparse_handle = deepparse_handle

    def tag(self, obj):
        return self.deepparse_handle(obj).to_dict()

    def batch_tag(self, objs):
        return [r.to_dict() for r in self.deepparse_handle(objs)]

