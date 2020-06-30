import requests
import json
import jsonpath


# API URL
url = "https://reqres.in/api/users"
# path_to_json_file = '/var/lib/jenkins/workspace/Api_tests/GET_Request/POST_Request/create_user_data.json'
path_to_json_file = 'F:\\PythonProjects\\Requests_2\\schema.json'

# Read input json file
file = open(path_to_json_file, 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make PUT request with json input body
response = requests.put(url, request_json)

# Validation Response Code
assert response.status_code == 200, 'Response code is not "200"!'

# Parse response Content
response_json = json.loads(response.text)

# Pick id using json path
updatedAt = jsonpath.jsonpath(response_json, 'updatedAt')
print(updatedAt[0])
