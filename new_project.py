gcd = lambda a, b: a if b == 0 else gcd(b, a%b)
class fraction:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        sum1x = self.x * other.y + self.y * other.x
        sum1y = self.y * other.y
        return fraction(sum1x // gcd(sum1x, sum1y), sum1y // gcd(sum1x, sum1y))
    def __sub__(self, other):
        sub1x = self.x * other.y - self.y * other.x
        sub1y = self.y * other.y
        return fraction(sub1x // gcd(sub1x, sub1y), sub1y // gcd(sub1x, sub1y))
    def __str__(self):
        return '(' + str(self.x) + ';' + str(self.y) + ')'
    def __eq__(self, value):
        if (self.x / self.y) == (value.x / value.y): return True
        else: return False
    def __lt__(self, other):
        if (self.x / self.y) < (other.x / other.y): return True
        else: return False
    def __gt__(self, other):
        if (self.x / self.y) > (other.x / other.y): return True
        else: return False
print(fraction(1,2) - fraction(2, 3))
#git clone 