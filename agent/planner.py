import json
from typing import Dict

from .client import client, MODEL_NAME
from .prompts import SYSTEM_PROMPT, build_user_prompt
from .json_utils import extract_json_from_text


def generate_plan(user_info: Dict) -> str:
    """
    根据用户信息调用 DeepSeek 模型，生成学习计划。
    返回一个格式化后的字符串（包含说明 + 格式化 JSON）。
    """
    prompt = build_user_prompt(user_info)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )

    raw_text = response.choices[0].message.content

    # 尝试从返回结果中拆出 JSON
    explanation, json_obj = extract_json_from_text(raw_text)

    if json_obj is None:
        # 说明模型没按要求输出 JSON，直接返回原文
        return "【模型完整输出】\n" + raw_text

    # 漂亮地打印 JSON（保留中文）
    pretty_json = json.dumps(json_obj, ensure_ascii=False, indent=2)

    result = (
        "【说明部分】\n"
        + explanation
        + "\n\n【JSON 学习计划】\n"
        + pretty_json
    )

    return result
