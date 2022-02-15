# disjoint-set forests using union-by-rank and path compression(sort of)
class Uni_elt:
    def __init__(self,star=0,p=0,size=0):
        self.star= star
        self.p = p
        self.size = size

class Universe:
    def __init__(self,elements):
        self.num = elements
        self.elts = [Uni_elt(star=0,p=i,size=1) for i in range(elements)]

    def join(self,x,y):
        if(self.elts[x].rank > self.elts[y].star):
            self.elts[y].p = x
            self.elts[x].size += self.elts[y].size
        else:
            self.elts[x].p = y
            self.elts[y].size += self.elts[x].size
            if self.elts[x].star == self.elts[y].star:
                self.elts[y].star += 1
        self.num -= 1
    def size(self,x):
        return self.elts[x].size

    def nu_sets(self):
        return self.num

    def find(self,x):
        y = x
        while(y != self.elts[y].p):
            y = self.elts[y].p
        self.elts[x].p = y
        return y



