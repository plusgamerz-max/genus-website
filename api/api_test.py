#=============
# Test: api
#=============

from fastapi.testclient import TestClient
from api.main import app

# Test Client
client = TestClient(app)

# Welcome API tests (/welcome)
def test_welcome_api_status():
    # Checks if the response was OK
    res = client.get("/welcome")
    assert res.status_code == 200

def test_welcome_api_content():
    # Checks if the welcome API returns the expected content
    res = client.get("/welcome")
    assert res.json() == {"message": "Welcome to the Genus API!"} 