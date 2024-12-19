import requests
import json
def add_usesr(data):
    url = "https://d80c-240c-c001-1008-294a-3d66-a878-8091-67e5.ngrok-free.app/user"
    #data = { "user_name": "John", "password": "password123", "tel": "123456789", "score": 95.5 }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("User added successfully!")
    else:
        print(f"Failed to add user. Status code: {response.status_code}")
def get_usesr(user_id):
    url = "https://d80c-240c-c001-1008-294a-3d66-a878-8091-67e5.ngrok-free.app/user"
    id_ = {'user_id': user_id}
    response = requests.get(url, params = id_)

    if response.status_code == 200:
        user_data = response.json()
        #print("User found:", user_data)
        return user_data

    else:
        print(f"Failed to retrieve user. Status code: {response.status_code}")
        return False, '账户不存在'
get_usesr("1")
