### practice08.py
"""
RPG に登場するキャラクターをオブジェクト指向で表現するためのクラス構造
"""

# 親クラス︓Character
class Character:
    ## 初期化設定
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    ## ダメージを受け HP を減少させる（最低 0）
    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)
        print(f"{self.name} は {amount} のダメージを受けた！ 残りHP: {self.hp}")

    ## HP が 0 より大きいか判定
    def is_alive(self):
        return self.hp > 0

# 子クラス︓Warrior（戦士）
class Warrior(Character):
    ## 追加属性:防御力(defense)
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack)
        self.defense = defense

    ## オーバーライド:防御力を考慮したダメージ計算
    ### 計算式:ダメージ = max(1, 攻撃力 - 防御力) 
    def take_damage(self, amount):
        super().take_damage(max(1, amount - self.defense))

# 子クラス︓Mage（魔法使い）
class Mage(Character):
    ## 追加メソッド:ターゲットに12ダメージの魔法攻撃
    def cast_spell(self, target):
        spall_damage = 12
        print(f"{self.name}の魔法攻撃！{target.name} に {spall_damage} ダメージ！ ")
        target.take_damage(spall_damage)

# 動作確認
warrior = Warrior("ウォーリア", 40, 8, 3)
mage = Mage("メイジ", 30, 5)

## 1. 戦士が攻撃
print("戦士が攻撃")
mage.take_damage(warrior.attack)
### メイジが 8 ダメージを受ける → HP 22

## 2. メイジが魔法攻撃
print("メイジが魔法攻撃")
mage.cast_spell(warrior)
### ウォリアーが魔法ダメージ 12 を受ける
### 防御力 3 により実ダメージは 9 → HP 31

## 3. 戦士が再度攻撃
mage.take_damage(warrior.attack)
### メイジが 8 ダメージ → HP 14

## 4. 戦闘終了
print("戦闘終了")