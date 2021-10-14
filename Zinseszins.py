import random

class compoundInterst():
    def __init__(self,startcap, return_on_cap, volatility, savings, time):
        self.startcap = startcap
        self.kapInvested = startcap
        self.endcap = startcap
        self.return_on_cap = return_on_cap # in %
        self.savings = savings * 12 # savings p.a
        self.time = time # in years
        self.volatility = volatility # volatility in %
        self.min_return_on_cap = int(return_on_cap - volatility)
        self.max_return_on_cap = int(return_on_cap + volatility)

    def calc_endcap_randomized(self):
        for t in range(self.time):
            self.kapInvested += self.savings
            self.endcap = (self.endcap + self.savings) * (1 + (random.randrange(self.min_return_on_cap,self.max_return_on_cap)/100))

    def calc_endcap(self):
        for t in range(self.time):
            self.kapInvested += self.savings
            self.endcap = (self.endcap + self.savings) * (1 + (self.return_on_cap/100))

    def get_endcap(self):
        return round(self.endcap,2)

    def get_cap_invested(self):
        return round(self.kapInvested,2)

v1 = [11000,11,12,500,10]
v2 = [11000,8,17,500,10]
# startcap,ren,vola,savings,time

compare = [v1,v2]
num = 100000 # number cases
solutions = []

for v in compare:
    for n in range(num):
        solution = compoundInterst(v[0],v[1],v[2],v[3],v[4])
        solution.calc_endcap_randomized()
        endcap = solution.get_endcap()
        solutions.append(endcap)

    minendcap = min(solutions)
    maxendcap = max(solutions)
    medendcap = round((minendcap+maxendcap)/2,2)

    print("max Capital:",maxendcap)
    print("med Capital:",medendcap)
    print("min Capital:",minendcap)
    print()

    solutions.clear()