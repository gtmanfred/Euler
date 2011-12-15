def mmod(modulus):
    class M(long):
        def __pow__(self, p):
            return type(self)(long.__pow__(self, p, self.modulus))
        def __repr__(self): return 'M(%s %%%s)'% (long.__repr__(self), self.modulus)
        M.modulus = modulus
    return M
