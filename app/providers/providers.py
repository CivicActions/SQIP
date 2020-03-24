import abc


class ProviderInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'connect') and
                callable(subclass.connect) and
                hasattr(subclass, 'disconnect') and
                callable(subclass.disconnect) or
                NotImplemented)

    @abc.abstractmethod
    def connect(self, path: str, file_name: str):
        """Connect to resource"""
        raise NotImplementedError

    @abc.abstractmethod
    def disconnect(self, full_file_path: str):
        """Disconnect from resource"""
        raise NotImplementedError