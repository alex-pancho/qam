import requests
server = "https://qauto.forstudy.space/api"
endpoint = "/auth/signin"
ed_2 = "/users/current"

example_value = {
  "email": "test2099@test.com",
  "password": "Qwerty12345",
  "remember": True
}
s = requests.session()

r = s.post(server+endpoint, json=example_value)

server_says = r.json()

if "status" in server_says:
    if server_says["status"] == "ok":
        print("all ok")
    else:
        print(server_says['message'])

 #task 2
r2 = s.get(server+ed_2)
print(r2.status_code)
print(r2.json())

