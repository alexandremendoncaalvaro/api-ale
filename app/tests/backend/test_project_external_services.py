from pytest import raises

from app.backend.interfaces.external_service_interface import IExternalService


class ExternalServiceWithoutImplementation(IExternalService):
    pass


def test_create_project_should_raise_exception_for_non_implementation():
    external_service = ExternalServiceWithoutImplementation()

    with raises(NotImplementedError, match="Please implement this method"):
        external_service.create_project("project_test")


def test_delete_project_should_raise_exception_for_non_implementation():
    external_service = ExternalServiceWithoutImplementation()

    with raises(NotImplementedError, match="Please implement this method"):
        external_service.delete_project("project_test")
