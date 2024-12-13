import requests
import json


base_url = "https://nexus.bugdazz.com"
origin = "https://bugdazzstage.bugdazz.com"
host = "nexus.bugdazz.com"
auth_token ="bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvbmV4dXMuYnVnZGF6ei5jb21cL2N1c3RvbWVydjJcL2FwaVwvdjFcL2xvZ2ludmVyaWZ5IiwiaWF0IjoxNzIwNTA0MzAxLCJleHAiOjE3MjA1MzMxMDEsIm5iZiI6MTcyMDUwNDMwMSwianRpIjoicGRGcGQwVDJGUEN6MnJ0VyIsInN1YiI6IjYxMTM2NDNiN2RjZTNkMGM5NzIwMTMyYiIsInBydiI6IjhiNDIyZTZmNjU3OTMyYjhhZWJjYjFiZjFlMzU2ZGQ3NmEzNjViZjIifQ.RBaI7CHBYM-usIWQSSPp7mTg8rwBN8Y7AHGwSriv4F5EWEvryYi3e715dQ7GqdVu9EmvwvBIXVC1c7u18gffWNaBVhZC5a34Uez5E5dgWEX5cGFfLm8mTRtQrcjjk3z8OL0cCK4nffoWw4Cdzao5XiXKEUZd7kEE63w_nWkjwSpuvNJv9_I8jwY-e7k4BDkRBn3qcjuqpjYcanDUvUf24_hlDuU7ffDpDXS4SF-qLRLSzdUGvfJRloRIl3bec0q1C_r72kBklJ7cswMRoEzTR8ntTt_HImi_wUUsXqzXOvmiTi5yfBVgXp19vQ0VBRJumcGNUhdlA4sa1TMe5EFonH7UatoAEmE5IE2Lssk3YyOLmrjOJaDLLYuTlHlCppbGlRo8VdWUC-am_OTFzApE8Ykl8uv6iVTxloIPBsBiLeS3biaQ8VNzGOAF57s1a30hsJr1OhiEt8O0urHsuFX1A1izqGgVRalooyDZxxGcJlNcj6hVPJoY4dSHU0wKTAjutc6mGnDTh2WdIJy4YxktM2ellS1ML4UykwSaMJ_QNC5UR8RkZvBAKT7OpkTH9DA1qW0w_wxD_19hSa2KVNtuaC7Ogv-zjVdYTtKKDpJYh7G3R16ljncbw8XfBhiJS438sHWmSOlZgXEbi1TgWNJQr7NBhrXy9d_bpON8ghGUFd4"
def get_request():
    url = base_url+"/customerv2/api/v1/projects?page=1&perPage=10"
    headers = {"Authorization": auth_token, "origin": origin, "host": host}
    response=requests.get(url,headers=headers)
    # assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body :", json_str)

get_request()