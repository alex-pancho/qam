import hillel_api
import pytest

def test_01_sigin_positive():
    s = hillel_api.s
    user_data = {
    "email": "qam2608@2022test.com",
    "password": "Qam2608venv",
    "remember": False
    }
    r = hillel_api.auth_signin(s, user_data)
    r_json = hillel_api.after_processsing(r)    
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"

def test_02_sigin_negative():
    s = hillel_api.s
    user_data = {
    "email": "qam@2022test.com",
    "password": "Qam2",
    "remember": False
    }
    r = hillel_api.auth_signin(s, user_data)
    r_json = hillel_api.after_processsing(r)
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not error"

