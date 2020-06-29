import requests


# API URL
VALID_URL = "https://reqres.in/api/users?page=2"

# Send not_valid_url to get request
response = requests.get(VALID_URL)

# If status code not equal 200, print actual status code
if response.status_code != 200:
    print(response.status_code)
else:
    print(response.status_code)

# check: status_code equal 200
assert response.status_code == 200, 'Response code is not "200"!'
