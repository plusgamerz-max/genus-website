# Initializing
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

from colorama import init as colorama_init
colorama_init()

import uvicorn

# Load environment variables and getting db url
from os import environ
from dotenv import load_dotenv
load_dotenv()
host = environ.get('HOST', "0.0.0.0")
port = int(environ.get('PORT', 80))

# Running Server
if __name__ == "__main__":
    uvicorn.run(
        "web.asgi:app",
        reload=True,
        host=host,
        access_log=True,
        port=port,
    )
    