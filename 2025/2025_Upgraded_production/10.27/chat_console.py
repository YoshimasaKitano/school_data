# chat_console.py
from rag_core import generate_answer

def main():
    print("=== 🎓 学校案内チャットBot ===")
    print("質問を入力してください。終了するには「exit」と入力。")
    print("-----------------------------------------")

    while True:
        user_input = input("あなた: ")
        if user_input.lower() in ["exit", "quit", "終了"]:
            print("Bot: ご利用ありがとうございました！")
            break

        print("Bot: 考え中...")
        answer = generate_answer(user_input)
        print(f"Bot: {answer}\n")

if __name__ == "__main__":
    main()