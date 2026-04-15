import anthropic
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# 今月の年月を自動取得
今月 = datetime.now().strftime("%Y年%m月")

prompt = f"""
{今月}時点での以下の情報を調べて、給食・食品業界の購買担当者向けに報告書形式でまとめてください。

【食品全般の値上げ情報】
・直近1ヶ月以内に発表または実施された食品・飲料の値上げ情報を5件程度
・各項目：食品名/カテゴリ、値上げ時期、値上げ率または概要、報道元

【消耗品の値上げ情報】
・直近1ヶ月以内のラップ・袋・洗剤など業務用消耗品の値上げ情報を3件程度
・各項目：品目/カテゴリ、値上げ時期、値上げ率または概要

【コメの動向】
・最近の米価格・流通に関するニュースを2〜3件

出力形式は箇条書きでわかりやすくまとめてください。
"""

print(f"=== {今月} 食品値上げ・市場動向レポート ===")
print("情報収集中...")

message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=2048,
    messages=[{"role": "user", "content": prompt}]
)

print(message.content[0].text)

# テキストファイルに保存
ファイル名 = f"値上げ情報_{datetime.now().strftime('%Y%m%d')}.txt"
with open(ファイル名, "w", encoding="utf-8") as f:
    f.write(f"=== {今月} 食品値上げ・市場動向レポート ===\n")
    f.write(message.content[0].text)

print(f"\n=== {ファイル名} に保存しました ===")