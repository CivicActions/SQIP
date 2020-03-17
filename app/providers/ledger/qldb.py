from app.providers.providers import ProviderInterface


@ProviderInterface.register
class QLDBProvider:
    def connect(self, path: str, file_name: str):
        """Connect to resource"""
        raise NotImplementedError

    def disconnect(self, full_file_path: str):
        """Disconnect from resource"""
        raise NotImplementedError
