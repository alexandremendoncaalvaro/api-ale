from app.backend.interfaces.external_service_interface import IExternalService
from app.backend.models.external_services_model import ExternalServicesModel


class Project:
    def __init__(self, name: str, external_services: ExternalServicesModel) -> None:
        self.name = name
        self.external_services = external_services
        self.storage: IExternalService = self.external_services.storage
        self.sql_database: IExternalService = self.external_services.sql_database
        self.other_service: IExternalService = self.external_services.other_service
        self._create_external_services_projects()

    def _create_external_services_projects(self):
        projects_successful_created = []
        try:
            for external_service in self.external_services:
                external_service[1].create_project(self.name)
                projects_successful_created.append(external_service)
        except Exception as exception:
            self._delete_external_services_projects(
                self.name, projects_successful_created
            )
            print(exception)

    def _delete_external_services_projects(
        self, name: str, projects_to_delete: list
    ) -> None:
        for project in projects_to_delete:
            project[1].delete_project(name)

    def list_storage_containers(self) -> list:
        return self.storage.list_containers()
