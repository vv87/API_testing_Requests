import requests

# API URL
not_valid_url = 'https://www.youtube.com/qxje'

# Send not_valid_url to get request
response = requests.get(not_valid_url)

# # Display response content
# print(response.content)
#
# # Display response headers
# print(response.headers)
#
# # Display response status code
# print(response.status_code)


def get_valid_request_test():
    # If status code not equal 200, print actual status code
    if response.status_code != 200:
        print(response.status_code)
    assert response.status_code == 404, 'Response code is not "404"!'
