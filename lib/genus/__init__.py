#============================
# Initializing Genus Core
#============================

# Importing Libraries
from os import getenv

# Get all necessary environment variables

# Loading API Key
api_key = getenv("GEMINI_API_KEY", None)
if not api_key:
    raise ValueError("Gemini API Key is not set in the environment variables.")