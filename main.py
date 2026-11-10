#2-m
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

talaba1 = Talaba("Ali",18 )

print(talaba1.ism)

talaba1.ism = "Vali"
talaba1.yosh = 20

print(talaba1.ism)
print(talaba1.yosh)
