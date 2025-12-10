import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载 .env 文件中的配置
load_dotenv()

# 从环境变量读取配置
API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.deepseek.com")
MODEL_NAME = os.getenv("OPENAI_MODEL", "deepseek-chat")


if not API_KEY:
    raise RuntimeError("请在 .env 文件中填写 OPENAI_API_KEY")

# 创建 DeepSeek 客户端（兼容 OpenAI 协议）
client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL,
)
