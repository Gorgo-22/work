import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

food_items = [
    {"名前": "鶏卵（Mサイズ・大阪）", "先月": 300, "今月": 315, "単位": "円/kg"},
    {"名前": "キャベツ", "先月": 118, "今月": 125, "単位": "円/kg（前年比）"},
    {"名前": "レタス", "先月": 105, "今月": 108, "単位": "円/kg（前年比）"},
    {"名前": "白菜", "先月": 108, "今月": 112, "単位": "円/kg（前年比）"},
    {"名前": "トマト", "先月": 120, "今月": 134, "単位": "円/kg（前年比）"},
    {"名前": "きゅうり", "先月": 118, "今月": 126, "単位": "円/kg（前年比）"},
]

price_text = ""
for item in food_items:
    変化 = item["今月"] - item["先月"]
    方向 = "値上がり" if 変化 > 0 else "値下がり"
    price_text += f"・{item['名前']}：{item['先月']}{item['単位']} → {item['今月']}{item['単位']}（{方向} {abs(変化)}）\n"

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
