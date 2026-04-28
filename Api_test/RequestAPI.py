import requests

#base url:
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())

#Filtering the data
params = {"userId": 2}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params)
print(response.json())

# POST
data = {"title": "Hello", "body": "World", "userId": 101}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json= data)
print(response.status_code)
print(response.json())

headers = {
    "Authorization" : "Bearer skjdksdjsid888232@Tdaada",
    "Content-Type" : "application/json"
}

try:
    response = requests.post("https://rathanky.com", timeout = 10 )
    print(response)
except requests.exceptions.RequestException as e:
    print("Error ", e)
