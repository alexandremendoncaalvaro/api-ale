from typing import Dict

from app.backend.interfaces.external_service_interface import IExternalService
from app.backend.models.external_services_model import ExternalServicesModel
from app.backend.project import Project


class ProductAccount:
    def __init__(self, name: str, external_services: ExternalServicesModel) -> None:
        """
        Cria uma nova instância da classe ProductAccount.

        Args:
            name: Nome da Conta no Produto.
            external_services: Instância da classe ExternalServicesModel para a injeção das dependências.

        Returns:
            None

        Examples:
            >>> class GenericServiceExample(IExternalService):
            ...     def create_project(self, name: str) -> None:
            ...         pass
            >>> external_services: ExternalServicesModel = ExternalServicesModel(
            ...     storage=GenericServiceExample(),
            ...     sql_database=GenericServiceExample(),
            ...     other_service=GenericServiceExample()
            ... )
            >>> sv_account = ProductAccount("account_test", external_services)
        """
        self.name = name
        self.external_services: ExternalServicesModel = external_services
        self.storage: IExternalService = self.external_services.storage
        self.sql_database: IExternalService = self.external_services.sql_database
        self.other_service: IExternalService = self.external_services.other_service
        self.projects: Dict[str, Project] = {}

    def __len__(self) -> int:
        return len(self.projects)

    def __getitem__(self, name: str) -> Project:
        return self.projects[name]

    def create_project(self, name: str) -> None:
        """
        Cria um novo projeto.

        Args:
            name: Nome do projeto.

        Returns:
            None

        Examples:
            >>> class GenericServiceExample(IExternalService):
            ...     def create_project(self, name: str) -> None:
            ...         pass
            >>> external_services: ExternalServicesModel = ExternalServicesModel(
            ...     storage=GenericServiceExample(),
            ...     sql_database=GenericServiceExample(),
            ...     other_service=GenericServiceExample()
            ... )
            >>> sv_account = ProductAccount("account_test", external_services)
            >>> sv_account.create_project("project_test")
        """
        self.projects[name] = Project(name, self.external_services)
