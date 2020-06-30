import requests
import json

# API URL
url = "https://reqres.in/api/users"
path_to_json_file = '/var/lib/jenkins/workspace/Api_tests/GET_Request/POST_Request/create_user_data.json'
# path_to_json_file = 'F:\\PythonProjects\\Requests_2\\schema.json'

# Read input json file
file = open(path_to_json_file, 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make POST request with json input body
response_create_user = requests.post(url, request_json)
print(response_create_user)

# validating response code
assert response_create_user.status_code == 201, 'Response code is not "201"!'
