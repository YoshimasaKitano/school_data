#!/usr/bin/env python3
import sys
import json

from create_ans import answer_question


def read_stdin_text() -> str:
    """
    PHP から渡された標準入力を UTF-8 として読み取る。
    Windows では sys.stdin.read() が cp932 などでデコードされることがあるため、
    必ずバイナリから UTF-8 で明示的にデコードする。
    """
    data = sys.stdin.buffer.read()
    if not data:
        return ""
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("utf-8", errors="replace")


def main() -> None:
    try:
        raw = read_stdin_text().strip()
        if not raw:
            raise ValueError("no input")

        # PHP 側からは {"question": "..."} の JSON が送られてくる想定
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            payload = {"question": raw}

        question = (payload.get("question") or payload.get("message") or "").strip()
        if not question:
            raise ValueError("question is empty")

        user_profile = (payload.get("user_profile") or "").strip()
        assistant_style = (payload.get("assistant_style") or "").strip()

        answer = answer_question(question, user_profile=user_profile, assistant_style=assistant_style)

        if not isinstance(answer, str):
            answer = str(answer)
        if not answer.strip():
            # 万一空文字が返ってきた場合の保険
            answer = "申し訳ありません。うまくお答えできませんでした。もう一度質問してもらえますか？"

        resp = {"answer": answer}

    except Exception as e:  # noqa: BLE001
        # どんな例外もここで JSON {"error": "..."} にまとめる
        # ユーザーには具体的なエラー内容は見せず、PHP 側で「AI内部でエラーが発生しました。」と表示される
        sys.stderr.write(f"[ai_bridge] error: {e}\n")
        resp = {"error": "internal_error"}

    # PHP 側に UTF-8 の JSON を返す
    out = json.dumps(resp, ensure_ascii=False)
    sys.stdout.buffer.write(out.encode("utf-8", "replace"))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
