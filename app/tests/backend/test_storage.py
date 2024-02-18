from unittest.mock import create_autospec

from app.backend.interfaces.external_service_interface import IExternalService
from app.backend.models.external_services_model import ExternalServicesModel
from app.backend.product_account import ProductAccount
from app.backend.storage import Storage


def test_should_list_containers():
    product_account = ProductAccount(
        name="account_test",
        external_services=ExternalServicesModel(
            storage=Storage(),
            sql_database=create_autospec(IExternalService),
            other_service=create_autospec(IExternalService),
        ),
    )
    product_account.create_project(name="project_test")
    containers = product_account["project_test"].list_storage_containers()
    assert len(containers) > 0
    assert containers == ["test1", "test2"]
