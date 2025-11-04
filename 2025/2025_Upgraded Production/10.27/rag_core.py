# rag_core.py
import sqlite3
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from openai import OpenAI

# === 設定 ===
DB_PATH = "oca_data.db"
MODEL_NAME = "all-MiniLM-L6-v2"
OPENAI_API_KEY = "あなたのOpenAI APIキー"

client = OpenAI(api_key=OPENAI_API_KEY)
model = SentenceTransformer(MODEL_NAME)

# === データ読み込み ===
def load_articles():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, text, category, subcategory FROM articles")
    data = cursor.fetchall()
    conn.close()
    return data

articles = load_articles()
texts = [a[2] for a in articles]
meta = [{"id": a[0], "title": a[1], "category": a[3], "subcategory": a[4]} for a in articles]

# === ベクトル化とインデックス構築 ===
print("🔍 データをベクトル化中...")
embeddings = model.encode(texts, show_progress_bar=True)
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))
print("✅ ベクトルインデックス作成完了！")

# === 類似検索 ===
def search_similar_articles(query, top_k=3):
    q_vec = model.encode([query])
    D, I = index.search(np.array(q_vec), top_k)
    results = [texts[i] for i in I[0]]
    return results

# === 回答生成 ===
def generate_answer(query):
    related = search_similar_articles(query)
    context = "\n\n".join(related)
    prompt = f"""
あなたは学校案内AIです。以下の情報をもとに、質問に簡潔で自然な日本語で答えてください。
情報が不十分な場合は「不明です」と述べてください。

---情報---
{context}

---質問---
{query}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content