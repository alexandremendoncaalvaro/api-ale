import abc


class IExternalService:
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def create_project(self, name: str) -> None:
        raise NotImplementedError("Please implement this method")

    @abc.abstractmethod
    def delete_project(self, name: str) -> None:
        raise NotImplementedError("Please implement this method")
