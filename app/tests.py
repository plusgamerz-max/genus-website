#=============
# Test: app
#=============

import pytest

# Home Page Tests (/home)
def test_home_page_status(client):
    # Checks if the response was OK
    res = client.get('/home')
    assert res.status_code == 200

def test_home_page_template_check(client):
    # Checks if server uses the correct template for home page
    res = client.get('/home')
    assert "home.html" in [t.name for t in res.templates]

def test_home_page_content(client):
    # Checks if the home page contains the expected content
    res = client.get('/home')
    assert b"Genus Core" in res.content