from app.backend.interfaces.storage_api_interface import IStorageApi


class StorageApi(IStorageApi):
    def __init__(self):
        pass

    def list_containers(self) -> list[str]:
        """
        Lista os containers do Storage.

        Returns:
            list[str]: Uma lista com os containers do Storage.

        Examples:
            >>> storage_api = StorageApi()
            >>> storage_api.list_containers()
            ['test1', 'test2']
        """
        return ["test1", "test2"]
