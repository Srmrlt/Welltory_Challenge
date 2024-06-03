import logging

from pydantic import PositiveInt
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger("Settings")
logging.basicConfig(level=logging.DEBUG)


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: PositiveInt
    POSTGRES_DB_NAME: str

    @property
    def db_url(self) -> str:
        """
        Generates a database connection URL for database libraries from the given settings.
        """
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB_NAME}"
        )

    model_config = SettingsConfigDict(env_file=".env")


try:
    settings = Settings()
    logger.debug(settings.db_url)
except ValueError as e:
    logger.error(f"Configuration error: {e}")
