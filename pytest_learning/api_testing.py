import requests
import random
import json
from python_practise import string

#base url
base_url = "https://nexus.bugdazz.com"


#auth_token
auth_token= "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL25leHVzLmJ1Z2RhenouY29tL2N1c3RvbWVyL2FwaS92MS9zaWduaW4iLCJpYXQiOjE2OTMxMDI4NzYsImV4cCI6MTY5MzEzMTY3NiwibmJmIjoxNjkzMTAyODc2LCJqdGkiOiJLSDFxUUFmSVZqWDBtT09pIiwic3ViIjoiNjI4MzQzYmJhMTUzNmY3NTAyMTRmYmY3IiwicHJ2IjoiOGI0MjJlNmY2NTc5MzJiOGFlYmNiMWJmMWUzNTZkZDc2YTM2NWJmMiJ9.aY2OnNAJgIn0-5H2qsLfrZ3paBGmcIfFCh8BAvyU030"
origin = "https://bugdazzstage.bugdazz.com"
host = "nexus.bugdazz.com"
# get random email id
def generate_email_id():
    domain = "automation.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

#Get Request

def get_request():
    url = base_url + "/customer/api/v1/programcount?filter=all"
    headers = {"Authorization" : auth_token,"origin" : origin, "host" : host}
    response = requests.get(url,headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data,indent=4)
    print("json response body :", json_str)

#post Request
def Post_Request():
    url = base_url+""
    print("post url : ", url)
    headers = {"Authorization" : auth_token}
    data = {
        "name" : "Rohini Hirekhan",
        "email" : generate_email_id(),
        "gender" : "female",
        "status" : "active"
    }
    response = requests.post(url,json=data,headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body:",json_str)
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "Rohini Hirekhan"
    return user_id

# PUT Request
def Put_Request(user_id):
    url = base_url+f"/public/v2/users/{user_id}"
    print("put url : ", url)
    headers = {"Authorization" : auth_token}
    data = {
        "name" : "Rohini Malakwade",
        "email" : generate_email_id(),
        "gender" : "female",
        "status" : "active"
    }
    response = requests.put(url,json=data,headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json PUT response body:", json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "Rohini Malakwade"

# Delete Call
def Delete_Request(user_id):
    url = base_url+f"/public/v2/users/{user_id}"
    print("delete url : ", url)
    headers = {"Authorization" : auth_token}
    response = requests.delete(url,headers=headers)
    assert response.status_code == 204
    print("delete user is done............")

# call
get_request()
user_id = Post_Request()
Put_Request(user_id)
Delete_Request(user_id)











