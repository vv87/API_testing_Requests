import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"
path_to_json_file = '/var/lib/jenkins/workspace/Api_tests/GET_Request/POST_Request/create_user_data.json'
# path_to_json_file = 'F:\\PythonProjects\\Requests_2\\schema.json'


def parse_id_from_json_test():
    # Read input json file
    file = open(path_to_json_file, 'r')
    json_input = file.read()
    request_json = json.loads(json_input)

    # Make POST request with json input body
    response = requests.post(url, request_json)

    assert response.status_code == 201, 'Response code is not "201"!'

    # Parse Content-Length from response header
    print(response, '\nContent-Length:', response.headers.get('Content-Length'))

    # Parse response to json format
    response_json = json.loads(response.text)

    # Pick id using json path
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])
