import os
from dotenv import load_dotenv
from openai import OpenAI

# بارگذاری کلید از فایل .env
load_dotenv()
api_key = os.getenv("AVALAI_API_KEY")

# اتصال به AvalAI (به جای OpenAI مستقیم)
client = OpenAI(
    api_key=api_key,
    base_url="https://api.avalai.ir/v1"
)

# اولین پیام به هوش مصنوعی
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "سلام! یک جمله کوتاه به فارسی بگو که نشون بده وصل شدی."}
    ]
)

print(response.choices[0].message.content)