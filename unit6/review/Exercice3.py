class strplus(str, object):
    def __lshift__(self, other):
        self += str(other)
        return self

    def __sub__(self, other):
        self = self.replace(other, '')
        return self

    def __invert__(self):
        self = self[len(self)::-1]
        return self

texto = strplus('algo')
print(texto) # 'algo'
texto = texto << ' mas'
print(texto) # 'algo mas'
texto = texto - 'as'
print(texto) # ''algo m'
print(~texto) # 'm ogla'