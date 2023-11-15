from api.client import Client

username = "..."
password = "L1ll14nUS4"

client = Client()
print(client.go_home().text)
print(client.go_login().text)
print(client.login(username, password))