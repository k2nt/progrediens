import uvicorn
from fastapi import FastAPI

from app.api.router import router
from app.core.config import AppConfig, EnvConfig


app_config = AppConfig()
env_config = EnvConfig()


def start_ingress():
    pass


def asgi_app_factory() -> FastAPI:
    app = FastAPI(
        title=app_config.APP_NAME,
        docs_url=app_config.DOCS_URL,
        openapi_url=app_config.OPENAPI_URL
        )

    app.include_router(router)

    return app


def start():
    # Start reverse proxy to connect localhost application to world wide web
    start_ingress()

    # Start application
    uvicorn.run(
        app=asgi_app_factory(),
        port=env_config.PORT
        )


if __name__ == '__main__':
    start()
    