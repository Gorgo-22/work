# work — 名阪食品 仕入部 業務自動化ツール群

仕入部の経営会議報告書作成、価格動向分析、データ収集を効率化するためのPythonツール集です。

---

## 含まれるツール

### 1. weekly_report.py — 週次食品動向報告書 自動生成

**用途**: 経営会議向けの週次食品動向報告書を自動作成

**機能**:
- Excel(`food_prices.xlsx`)から玉子価格・期間を読み込み
- Web検索(Claude API)で最新の野菜価格・食品値上げ情報・食中毒情報を自動収集
- メタコメント自動除去
- Word文書(`.docx`)として表組み付きで自動保存
- 履歴シートに実行結果を自動蓄積

**使い方**: 詳細は [運用手順.md](./運用手順.md) を参照
---

### 2. price_comment.py — 食材価格コメント自動生成

**用途**: 月次の食材価格データから経営会議向けコメントを生成

**機能**:
- Excel(`food_prices.xlsx`の「食材価格」シート)から18品目の価格データを読み込み
- カテゴリ別の平均価格・変動率を自動計算
- Claude APIで分析コメントを自動生成

**使い方**:
---

### 3. setup_weekly_sheet.py — 週次設定シート 初回作成

`food_prices.xlsx` に「週次設定」シートを作成する初回セットアップ用スクリプト。
通常は1回だけ実行する。

---

### 4. setup_history_sheet.py — 履歴シート 初回作成

`food_prices.xlsx` に「履歴」シートを作成する初回セットアップ用スクリプト。
通常は1回だけ実行する。

---

### 5. create_excel.py — 食材価格Excel 初回作成

CSVから`.xlsx`形式に変換する初回セットアップ用スクリプト。
通常は1回だけ実行する。

---

## ファイル構成
work/
├── .env                       ← APIキー（Git管理外）
├── .gitignore                 ← Git除外設定
├── README.md                  ← このファイル
├── 運用手順.md                ← 週次報告書ツールの運用手順書
├── food_prices.xlsx           ← データファイル（3シート構成）
│   ├─ 週次設定                ← 玉子価格・期間（毎週更新）
│   ├─ 食材価格                ← 18品目データ
│   └─ 履歴                    ← 過去の実行結果
├── weekly_report.py           ← 週次報告書ツール（メイン）
├── price_comment.py           ← 食材価格コメントツール
├── setup_weekly_sheet.py      ← 初回セットアップ用
├── setup_history_sheet.py     ← 初回セットアップ用
├── create_excel.py            ← 初回セットアップ用
├── claude_test.py             ← APIテスト用
└── hello.py                   ← Python練習用

---

## 環境構築

### 必要なもの

- Python 3.12
- Anthropic APIキー
- Microsoft Excel
- VSCode（推奨）

### 初回セットアップ手順

1. リポジトリをクローン
2. 必要なライブラリをインストール
3. `.env` ファイルを作成し、APIキーを設定
4. Excelファイルの初期化（必要に応じて）