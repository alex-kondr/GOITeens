from typing import Dict

import requests


# response = requests.get("https://api.agify.io/", params=dict(name="Alex"))
# if response.status_code == 200:
#     response = response.json()
#     print(f"Name: {response.get('name')}\nCount: {response.get('count')}\nAge: {response.get('age')}")
# else:
#     print("no site")

def get_data(url: str) -> Dict[str, str]:
    json_data = dict(
        name="Олександр",
        email="super@gmail.com",
        message="Привіт мій друже!!!"
    )
    resp = requests.post(url, json=json_data)
    return resp.json()


data = get_data("https://jsonplaceholder.typicode.com/posts")
print(f"{data = }")
