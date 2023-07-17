from fastapi import FastAPI

from src.Shared.api import api_router
from src.Shared.ic import configure_ic

configure_ic()
app = FastAPI(
    title="PAWQ", description="PAWQ API", openapi_url="/openapi.json", docs_url="/"
)


app.include_router(api_router)
