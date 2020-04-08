import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users?page=2"

#Send Get Request 
response = requests.get(url)

#Display response content
#print(response)
#print(response.content)
#print(response.headers)

#Validate status code 
print(response.status_code)
print(response.headers.get('Date'))
print(response.cookies)

#Fetch elapsed time :
print(response.elapsed)
assert response.status_code == 200

#parse response to json format. 
json_response = json.loads(response.text)
#print(json_response)
pages = jsonpath.jsonpath(json_response,'total_pages')
for i in range(0,3):   
    data  = jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
    print(data[0])
#print(pages)
