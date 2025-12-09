import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载 .env 文件
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.deepseek.com")
MODEL_NAME = os.getenv("OPENAI_MODEL", "deepseek-chat")

if not API_KEY:
    raise RuntimeError("请在 .env 文件中填写你的 DeepSeek API Key")

# 创建 DeepSeek 客户端
client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL,
)

SYSTEM_PROMPT = """
You are a study planning agent for a Chinese CS sophomore.
Your job is to generate clear, practical, structured study plans.

Output format requirement:
1. Provide a Chinese explanation first.
2. Then provide a JSON object in the following exact format:

{
  "goal": "string",
  "total_days": number,
  "hours_per_day": number,
  "plan": [
    {
      "day": number,
      "focus": "string",
      "tasks": ["string", "string"]
    }
  ]
}

Ensure the JSON has no comments and is valid.
"""

def collect_user_input():
    print("=== 学习规划智能体（DeepSeek 版）===")
    goal = input("你的学习目标是什么？\n> ")
    days = input("你希望多少天完成？（数字）\n> ")
    hours = input("每天能投入多少小时？（数字）\n> ")
    level = input("你目前的水平如何？\n> ")

    try:
        days = int(days)
    except:
        days = 30

    try:
        hours = float(hours)
    except:
        hours = 2.0

    return {
        "goal": goal,
        "days": days,
        "hours": hours,
        "level": level
    }

def build_prompt(info):
    return f"""
用户信息：
- 目标：{info['goal']}
- 总天数：{info['days']}
- 每天学习时间：{info['hours']}
- 当前水平：{info['level']}

请根据以上信息生成学习计划。
"""

def call_agent(prompt):
    resp = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return resp.choices[0].message.content

def main():
    info = collect_user_input()
    prompt = build_prompt(info)

    print("\nDeepSeek 正在生成学习计划...\n")
    result = call_agent(prompt)

    print("===== 输出 =====\n")
    print(result)
    print("\n===============\n")

if __name__ == "__main__":
    main()