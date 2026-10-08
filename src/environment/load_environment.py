from dotenv import dotenv_values
import os

# Loading environment values


def load_environment() -> dict:
    environment = os.getenv("ENVIRONMENT")
    env_file = f".env.{environment}"
    return dotenv_values(env_file)
