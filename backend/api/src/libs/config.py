from src.libs.custom_exceptions import ConfigError
import configparser
import sys, os

class Config:
    def __init__(self, MODE: str = "DEV"):
        self.__config = configparser.ConfigParser()
        if MODE == "DEV":
            sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
            path = sys.path[-1] + "/config/config.dev.ini"
        elif MODE == "PROD":
            path = "/api/src/config/config.prod.ini"
        self.__config.read(path)
        if self.__config.get("DATABASE", "PG_USER") is None:
            raise ConfigError("PG_USER is not set")
        self.POSTGRES_USER = self.__config.get("DATABASE", "PG_USER")
        if self.__config.get("DATABASE", "PG_PASS") is None:
            raise ConfigError("PG_PASSWORD is not set")
        self.POSTGRES_PASS = self.__config.get("DATABASE", "PG_PASS")
        if self.__config.get("DATABASE", "PG_HOST") is None:
            raise ConfigError("PG_HOST is not set")
        self.POSTGRES_HOST = self.__config.get("DATABASE", "PG_HOST")
        if self.__config.get("DATABASE", "PG_PORT") is None:
            self.POSTGRES_PORT = 5432
        self.POSTGRES_PORT = self.__config.getint("DATABASE", "PG_PORT")
        if self.__config.get("DATABASE", "PG_DATABASE") is None:
            raise ConfigError("PG_DATABASE is not set")
        self.POSTGRES_DB = self.__config.get("DATABASE", "PG_DATABASE")
        if self.__config.get("SECRET", "SECRET_AUTH") is None:
            raise ConfigError("SECRET_AUTH is not set")
        self.SECRET_AUTH = self.__config.get("SECRET", "SECRET_AUTH")
        if self.__config.get("REDIS", "REDIS_HOST") is None:
            raise ConfigError("REDIS_HOST is not set")
        self.REDIS_HOST = self.__config.get("REDIS", "REDIS_HOST")
        self.SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASS}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"