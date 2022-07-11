from enum import Enum, IntEnum
from typing import TypeVar, Generic, Literal

from pydantic import BaseModel
from pydantic.generics import GenericModel


class _Platform(str, Enum):
    android = "android"
    pc = "pc"


class _Client(str, Enum):
    web = "web"
    app = "app"


class _Gz(IntEnum):
    Enable = 1
    Disable = 0


class _IsEncrypted(IntEnum):
    true = 1
    false = 0


class BasicSubBodyModel(BaseModel):
    class Config:
        allow_population_by_field_name = True


SubModelT = TypeVar('SubModelT', bound=BasicSubBodyModel)


class BasicBody(GenericModel, Generic[SubModelT]):
    platform: Literal["android", "pc"] = _Platform.android
    client: Literal["web", "app"] = _Client.web
    sign: str = ""
    ver_name: str = "0.11.50"
    ver_code: int = 190
    gz: Literal[0, 1] = _Gz.Disable
    is_encrypted: Literal[0, 1] = _IsEncrypted.false
    d: SubModelT
