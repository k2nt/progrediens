import logging

import uvicorn
from ngrok import ngrok
from fastapi import FastAPI

from app.api.router import router
from app.core.config import AppConfig, EnvConfig


app_config = AppConfig()
env_config = EnvConfig()


def start_ingress():
    addr = f"{env_config.HOST}:{env_config.PORT}"
    listener = ngrok.forward(addr, authtoken=env_config.NGROK_AUTHTOKEN)
    print(f"Ingress established at: {listener.url()}")


def asgi_app_factory() -> FastAPI:
    app = FastAPI(
        title=app_config.APP_NAME,
        docs_url=app_config.DOCS_URL,
        openapi_url=app_config.OPENAPI_URL
        )

    app.include_router(router)

    return app


def start():
    """Launch application."""
    # Start reverse proxy to connect localhost application to world wide web
    start_ingress()

    # Start application
    uvicorn.run(
        app=asgi_app_factory(),
        port=env_config.PORT
        )


if __name__ == '__main__':
    start()
    