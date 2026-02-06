#!/usr/bin/env python3
import sys
import json

from create_ans import answer_question

def main():
    try:
        raw = sys.stdin.read()
        raw = raw.strip()
        if not raw:
            raise ValueError("no input")

        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            # プレーンテキストで送られてきた場合
            payload = {"question": raw}

        question = payload.get("question") or payload.get("message") or ""
        if not question:
            raise ValueError("question is empty")

        answer = answer_question(question)
        resp = {"answer": answer}
    except Exception as e:
        resp = {"error": str(e)}

    sys.stdout.write(json.dumps(resp, ensure_ascii=False))

if __name__ == "__main__":
    main()
