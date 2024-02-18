from app.backend.external_services.storage_api import StorageApi
from app.backend.interfaces.external_service_interface import IExternalService
from app.backend.interfaces.storage_api_interface import IStorageApi


class Storage(IExternalService):
    def __init__(self, service_api: IStorageApi = None):
        self.service_api = service_api or StorageApi()

    def create_project(self, name: str) -> None:
        pass

    def delete_project(self, name: str) -> None:
        pass

    def list_containers(self) -> list:
        """
        Lista os containers do serviço de API de Storage.

        Returns:
            list: Uma lista com os containers do serviço de API de Storage.

        Examples:
            >>> storage = Storage()
            >>> storage.list_containers()
            ['test1', 'test2']
        """
        return self.service_api.list_containers()
