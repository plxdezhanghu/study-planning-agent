def choose_focus_area() -> str:
    """
    让用户选择学习方向，返回一个内部标签字符串。
    """
    print("请选择你的主要学习方向：")
    print("1. Python 基础")
    print("2. AI / Agent 基础")
    print("3. 实战项目 & 简历")

    choice = input("> ").strip()

    mapping = {
        "1": "python-basics",
        "2": "ai-agent-basics",
        "3": "project-and-resume",
    }

    return mapping.get(choice, "ai-agent-basics")


def collect_user_input() -> dict:
    """
    收集用户输入，返回结构化的字典信息。
    """
    print("=== 学习规划智能体（DeepSeek 版 · 模块化）===")
    goal = input("你的学习目标是什么？\n> ")
    days = input("你希望多少天完成？（数字）\n> ")
    hours = input("你每天大约能学习多少小时？（数字）\n> ")
    level = input("你目前的基础如何？\n> ")
    focus = choose_focus_area()

    # 类型转换 + 容错
    try:
        days_int = int(days)
    except ValueError:
        days_int = 30

    try:
        hours_float = float(hours)
    except ValueError:
        hours_float = 2.0

    return {
        "goal": goal,
        "days": days_int,
        "hours": hours_float,
        "level": level,
        "focus": focus,
    }
