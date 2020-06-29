import requests

url = 'https://api.github.com'
r = requests.get(url)

assert r.status_code == 200, ("Response code is not 200")
assert 'current_user_url' in r.json()

print(r.status_code, '\n', r.json())
