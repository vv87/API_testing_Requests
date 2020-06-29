import requests
import json
import jsonpath


# API URL
url = "https://reqres.in/api/users?page=2"

# Send Get Request
response = requests.get(url)

# Parse response to Json format
json_response = json.loads(response.text)
# print(json_response)

# Fetch value using Json Path
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])

assert pages[0] == 2, 'Wrong Value'