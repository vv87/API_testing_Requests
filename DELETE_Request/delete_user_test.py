import requests

# Api URL
url = "https://reqres.in/api/users/2"
response = requests.delete(url)


def delete_user_test():
    # Fetch response
    print(response.status_code)
    assert response.status_code == 204, 'Response code is not "204"!'
