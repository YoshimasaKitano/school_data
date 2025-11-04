# # 条件分岐構文、繰返し構文、例外処理の実践問題1

# ## 冷暖房の設定と制御
# ### 概要  
# ユーザーからの操作入力に応じて「暖房」「冷房」「停止」の処理を行い、
# 設定された温度と状態を表示する簡易的な冷暖房管理システムです。

# ### 目的  
# 標準入力と条件分岐処理の習得  
# ユーザーによる冷暖房の設定・状態の管理  
# 選択内容に応じた動作および温度表示の実装

# ### 実装要件
# デフォルト温度：暖房：20度　／　冷房：28度 
# 入力方法：数値入力（1:暖房, 2:冷房, 0:停止 ）
# 温度変更：ユーザー入力。未入力時は各モードの前回の値（初回はデフォルト値）
# エラーハンドリング：例外処理により整数以外の入力に対応
# 表示内容：モード、エアコン状態、設定温度、現在の温度 


# ### 出力例  
# ```
# 操作を入力してください（1:hot / 2:cool / 0:off）： 1
# 暖房ON:設定温度（未入力なら20度）： 
# 暖房を20度で設定しました。

# 操作を入力してください（1:hot / 2:cool / 0:off）： 1
# 暖房ON:設定温度（未入力なら20度）： 25
# 暖房を25度で設定しました。

# 操作を入力してください（1:hot / 2:cool / 0:off）： 2
# 冷房ON:設定温度（未入力なら28度）： 
# 冷房を28度で設定しました。

# 操作を入力してください（1:hot / 2:cool / 0:off）： 2
# 冷房ON:設定温度（未入力なら28度）： 30
# 冷房を30度で設定しました。

# 操作を入力してください（1:hot / 2:cool / 0:off）： 1
# 暖房ON:設定温度（未入力なら25度）： 
# 暖房を25度で設定しました。

# 操作を入力してください（1:hot / 2:cool / 0:off）： 0
# エアコンをOFFにしました。```
hot = 20
hot_copy = 20
cool = 28
cool_copy = 28
while True:
    try:
        num = input("操作を入力してください（1:hot / 2:cool / 0:off)")
        if int(num) == 1:
            if hot == "":
                hot = hot_copy
            else:
                hot_copy = hot
            hot = input(f"暖房ON:設定温度（未入力なら{hot}度）：")
            hot = int(hot)
            print(f"暖房を{hot}度で設定しました。")
        elif int(num) == 2:
            if cool == "":
                cool = cool_copy
            else:
                cool_copy = cool
            cool = input(f"冷房ON:設定温度（未入力なら{cool}度）：")
            cool = int(cool)
            print(f"冷房を{cool}度で設定しました。")
        elif int(num) == 0:
            print("エアコンをOFFにしました。")
            break
        else:
            print("0～2で入力してください")
    except:
        if hot == "":
            print(f"暖房を{hot_copy}度で設定しました。")
            continue
        elif cool == "":
            print(f"冷房を{cool_copy}度で設定しました。")
            continue
        else:
            hot = hot_copy
            cool = cool_copy
            print("数字で入力してください")
            continue

