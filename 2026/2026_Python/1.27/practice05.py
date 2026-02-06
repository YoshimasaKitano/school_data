class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        f = (self.celsius * 9) / 5 + 32
        return float(f)

    @classmethod
    def from_fahrenheit(cls, f):
        c = (f - 32) * 5 / 9
        return cls(c)
    
    @staticmethod
    def is_freezing(c):
        if c <= 0:
            return True
        else:
            return False

t1 = Temperature(10)

t2 = Temperature.from_fahrenheit(14)

print(f"t1の華氏温度: {t1.to_fahrenheit()}")
print(f"t1は氷点下か: {Temperature.is_freezing(t1.celsius)}")
print(f"t2の摂氏温度: {t2.celsius}")
print(f"t2は氷点下か: {Temperature.is_freezing(t2.celsius)}")