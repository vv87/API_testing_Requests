import requests


r = requests.get('https://api.github.com/events')
assert r.status_code == 200, ("No search results!")
print(r.json())
