import pytest
from selenium import webdriver

def test_one():
    browser = webdriver.Chrome()
    browser.get('http://www.google.com')
    assert "Google" in browser.title
    assert "Yandex" not in browser.title
    assert 'google'in browser.current_url