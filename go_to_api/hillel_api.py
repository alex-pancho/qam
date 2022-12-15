import requests
base_api_url = "https://qauto.forstudy.space/api"
s = requests.session()

def auth_signin(s:requests.session, request_body:dict):
    signin = "/auth/signin"
    return s.post(base_api_url+signin, json=request_body)

def users_curr(s:requests.session):
    users_current = "/users/current"
    return s.get(base_api_url+users_current)

def after_processsing(r):
    try:
        return r.json()
    except Exception as e:
        return {}
