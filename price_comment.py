import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

food_items = [
    {"名前": "鶏卵", "先月": 290, "今月": 320, "単位": "円/kg"},
    {"名前": "キャベツ", "先月": 95, "今月": 110, "単位": "円/kg"},
    {"名前": "豚肉", "先月": 720, "今月": 750, "単位": "円/kg"},
]

price_text = ""
for item in food_items:
    変化 = item["今月"] - item["先月"]
    方向 = "値上がり" if 変化 > 0 else "値下がり"
    price_text += f"・{item['名前']}：{item['先月']}{item['単位']} → {item['今月']}{item['単位']}（{方向} {abs(変化)}円）\n"

prompt = f"""
以下の食材価格の変動について、経営会議向けに簡潔なコメントを150字以内で作成してください。

{price_text}

コメントは「今月の食材価格は」で始めてください。
"""

message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": prompt}]
)

print("=== 経営会議向けコメント ===")
print(message.content[0].text)