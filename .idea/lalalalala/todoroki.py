from math import gcd
class My_Fraction:
    def __init__(self,num, den):
        if num != 0 and den != 0:
            k = gcd(num, den)
            self.num = num // k
            self.den = den
        else:
            raise ValueError
    @staticmethod
    def generate(num_min, num_max, den_min, den_max):
        return My_Fraction(randint(num_min, num_max), randint(den_min, den_max))
    def __str__(self):
        return f'{self.num}/{self.den}'
    def __mul__(self, other):
        if isinstance(other, My_Fraction):
            return My_Fraction(self.num * other.num, self.den * self.den)
        if isinstance(other, int):
            return My_Fraction(self.num, self.den)
    def
