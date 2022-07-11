from typing import TypeVar, Generic, Optional, Dict, List

from pydantic import BaseModel, root_validator
from pydantic.generics import GenericModel

from pylkapi.exception import PyLKApiException


class BasicSubResponseModel(BaseModel):
    ...


SubModelT = TypeVar("SubModelT", bound=BasicSubResponseModel)


class BasicResponse(GenericModel, Generic[SubModelT]):
    code: int
    t: int
    data: Optional[SubModelT]

    @root_validator
    def check_exception(cls, values: dict):
        code = values.get("code")
        if code != 0:
            raise PyLKApiException(code)
        return values


class SimplePageInfo(BaseModel):
    count: int
    cur: int
    prev: Optional[int]
    next: Optional[int]
    has_prev: Optional[int]
    has_next: Optional[int]

    @root_validator
    def automatic_inference(cls, values: Dict[str, int]):
        if not values.get("prev"):
            prev = 1 if values.get("cur") == 1 else values.get("cur") - 1
            values.update({"prev": prev})
        if not values.get("next"):
            next = values.get("count") if values.get("cur") == values.get("count") else values.get("cur") + 1
            values.update({"next": next})
        if not values.get("has_prev"):
            has_prev = 1 if values.get("cur") != 1 else 0
            values.update({"has_prev": has_prev})
        if not values.get("has_next"):
            has_next = 1 if values.get("cur") != values.get("count") else 0
            values.update({"has_next": has_next})
        return values


class PageInfo(BaseModel):
    count: int
    size: int
    cur: int
    prev: int
    next: int
    has_prev: int
    has_next: int
    model: int
    support_model: List[int]
