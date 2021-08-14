from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).parent.parent
DOTENV_PATH = BASE_DIR / ".env"
COGS_PATH = "listener/cogs"
SETTINGS_PATH = BASE_DIR / "settings"
SETTINGS_PATH.mkdir(exist_ok=True)