from abc import abstractmethod


class Preprocessor:
    def __call__(self, sentence):
        return self.process(sentence)

    @abstractmethod
    def process(self, sentence):
        pass

    def batch_process(self, sentences):
        return [self.process(sentence) for sentence in sentences]
