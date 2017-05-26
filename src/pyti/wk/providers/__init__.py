import abc


class BaseDataProvider(abc.ABC):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def all(self):
        pass

    @abc.abstractmethod
    def new(self, **kwargs):
        pass


class DbDataProvider(BaseDataProvider):
    def __init__(self, **kwargs):
        pass

    def new(self, **kwargs):
        pass

    def all(self):
        pass

    def get(self, key):
        pass
