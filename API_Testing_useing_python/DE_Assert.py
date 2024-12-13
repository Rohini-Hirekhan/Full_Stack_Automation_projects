import requests

# response = requests.get("https://clientdev.authsafe.ai/api/recent-user-activites/768927aa-d5f6-469c-a7cf-4653c72658c0/bc6ce4e58c6b459c9c7248159bac9e1a/?user=vIGu0GFBvv7DF4MaaaG2BA&limit=25")
response1 = requests.get("https://clientdev.authsafe.ai/api/user-locations/768927aa-d5f6-469c-a7cf-4653c72658c0/d046fa84856f4d84a7c1a43420171ebd/?user=vOLnJMFZZOGsf4DzbkbVGA")
# print(response)
print(response1)
json_data = response1.json()
print(json_data)
# print(response['data'][1][0]['events'][""])
# events = response['data'][1][0]['events'] == "Invalid email detected"
# assert  response.status_code == 201