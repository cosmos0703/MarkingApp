import abc

class BaseStorageService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_file(container: str, id: str):
        raise NotImplementedError()