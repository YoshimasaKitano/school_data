import json
import os
import google.generativeai as genai

# -----------------------------
# ① 環境変数から API キーを取得
# -----------------------------
# 事前に OS 側で環境変数を設定しておくこと
# Windows (PowerShell):
#   setx GOOGLE_API_KEY "YOUR_API_KEY"
# macOS/Linux (bash/zsh):
#   export GOOGLE_API_KEY="YOUR_API_KEY"

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("環境変数 'GOOGLE_API_KEY' が設定されていません。")

genai.configure(api_key=api_key)

# -----------------------------
# ② JSON読み込み
# -----------------------------
with open("articles.json", "r", encoding="utf-8") as f:
    ARTICLES = json.load(f)

# -----------------------------
# ③ カテゴリ・サブカテゴリ作成
# -----------------------------
SUBCATEGORIES = sorted(list({a["subcategory"] for a in ARTICLES if a["subcategory"]}))
CATEGORIES = sorted(list({a["category"] for a in ARTICLES if a["category"]}))

def subcategories_text():
    return "\n".join(f"- {s}" for s in SUBCATEGORIES)

def categories_text():
    return "\n".join(f"- {c}" for c in CATEGORIES)

# -----------------------------
# ④ Gemini で分類する関数
# -----------------------------
def ask_gemini(prompt: str):
    model = genai.GenerativeModel("gemini-2.5-flash")
    res = model.generate_content(prompt)
    return res.text.strip()

def classify_subcategory(question: str):
    prompt = f"""
以下はすべてのサブカテゴリー一覧です：

{subcategories_text()}

質問：「{question}」

あなたの役割：
- 質問が最も当てはまるサブカテゴリー名を一つだけ返す
- 選べない場合は「None」を返す
- 文章以外は出力しない
"""
    return ask_gemini(prompt)

def classify_category(question: str):
    prompt = f"""
以下はすべてのカテゴリー一覧です：

{categories_text()}

質問：「{question}」

あなたの役割：
- 質問が最も当てはまるカテゴリー名を一つだけ返す
- 選べない場合は「None」を返す
"""
    return ask_gemini(prompt)

# -----------------------------
# ⑤ JSON全文検索関数
# -----------------------------
def search_articles_by_subcategory(subcat):
    return [a for a in ARTICLES if a["subcategory"] == subcat]

def search_articles_by_category(cat):
    return [a for a in ARTICLES if a["category"] == cat]

def search_school_overview(question):
    texts = [a for a in ARTICLES if a["category"] == "学校概要"]
    keyword = question.lower()
    return [a for a in texts if keyword in a["text"].lower() or keyword in a["title"].lower()]

# -----------------------------
# ⑥ RAG生成
# -----------------------------
def generate_answer(question, context_articles):
    context_text = "\n\n".join([f"◎ {a['title']}\n{a['text']}" for a in context_articles])
    prompt = f"""
【質問】
{question}

【参考情報（RAG）】
{context_text}

【指示】
- 上記の情報のみを参考に正確な回答を作成してください。
- データに無い情報を捏造しないこと。
- わからない部分は「わかりません」と明確に言うこと。
"""
    return ask_gemini(prompt)

# -----------------------------
# ⑦ 全体フロー
# -----------------------------
def answer_question(question: str):
    subcat = classify_subcategory(question)
    print("サブカテゴリ判定:", subcat)

    if subcat != "None":
        data = search_articles_by_subcategory(subcat)
        if data:
            return generate_answer(question, data)

    cat = classify_category(question)
    print("カテゴリ判定:", cat)

    if cat != "None":
        data = search_articles_by_category(cat)
        if data:
            return generate_answer(question, data)

    data = search_school_overview(question)
    if data:
        return generate_answer(question, data)

    return "申し訳ありません、その質問に関連する情報が見つかりませんでした。"

# -----------------------------
# ⑧ 実行例
# -----------------------------
if __name__ == "__main__":
    print(answer_question("学園祭はいつですか？"))
