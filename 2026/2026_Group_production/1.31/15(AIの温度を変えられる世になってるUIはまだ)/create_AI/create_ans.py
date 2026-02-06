import json
import os
from typing import List, Dict, Any, Optional, Tuple

# =============================
# 設定・共通ユーティリティ
# =============================

BASE_DIR = os.path.dirname(__file__)
ARTICLES_PATH = os.path.join(BASE_DIR, "articles.json")

# articles.json の読み込み
try:
    with open(ARTICLES_PATH, "r", encoding="utf-8") as f:
        ARTICLES: List[Dict[str, Any]] = json.load(f)
except Exception:
    ARTICLES = []

# Gemini ライブラリ（無ければ None にしてフォールバック）
try:
    import google.generativeai as genai  # type: ignore
except Exception:
    genai = None  # type: ignore


def _safe_str(x: Any) -> str:
    """UTF-8 安全な文字列に変換する。"""
    if isinstance(x, str):
        s = x
    else:
        s = str(x)
    try:
        return s.encode("utf-8", "ignore").decode("utf-8", "ignore")
    except Exception:
        return s


def _get_api_key() -> Optional[str]:
    """
    API キーを取得する。
    1) 環境変数 GOOGLE_API_KEY
    2) create_AI/google_api_key.txt の 1 行目
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key:
        api_key = api_key.strip()
        if api_key:
            return api_key

    key_path = os.path.join(BASE_DIR, "google_api_key.txt")
    if os.path.exists(key_path):
        try:
            with open(key_path, "r", encoding="utf-8") as f:
                k = f.read().strip()
                if k:
                    return k
        except Exception:
            pass
    return None


# =============================
# JSON（articles.json）側の検索ロジック
# =============================

KEYWORDS = [
    "ホワイトハッカー",
    "ホワイトハッカー専攻",
    "AIエンジニア",
    "AIエンジニア専攻",
    "専攻",
    "コース",
    "学費",
    "授業",
    "カリキュラム",
    "資格",
    "就職",
    "入試",
    "試験",
    "オープンキャンパス",
    "OCA",
]


def _score_article(question: str, art: Dict[str, Any]) -> float:
    """
    質問文と記事との簡易スコアリング。
    文字レベルの重なり＋いくつかの重要キーワードで重み付けする。
    """
    title = _safe_str(art.get("title", ""))
    text = _safe_str(art.get("text", ""))
    subcat = _safe_str(art.get("subcategory") or art.get("category") or "")
    full = f"{title}。{text}。{subcat}"

    q = question.strip()
    if not q:
        return 0.0

    score = 0.0

    # 質問全文が含まれていれば大きく加点
    if q in full:
        score += 6.0

    # 文字レベルの重なり（短文に対して強くなりすぎないよう、控えめ）
    chars = set(q)
    for ch in chars:
        if ch.strip() and ch in full:
            score += 0.3

    # キーワード一致
    lower_full = full.lower()
    lower_q = q.lower()
    for kw in KEYWORDS:
        if kw in full and kw in q:
            score += 3.0
        elif kw.lower() in lower_full and kw.lower() in lower_q:
            score += 1.5

    # サブカテゴリ名が質問文に含まれている場合のボーナス
    base_sub = subcat.replace("専攻", "").replace("コース", "")
    if base_sub and base_sub in q:
        score += 4.0

    return score


def _search_articles(question: str, limit: int = 5) -> List[Dict[str, Any]]:
    """質問に関連しそうな記事をスコア順に最大 limit 件返す。"""
    if not ARTICLES:
        return []

    scored: List[Tuple[float, Dict[str, Any]]] = []
    for art in ARTICLES:
        s = _score_article(question, art)
        if s > 0.0:
            scored.append((s, art))

    if not scored:
        return []

    scored.sort(key=lambda x: x[0], reverse=True)

    result: List[Dict[str, Any]] = []
    for s, art in scored:
        if s < 1.0:
            break
        result.append(art)
        if len(result) >= limit:
            break
    return result


def _build_context(articles: List[Dict[str, Any]]) -> str:
    """
    Gemini に渡す CONTEXT 文字列を作る。
    OCA のパンフレット抜粋のようなイメージ。
    """
    if not articles:
        return "（関連する学校情報は見つかりませんでした。）"

    parts: List[str] = []
    for art in articles:
        subcat = _safe_str(art.get("subcategory") or art.get("category") or "情報")
        title = _safe_str(art.get("title") or "")
        text = _safe_str(art.get("text") or "")

        if len(text) > 500:
            text = text[:500] + "..."

        header = f"【{subcat}】"
        if title:
            header += title
        parts.append(f"{header}\n{text}")

    return "\n\n".join(parts)


# =============================
# フォールバック回答
# =============================

def _fallback_answer(question: str, articles: List[Dict[str, Any]]) -> str:
    """
    Gemini が使えない場合のフォールバック回答。
    技術的なエラー内容はユーザーに見せない。
    """
    q = question.strip()
    if not articles:
        return (
            "現在 AI の回答生成で問題が発生しているため、"
            "詳しいお答えができません。時間をおいてもう一度お試しください。"
        )

    lines: List[str] = []
    lines.append(
        "現在 AI の回答生成で問題が発生しているため、"
        "登録されている学校データの要約でご案内します。"
    )
    lines.append("")

    for art in articles:
        subcat = _safe_str(art.get("subcategory") or art.get("category") or "")
        title = _safe_str(art.get("title") or "")
        text = _safe_str(art.get("text") or "")

        if len(text) > 200:
            text = text[:200] + "..."

        if subcat:
            lines.append(f"【{subcat}】{title}")
        elif title:
            lines.append(f"【情報】{title}")
        if text:
            lines.append(text)
        lines.append("")

    return "\n".join(l for l in lines if l.strip())


# =============================
# メイン: answer_question
# =============================

def answer_question(question: str, user_profile: str = "", assistant_style: str = "") -> str:
    """
    フロントエンド（PHP）から呼び出されるメイン関数。

    - articles.json から関連しそうな記事を探す
    - Gemini が利用可能なら、それを CONTEXT として会話形式で回答
    - Gemini が利用できない / 失敗した場合は JSON だけでフォールバック回答
    """
    q = _safe_str(question).strip()
    if not q:
        return "質問が空です。もう一度入力してください。"

    # JSON から関連記事を抽出（Gemini が使える場合もコンテキストとして使用）
    articles = _search_articles(q, limit=5)

    # Gemini がそもそも使えない場合はフォールバック
    if genai is None:
        return _fallback_answer(q, articles)

    api_key = _get_api_key()
    if not api_key:
        return _fallback_answer(q, articles)

    context_text = _build_context(articles)

    # モデル名: 環境変数 GEMINI_MODEL_NAME > デフォルト gemini-2.5-flash-lite
    model_name = os.getenv("GEMINI_MODEL_NAME") or "gemini-2.5-flash-lite"

    prompt = f"""あなたは OCA大阪デザイン&テクノロジー専門学校に関するアシスタントです。
