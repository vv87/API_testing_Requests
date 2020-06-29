import requests


url = 'https://api.vk.com/method/users.get?user_ids=210700286&fields=bdate&access_token=533bacf01e11f55b536a565b57531ac114461ae8736d6506a3&v=5.110'
r = requests.get(url)
assert 'error' in r.json(), ("'error' Not found")
assert r.status_code == 200

print(r.status_code, "\n", r.json())
