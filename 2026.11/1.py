# %%
import requests

url = "https://httpbin.org/post"

headers = {
    "User-Agent": "my-python-client/1.0",
    "X-Student-Name": "xiaoming",
}

data = {"name": "小明", "score": 95}

try:
    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=10
    )
    response.raise_for_status()

    result = response.json()
    print(result["headers"])

except requests.exceptions.RequestException as e:
    print("请求失败", e)
# %%
import requests

url = "https://httpbin.org/post"

headers = {
    "User-Agent": "spring/1.0",
    "X-Exercise": "spring"
}
data = {
    "name": "小明",
    "day": 14
}
try:
    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=10
    )
    response.raise_for_status()
    result = response.json()
    print(result["json"]["name"])
    print(result["headers"]["User-Agent"])
except requests.exceptions.RequestException as e:
    print("请求失败",e)
# %%