次のルールに従って、日本語で自然な文章で回答してください。

# ユーザー情報（AI が事前に知っておくべきこと）
{user_profile or '（特になし）'}

# 応答スタイルの希望
{assistant_style or '（特になし。丁寧な敬体で、分かりやすく説明してください。）'}

# ルール
- CONTEXT に関係する質問の場合は、できるだけ CONTEXT の情報を使って分かりやすく説明してください。
- CONTEXT にない具体的な日程・学費・住所・電話番号などは、推測せず
  「正確な情報は公式サイトや学校に直接確認してください」と伝えてください。
- 単なるあいさつや雑談（例: こんにちは／元気？／最近どう など）には、
  CONTEXT に関係しなくても、普通の会話としてフレンドリーに返事して構いません。
- 専門学校や OCA と無関係な話題（天気・趣味など）も、軽い雑談として答えて構いません。
- OCA に関する内容で事実が不明なときは、適当に作らず
  「分かりません」「公式情報を確認してください」と伝えてください。
- 箇条書きにしても構いませんが、「以下の情報が見つかりました。」のような機械的な定型文は使わず、
  会話として自然な表現にしてください。
- 出力はマークダウンではなく、シンプルな日本語の文章だけで返してください。
- 文章量は 2〜6 文程度を目安にしてください。

# CONTEXT
{context_text}

# ユーザーの発言
{q}
"""

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)
        res = model.generate_content(prompt)
        text = _safe_str(getattr(res, "text", "")).strip()
        if not text:
            return _fallback_answer(q, articles)
        return text
    except Exception:
        # 技術的なエラー内容はユーザーには見せず、静かにフォールバック
        return _fallback_answer(q, articles)


if __name__ == "__main__":
    # 簡易テスト
    tests = [
        "ホワイトハッカー専攻について教えてください",
        "AIエンジニア専攻はどんなことを学びますか？",
        "こんにちは",
        "最近の趣味はゲームです。おすすめの過ごし方ありますか？",
    ]
    for t in tests:
        print("Q:", t)
        print(answer_question(t))
        print("-" * 60)
