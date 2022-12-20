import pytest
from roasts_and_recipies import create_app


def test_project_init():
    from selenium import webdriver

    browser = webdriver.Firefox()
    browser.get("http://localhost:5000")

    assert "Hello, index!" in browser.page_source

    browser.quit()
