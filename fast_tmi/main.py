from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fast_tmi.api.routes.api import router as api_router


def get_application():
    application = FastAPI(
        docs_url="/docs",
        openapi_url="/openapi.json",
    )

    application.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(api_router)
    return application


app = get_application()
