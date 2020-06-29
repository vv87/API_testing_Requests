import requests
import json

if __name__ == '__main__':
    # API URL
    url = "https://reqres.in/api/users"
    # Read input json file
    file = open('F:\\PythonProjects\\Requests_2\\DELETE_Request\\create_user_data.json', 'r')
    json_input = file.read()
    REQUEST_JSON = json.loads(json_input)
    # print(request_json)

    # Make POST request with json input body
    def response_create_user():
        response = requests.post(url, REQUEST_JSON)
        print(response.content)
        assert response.status_code == 201, 'Response code is not "201"!'


response_create_user()






