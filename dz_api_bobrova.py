import requests
server = "https://qauto.forstudy.space/api"
endpoint = "/auth/signin"

example_value = {
  "email": "asdfghjkl@gmail.com",
  "password": "Asdfg12345",
  "remember": False
}

r = requests.post(server+endpoint, json=example_value)

print(r.json())

server_says = r.json()
if "status" in server_says:
    if server_says["status"] == "ok":
        print("all ok")
    else:
       print(server_says['message'])


import requests
server = "https://qauto.forstudy.space/api"
endpoint = "/users/current"

r = requests.get(server+endpoint, json=example_value)

print(r.json())

server_says = r.json()
if "status" in server_says:
    if server_says["status"] == "ok":
        print("all ok")
    else:
       print(server_says['message'])