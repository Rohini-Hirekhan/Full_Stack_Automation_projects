import requests
import json

base_url = "http://localhost:9090/"
host = "localhost:9090"
auth_token = "bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzZWN1cmVMYXllcjciLCJleHAiOjE3MjQ0MjQ1MDUsImlzcyI6InRydXN0ZWQiLCJuYW1lIjoiNDg3Nzg3MzYtYzU0NS00ZTcwLTgzMDQtN2M0YmExYmZiMTJlIiwic3ViIjoic2NhbiJ9.Gm-_N8GEwXZpx7Yd0I-iBfmNrV0GjiPgtIy9tuti7EsXIl08pJNZWOD_qgH7wE6J7AKk3ccOtwDMhk8U6BQ_WYm0hPJ7litfYcxfU7k_m3bXAV2f3uVj7zPKmbDlljgar9ZN-or7QLi4DRKbmL46ZF7dXb0DcegOCbOKCTx_VT6NLUILB_hnPetiI4wPgI35eeN8R0Fv1jPUNMeV8C-BJvpvGl89DYyDN0HAhSnJIgkJC1A7t5rmYd7DMvqaNBkg9vqEUteUpEnZPanmpRVmUY5YQOxJOlUJjx7zxCX1uo4BwbAsW-u7_O0hsiU8YmQDOcqmoARdMJF5I1NPyzQtQ81igYbOAcF15rERrWCgCLbMJk9QyJgGF_mFoXp1zei_Xq8Hw6KgNBvJa8OnVSTWnncXojfJfTP5CMmqNedWOEzMM_-c6ierEXat6jI8vbJ-QtbDOqfPP5Ov9RNafZPTTqSJBMOhPSLwsGfRiptxjpWvst7BHOzBQwI9c6DXamYmPE5sW362J0TcY2OluZkIq2m1oS_14XtBdmaGI16-ak9DMrHyhV2oFxolAXI5tjmwBwPtBxsq8kuOVA--VXq_qmHZLnXDmCD8TBE241ZpYVNErobemmpR7ITvgnJhDQvAFVBjMsGa31ILz9vNpvz1egBH9cWfTviFQi59metEFCA"
def get_request():
    url=base_url+"v1/collectionNames"
    headers ={"Authorization":auth_token,"host":host}
    response = requests.get(url,headers)
    print("hi")
    # assert response.status_code == 200
    print("hello")
    json_data = response.json()
    print(json_data)

get_request()
