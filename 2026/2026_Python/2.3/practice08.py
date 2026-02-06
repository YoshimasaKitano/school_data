class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    
    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)
        print(f"{self.name}は{amount}のダメージを受けた！ 残りHP: {self.hp}")

    def is_alive(self):
        if self.hp > 0:
            pass
        else:
            print(f"{self.name}は力尽きた。")
    
class Warrior(Character):
    def __init__(self, name, hp, attack, defence):
        super().__init__(name, hp, attack)
        self.defence = defence
    
    def take_damage(self, amount):
        amount = amount - self.defence
        super().take_damage(amount)
        
class Mage(Character):
    def __init__(self, name, hp, attack) :
        super().__init__(name, hp, attack)
    
    def cast_spell(self, target):
        attack = 12
        print(f"{self.name}の魔法攻撃！ {target.name}に{attack}ダメージ！")
        target.take_damage(attack)
    
warrior = Warrior("ウォリアー", 40, 8, 3)
mage = Mage("メイジ", 30, 5)

print("--- 戦⼠の攻撃 ---")
mage.take_damage(8)
print()
print("--- メイジの魔法 ---")
mage.cast_spell(warrior)
print()
print("--- 戦⼠の攻撃 ---")
mage.take_damage(8)
print()
print("=== 戦闘終了 ===")


