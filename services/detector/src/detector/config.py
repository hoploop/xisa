
from pydantic import Field
from common.service import ClientConfig, ServiceConfig
from common.utils.mongodb import MongodbConfig


class DetectorServiceConfig(ServiceConfig):
    database: MongodbConfig
    path: str = Field(description="Relative path where all detectors are stored")
    original: str = Field(description="Original basic yolo weights .pt file reference")
    name: str = Field(description="Default name of .pt new detector weights file")
    data: str = Field(
        description="Default name of .yaml configuration file for new detector"
    )
    runs: str = Field(description="Name of the folder where runs are stored")
    classes: str = Field(description="Name of .yaml file used for storing the classes")
    recorder: ClientConfig
    api: ClientConfig
    trainer: ClientConfig
    auth: ClientConfig
    storage: ClientConfig
