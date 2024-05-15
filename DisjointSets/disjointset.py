class DisjointSet:
    def __init__(self, nb_of_items):
        self.ens = []
        for i in range(0,nb_of_items):
            self.ens.append(-1)

    def fin_rec(self, x):
        if self.ens[x] < 0:
            return x
        else:
            return self.find_rec(self.ens[x])

    def find(self, x):
        while self.ens[x] > 0:
            x = self.ens[x]
        return x

    def union(self, a, b):
        self.ens[b] = a

