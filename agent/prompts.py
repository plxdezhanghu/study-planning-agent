from typing import Dict

# 系统提示词：定义 Agent 的人设 + 输出格式
SYSTEM_PROMPT = """
You are a study planning agent for a Chinese CS sophomore.
Your job is to generate clear, practical, structured study plans.

You must first think step by step about:
- the student's goal,
- their current level,
- time available,
- and chosen focus area.

Then you output in TWO parts:
1) A friendly explanation in Chinese.
2) A JSON object:

{
  "goal": "string",
  "focus_area": "string",
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

The JSON must be valid (no comments).
"""

# 显示给模型看的“学习方向解释”
FOCUS_DESC_MAP: Dict[str, str] = {
    "python-basics": "Python 语法基础 + 刷题 + 小脚本",
    "ai-agent-basics": "大模型基础、API 调用、Agent 概念",
    "project-and-resume": "做可展示的项目、整理简历和 GitHub",
}


def build_user_prompt(info: dict) -> str:
    """
    根据用户输入的信息，构造发给大模型的 prompt 文本。
    info 是 collect_user_input 返回的字典。
    """
    focus_desc = FOCUS_DESC_MAP.get(info["focus"], "AI / Agent 综合提升")

    return f"""
用户信息：
- 目标：{info['goal']}
- 总天数：{info['days']}
- 每天学习时间：{info['hours']}
- 当前水平：{info['level']}
- 学习方向（内部标签）：{info['focus']}
- 学习方向说明：{focus_desc}

请根据以上信息生成一个详细的学习计划。
请严格按照 SYSTEM_PROMPT 中要求的格式输出：先中文说明，再 JSON。
"""
