import requests
server = "https://qauto.forstudy.space/api"
signin = "/auth/signin"
users_cur = "/users/current"
# сервер та ендпоінт задають урл який ми тестимо
# далі данні що ми шлемо методом пост
example_value = {
  "email": "qam2608@2022test.com",
  "password": "Qam2608venv",
  "remember": False
}

s = requests.session()
# викликаємо метод пост і json= вказує що ми шлем як ДЖСОН
r = s.post(server+signin, json=example_value)
# сервер присилає нм теж ДЖСОН що ми перетворюємол в словник і записуєм у зм. 
server_says = r.json()
# використовуємо методи словника
#  Якщо ключ "status" у словнику то
if "status" in server_says:
    #  Якщо значення клюса статус == ок
    if server_says["status"] == "ok":
        print("all ok")
    #  інакше
    else:
        print(server_says['message'])
print("="*88)
r2 = s.get(server+users_cur)
print(r2.status_code)
print(r2.json())