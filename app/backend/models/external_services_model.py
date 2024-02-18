from pydantic import BaseModel

from app.backend.interfaces.external_service_interface import IExternalService


class ExternalServicesModel(BaseModel):
    storage: IExternalService
    sql_database: IExternalService
    other_service: IExternalService

    class Config:
        arbitrary_types_allowed = True
