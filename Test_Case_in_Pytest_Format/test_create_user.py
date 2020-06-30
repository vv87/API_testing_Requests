import requests
import json
import jsonpath
import pytest

# API URL
url = "https://reqres.in/api/users"


@pytest.mark.regression
def test_create_new_user():
    path_to_json_file = '/var/lib/jenkins/workspace/Api_tests/GET_Request/POST_Request/create_user_data.json'
    # path_to_json_file = 'F:\\PythonProjects\\Requests_2\\POST_Request\\create_user_data.json'
    file = open(path_to_json_file, 'r')
    json_input = file.read()  # Read input json file
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)  # Make POST request with json input body
    assert response.status_code == 201, 'Response code is not "201"!'


@pytest.mark.regression
def test_create_other_user():
    path_to_json_file = '/var/lib/jenkins/workspace/Api_tests/GET_Request/POST_Request/create_user_data.json'
    # path_to_json_file = 'F:\\PythonProjects\\Requests_2\\POST_Request\\create_user_data.json'
    file = open(path_to_json_file, 'r')
    json_input = file.read()  # Read input json file
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)  # Make POST request with json input body
    response_json = json.loads(response.text)  # Parse response to json format
    id = jsonpath.jsonpath(response_json, 'id')  # Pick id using json path
    print(id[0])


@pytest.mark.smoke
@pytest.mark.regression
def test_create_new_user2():
    path_to_json_file = '/var/lib/jenkins/workspace/Api_tests/GET_Request/POST_Request/create_user_data.json'
    # path_to_json_file = 'F:\\PythonProjects\\Requests_2\\POST_Request\\create_user_data.json'
    file = open(path_to_json_file, 'r')
    json_input = file.read()  # Read input json file
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)  # Make POST request with json input body
    assert response.status_code == 201, 'Response code is not "201"!'


@pytest.mark.smoke
def test_create_other_user2():
    path_to_json_file = '/var/lib/jenkins/workspace/Api_tests/GET_Request/POST_Request/create_user_data.json'
    # path_to_json_file = 'F:\\PythonProjects\\Requests_2\\POST_Request\\create_user_data.json'
    file = open(path_to_json_file, 'r')
    json_input = file.read()  # Read input json file
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)  # Make POST request with json input body
    response_json = json.loads(response.text)  # Parse response to json format
    id = jsonpath.jsonpath(response_json, 'id')  # Pick id using json path
    print(id[0])
