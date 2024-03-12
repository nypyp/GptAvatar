import json
import openai
openai.api_key = "sess-BENqmiOJnhmFkReRlGXm2WA492S1uKQcV7wrevt0"
# 替换成你的OpenAI API密钥


# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "user", "content": "Hello!"}
#   ]
# )
# #输出生成的内容
# print(completion.choices[0].message)

# #把整个响应输出一下
# print(completion)

while True:

    msg = input("请输入:")
    if msg == "exit":
        print("已退出聊天程序")
        break
    else:
        completion =openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                    {"role": "user","content": msg}
        ]
        )
        message = json.dumps(completion.choices[0].message, indent=4, ensure_ascii=False)
        content = json.loads(message)["content"]
        max_width = 50
        content = '\n'.join(content[i:i + max_width] for i in range(0, len(content), max_width))
        print("机器人:"+ content)