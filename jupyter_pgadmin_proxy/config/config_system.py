import logging
from pathlib import Path

# Use visible directory so we can browse it in jupyter
data_dir = Path.home() / "pgadmin"
LOG_FILE = str(data_dir / "pgadmin4.log")
SQLITE_PATH = str(data_dir / "pgadmin4.db")
SESSION_DB_PATH = str(data_dir / "sessions")
STORAGE_DIR = str(data_dir / "storage")
DATA_DIR = str(data_dir)
SERVER_MODE = True
DEFAULT_SERVER = "127.0.0.1"
DEBUG = False
FILE_LOG_LEVEL = logging.INFO
AUTHENTICATION_SOURCES = ["webserver"]
MASTER_PASSWORD_REQUIRED = False
