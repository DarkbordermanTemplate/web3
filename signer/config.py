import os


class Config:
    ACCOUNT = os.environ.get("ACCOUNT", "")
    PASSWORD = os.environ.get("PASSWORD", "")
    PROVIDER = os.environ.get("PROVIDER", "")


CONFIG = Config()
