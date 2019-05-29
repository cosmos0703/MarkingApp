import abc

class BaseImageProcessor(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def extract_questions(self, dir: str, file: str):
        raise NotImplementedError