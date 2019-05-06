import abc

class BaseImageProcessor(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def threshold_and_invert(self, path: str):
        raise NotImplementedError