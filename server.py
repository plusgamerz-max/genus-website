#=======================
# Server Manager Tool
#=======================

# Initializing
import init as _
import uvicorn

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')


# Getting port and host
from os import environ
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