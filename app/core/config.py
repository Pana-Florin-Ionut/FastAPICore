from pydantic_settings import BaseSettings
import os

from dotenv import load_dotenv

load_dotenv()

# Build the path to the password.txt file


def dbPass():
    with open("db/password.txt") as pws:
        password = pws.read()
        return password


password = dbPass()
user = os.getenv("POSTGRES_USER")
port = os.getenv("PORT")
host = os.getenv("HOST")
database = os.getenv("DATABASE")


class Settings(BaseSettings):
    # Database connection details
    DATABASE_URL: str = f"postgresql://{user}:{password}@{host}:{port}/{database}"

    # print(f"DATABASE_URL: {DATABASE_URL}")

    # Secret keys for hashing and tokens
    # ALGORITHM: str = os.getenv("ALGORITHM")
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

    # Other application settings


settings = Settings()
