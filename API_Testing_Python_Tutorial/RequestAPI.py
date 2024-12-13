import requests
import random
import json
import string

#base url
base_url="https://gorest.co.in/"

#Auth token
auth_token = "Bearer e000546f16aeff7b53a8b2f82af66a595b8fb345eba59668df5c048bce0690ca"

#Get Request
def get_request():
    url = base_url + "/public/v2/user"
    headers = {"Authorization" : auth_token}
    response = requests.get(url, headers=headers)
    # assert response.status_code == 200
    json_data = response.json()
    print("json response body :", json_data)




#call
get_request()