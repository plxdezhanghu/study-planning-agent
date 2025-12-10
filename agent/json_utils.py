import json
from typing import Any, Dict, Optional, Tuple


def extract_json_from_text(text: str) -> Tuple[str, Optional[Dict[str, Any]]]:
    """
    从模型返回的完整文本中，尝试提取 JSON 部分。
    返回 (explanation_text, json_obj 或 None)。

    简单策略：
    - 找到第一个 '{' 和最后一个 '}' 之间的内容
    - 尝试 json.loads 解析
    - 如果失败，就返回原文 + None
    """
    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1 or end <= start:
        # 找不到 JSON，大概率模型没按要求输出
        return text.strip(), None

    json_str = text[start : end + 1]
    explanation = text[:start].strip()

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        # JSON 解析失败，直接把整段文本当说明返回
        return text.strip(), None

    return explanation, data
