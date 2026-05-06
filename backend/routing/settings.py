from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    weather_endpoint: str = "https://archive-api.open-meteo.com/v1/archive"