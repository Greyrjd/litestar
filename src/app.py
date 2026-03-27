from attrs import define, validators, field
from typing import Union, Dict, List, Any
from litestar import Router, get

JSONType = Union[Dict[str, Any], List[Any], str, int, float, bool, None]

@define
class Version:
    id: int = field(
        validator=[
            validators.instance_of(int),
            validators.ge(1),
            validators.lt(10),
        ],
    )
    specs: JSONType = field(default=None)

VERSION = {
    1: Version(
        id=1,
        specs={
            "some": "value"
        }
    ),
    2: Version(
        id=2,
        specs={
            "some": "named value"
        }
    ),
}

@get(path="/{version_id:int}")
async def get_product_version(
        version_id: int
) -> Version:
    return VERSION[version_id]

product_version_router = Router(
    path="/versions",
    route_handlers=[get_product_version],
)