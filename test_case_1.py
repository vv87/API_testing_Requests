import requests


r = requests.get('https://api.github.com')

assert r.status_code == 200, ("No search results!")
assert 'current_user_url' in r.json()

print(r.json())
