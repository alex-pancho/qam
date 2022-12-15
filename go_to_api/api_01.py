import requests
server = "https://qauto.forstudy.space/api"
endpoint_auth = "/auth/signin"
endpoint_users = "/users/current"
  # сервер та ендпоінт задають урл який ми тестимо
  # далі данні що ми шлемо методом пост
example_value = {
  "email": "qam2608@2022test.com",
  "password": "Qam2608venv",
  "remember": False
}
  # викликаємо метод пост і json= вказує що ми шлем як ДЖСОН
ses = requests.session()
r = ses.post(server+endpoint_auth, json=example_value)
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
get_code = ses.get(server+endpoint_users)
#get_code = gr.json()
if get_code.status_code == 200:
    print("Статус код GET-запиту: ", get_code.status_code)
    print("Результат GET-запиту: ", get_code.json())
else:
    print("Потрібна авторизація: ", get_code.json())
