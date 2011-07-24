class xlist(list):
    def len(self):
        return len(self)
    def add(self, *args):
        self.extend(args)
        return None
    def index(self,val):
        gen = (i for i,x in enumerate(self) if x == val)
        return list(gen)
