import os
import requests
import sys

# 1. 读取 API Key
api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    print("没有找到 API Key")
    sys.exit(1)

# 2. 设置请求头
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# 3. 设置请求正文
question = input("请输入你的问题：")
data = {
    "model": "deepseek-flash",
    "messages": [
        {
            "role": "user",
            "content": question
        }
    ]
}

# 4. 发送请求
url = "https://api.deepseek.com/chat/completions"

try:
    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=30
    )

    response.raise_for_status()

    # 5. 解析服务器响应
    result = response.json()

    # 6. 取出 AI 的回答
    answer = result["choices"][0]["message"]["content"]

    print("DeepSeek 回复：")
    print(answer)

except requests.exceptions.RequestException as e:
    print("请求失败：", e)