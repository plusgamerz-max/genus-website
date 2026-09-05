#===========================
# Initializing Genus App
#===========================

# Importing libraries
import os

# Loading variables from .env
from dotenv import load_dotenv
load_dotenv()

# Initializing colorama
from colorama import init as colorama_init
colorama_init()

# Checking if required variables are available
REQUIRED_ENV_VARS = ["DJANGO_SETTINGS_MODULE", "DB1_URL", "GEMINI_API_KEY"]

missing = [var for var in REQUIRED_ENV_VARS if not os.environ.get(var)]
if missing:
    raise RuntimeError(f"Missing required environment variables: {', '.join(missing)}")