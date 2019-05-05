import abc

class BaseStorageService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_blob_stream(self, container: str, id: str):
        raise NotImplementedError()

    def get_blob_file(self, container: str, id: str):
        raise NotImplementedError()