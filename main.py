from litestar import Litestar

from src.app import product_version_router

app = Litestar(route_handlers=[product_version_router])