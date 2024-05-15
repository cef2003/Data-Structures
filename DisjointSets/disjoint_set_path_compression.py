class DisjointSetPathCompression:
    def __init__(self, nb_items):
        self.ens = []
        for i in range(0, nb_items):
            self.ens.append(-1)

    def find_rec(self, x):
        if self.ens[x] < 0:
            return x
        else:
            return self.find_rec(self.ens[x])

    def find(self, x):
        while self.ens[x] > 0:
            x = self.ens[x]
        return x

    def find_path_compression(self, a):
        while self.ens[a] > 0:
            b = self.ens[a]
            if self.ens[b] > 0:
                self.ens[a] = self.ens[b]
            a = b
        return a

