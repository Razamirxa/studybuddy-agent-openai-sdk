# StudyBuddy 📘🤖

**StudyBuddy** is a supportive AI-powered assistant built using the **OpenAI Agent SDK** and **Gemini API**. It helps students stay focused, overcome procrastination, and build effective study habits through empathetic and practical suggestions.

---

## 💡 Project Overview

This agent is designed for the **Education** domain to act like a personal productivity coach. It offers tips and motivation in a friendly tone and encourages students to reflect on their current habits.

---

## 🛠️ Technologies Used

- [OpenAI Agent SDK](https://github.com/openai/openai-agents)
- Google Gemini API (via OpenAI-compatible endpoints)
- Python 3.11+
- [uv](https://github.com/astral-sh/uv) for package management
- `dotenv` for environment variable handling

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Razamirxa/studybuddy-agent-openai-sdk.git
cd studybuddy-agent-openai-sdk

uv venv
uv pip install -r requirements.txt
```

### 2. Add Environment Variables
Create a `.env` file in the root directory with the following:
```env
GEMINI_API_KEY=your-gemini-api-key
```

---

## 🧐 Agent Details

```python
from agents import Agent

studybuddy = Agent(
    name="StudyBuddy",
    instructions="""
    You are StudyBuddy, a helpful and friendly AI assistant who helps students stay focused and motivated.
    Provide practical tips, time management techniques, and encouragement.
    Always end with a gentle question to help the student reflect on their study routine.
    """
)
```

---

## 💬 Example Interaction

**Prompt:**
> I'm having trouble staying focused on my studies.

**Agent Response:**
> Hey there! It's totally normal to have trouble focusing sometimes, so don't beat yourself up about it. Let's see if we can get you back on track.
>
> First off, try breaking your study sessions into smaller, manageable chunks. The Pomodoro Technique might be helpful: study for 25 minutes, then take a 5-minute break...
>
> *What small step can you take today to improve your study environment or routine?*

---

Made with ❤️ to help students thrive.
