import os
import requests
import sys

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("没有找到 API Key")
    sys.exit(1)
else:
    print("成功找到 API Key")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

messages = [
    {
    "role": "system",
    "content":"你是一名专业的 Python 编程老师。请使用中文回答，每次只讲一个知识点，先引导学生思考，不要直接公布答案"
}
]
url = "https://api.deepseek.com/chat/completions"
roles = {
        "/teacher":{
            "name" : "teacher",
            "prompt" :
        "你是一名专业的 Python 编程老师。请使用中文回答，每次只讲一个知识点，先引导学生思考，不要直接公布答案"
        },

        "/coder": {
            "name" : "coder",
            "prompt" : "你是一名专业的 Python 工程师。请使用中文回答"
        },
        "/friend": {
            "name" : "friend",
            "prompt" : "你是一个善解人意的朋友，用中文回答"
        }
    }
def show_help():
    for command, role in roles.items():  
            print(f"角色名称：{role['name']}, 切换指令：{command}")

    print("/clear - 清空聊天记录")
    print("/help - 显示帮助菜单")
    print("退出 - 结束程序")

def clear_history():
    global messages
    messages = messages[:1]

while True:
    question = input("你：（输入'退出'结束对话）")
    if question == "退出":
        print("聊天结束")
        break

    if question == "/clear":
        clear_history()
        print("聊天记录已清除，角色设定已保留")
        continue

    if question == "/help":
        show_help()
        continue

    if question in roles:
        messages[0]["content"] = roles[question]["prompt"]
        print(f"角色切换成功,当前角色为{roles[question]['name']}")
        continue

    if question.startswith("/") and question not in roles:
        print("未知指令，请输入有效角色或正常聊天内容。")
        continue

    messages.append({
        "role": "user",
        "content": question
    })

    data = {
        "model": "deepseek-flash",
        "messages": messages
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
        answer = result["choices"][0]["message"]["content"]
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(f"Deepseek 回复：{answer}")

    except requests.exceptions.RequestException as e:
        print("请求失败：", e)
