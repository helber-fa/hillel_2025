import os

def is_dev():
    return os.getenv("CURRENT_ENV", "PROD") == "DEV"