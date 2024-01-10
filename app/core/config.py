import tomllib
from pydantic_settings import BaseSettings

from app.domain.filepath import to_pwd_path


with open(to_pwd_path('./app/appl.toml'), mode='rb') as fp:
    appl = tomllib.load(fp)

with open(to_pwd_path('./app/env.toml'), mode='rb') as fp:
    env = tomllib.load(fp)


class AppConfig:
    """Data on application."""
    APP_NAME = appl['NAME']
    AUTHORS = appl['AUTHORS']
    DOCS_URL = '/docs'
    OPENAPI_URL = '/openapi'


class EnvConfig(BaseSettings):
    """Environment variable dataclass."""
    PORT: int = env['app']['PORT']
    # DATABASE_URL = 
    NGROK_AUTHTOKEN: str = env['ngrok']['AUTHTOKEN']
    STRAVA_CLIENT_SECRET: str = env['strava']['CLIENT_SECRET']
    STRAVA_CLIENT_ID: str = env['strava']['CLIENT_ID']
    STRAVA_REFRESH_TOKEN: str = env['strava']['REFRESH_TOKEN']
