from unittest.mock import Mock, create_autospec

from app.backend.interfaces.external_service_interface import IExternalService
from app.backend.models.external_services_model import ExternalServicesModel
from app.backend.product_account import ProductAccount


def test_create_project_and_dependencies_with_success():
    # Mock the external services
    mock_storage = create_autospec(IExternalService)
    mock_sql_database = create_autospec(IExternalService)
    mock_other_service = create_autospec(IExternalService)

    external_services: ExternalServicesModel = ExternalServicesModel(
        storage=mock_storage,
        sql_database=mock_sql_database,
        other_service=mock_other_service,
    )

    sv_account = ProductAccount(
        name="account_test", external_services=external_services
    )

    sv_account.create_project("project_test")

    # Verify if project was created
    assert len(sv_account) == 1
    assert sv_account["project_test"].name == "project_test"

    # Verify that each service's create_project method was called
    mock_storage.create_project.assert_called_once_with("project_test")
    mock_sql_database.create_project.assert_called_once_with("project_test")
    mock_other_service.create_project.assert_called_once_with("project_test")


def test_should_delete_external_services_if_project_created_with_error():
    # Mock the external services
    mock_storage = create_autospec(IExternalService)
    mock_sql_database = create_autospec(IExternalService)
    mock_other_service = Mock(spec=IExternalService)

    # Make mock_other_service.create_project raise an exception when called
    mock_other_service.create_project.side_effect = Exception("An error occurred")

    external_services: ExternalServicesModel = ExternalServicesModel(
        storage=mock_storage,
        sql_database=mock_sql_database,
        other_service=mock_other_service,
    )

    sv_account = ProductAccount(
        name="account_test", external_services=external_services
    )

    sv_account.create_project("project_test")

    # Verify that each service's create_project method was called
    mock_storage.create_project.assert_called_once_with("project_test")
    mock_sql_database.create_project.assert_called_once_with("project_test")
    mock_other_service.create_project.assert_called_once_with("project_test")

    # Verify that storage and sql_database services' delete_project method was called
    mock_storage.delete_project.assert_called_once_with("project_test")
    mock_sql_database.delete_project.assert_called_once_with("project_test")
