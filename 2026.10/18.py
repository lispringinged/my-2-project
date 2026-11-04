import requests
params = {
    "name": "小明",
    "age": 18
}
try:
    response = requests.get(
        "https://httpbin.org/get",
        params = params,
        timeout = 10
    )
    response.raise_for_status()
    data = response.json()
    print("姓名：", data["args"]["name"])
    print("年龄：", data["args"]["age"])
except requests.exceptions.RequestException as e:
    print("请求失败", e)
# %%
import requests
student = {
    "name": "小明",
    "score": 95
}
try:
    response = requests.post(
        "https://httpbin.org/post",
        json = student,
        timeout = 10
    )
    response.raise_for_status()
    data = response.json()
    print(data["json"])
except requests.exceptions.RequestException as e:
    print("请求失败", e)
    


# %%
import requests
student = {
    "name": "小明",
    "score": 95
}
try:
    response = requests.post(
        "https://httpbin.org/post",
        data = student,
        timeout = 10
    )
    response.raise_for_status()
    data = response.json()
    print(data["form"])
except requests.exceptions.RequestException as e:
    print("请求失败", e)
# %%
