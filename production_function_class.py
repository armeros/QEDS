class Production:
    def __init__(self, K=0, L=0, α=0.33, A=1):
        self.K, self.L, self.α, self.A = K, L, α, A
    
    def cobb_douglas(self, K=0, L=0, α=0.33, A=1):
        self.K, self.L, self.α, self.A = K, L, α, A  
        return self.A*self.K**self.α*self.L**(1-self.α)
    
    def returns_to_scale(self, γ):
        y1 = self.cobb_douglas(self.K, self.L)
        y2 = self.cobb_douglas(γ*self.K, γ*self.L)
        return y2/y1/γ
    
    def MP_num(self, increment=1e-10):
        K, L, α, A = self.K, self.L, self.α, self.A
        MPL = (self.cobb_douglas(K, L + increment) - self.cobb_douglas(K, L)) / increment
        MPK = (self.cobb_douglas(K + increment, L) - self.cobb_douglas(K, L)) / increment
        return MPL, MPK
    
    def MP_diff(self):
        K, L, α, A = self.K, self.L, self.α, self.A
        MPK = A*α*(K/L)**(α-1)
        MPL = (1-α)*A*(K/L)**α
        return MPL, MPK
    
if __name__=="_main__":
    F = Production()
    F.cobb_douglas(1.0, 0.5)
    print(F.MP_num())
    print(F.MP_diff())
