# Study Planning Agent (DeepSeek + Python)

一个基于 **DeepSeek API** 的命令行学习规划智能体，  
专门为「普通二本学校的计算机大二学生」设计，用来生成结构化的学习计划。

> This is a command-line study planning agent powered by DeepSeek API,
> designed for a CS sophomore to generate structured, JSON-based study plans.

---

## ✨ 项目功能 Features

- 根据用户输入的 **学习目标 / 时间 / 当前水平** 自动生成学习计划  
- 支持选择不同学习方向：  
  - Python 基础（`python-basics`）  
  - AI / Agent 基础（`ai-agent-basics`）  
  - 实战项目 & 简历（`project-and-resume`）  
- 输出包含两部分：
  1. 中文解释说明  
  2. 一个严格结构化的 JSON 计划（方便后续接前端 / n8n / 其它 Agent）

---

## 🧱 技术栈 Tech Stack

- **Python 3.11+**（本地环境）
- **virtualenv / venv**：项目级虚拟环境
- **DeepSeek API（OpenAI 协议兼容）**
- `openai` Python SDK (>=1.40,<2.0)
- `python-dotenv`：读取 `.env` 配置

---

## 📂 项目结构 Project Structure

```text
study-planning-agent/
├─ venv/                # 虚拟环境（本地，用 .gitignore 忽略）
├─ .env                 # 环境变量（DeepSeek API Key，本地私密）
├─ .gitignore           # 忽略 venv / .env / 缓存
├─ requirements.txt     # 依赖列表
└─ main.py              # Agent 主程序入口
