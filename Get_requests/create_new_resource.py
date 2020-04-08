import requests 


url = "https://reqres.in/api/users"

data = {"name":"sundar","job":"software-engineer"}

response = requests.post(url,data)
print(response.status_code)
print(response.content)
