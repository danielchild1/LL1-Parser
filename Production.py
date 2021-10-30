class Production:
    
    def __init__(self, **kwargs):
        self.productions = []
        self.lSide = kwargs['lSide']
        for key in kwargs:
            if key != 'lSide':
                self.productions.append(kwargs[key])

    def append(self, **kwargs):
        self.lSide = kwargs['lSide']
        for key in kwargs:
            if key != 'lSide':
                self.productions.append(kwargs[key])
    
    def regurgitate(self):
        thing2Return = []
        for el in reversed(self.productions):
            thing2Return.append(el)
        return thing2Return
    
    def __int__(self):
        return len(self.productions)
    
    def __len__(self):
        return len(self.productions)
    
    def __str__(self):
        return self.lSide
    
    def __getitem__(self, key):
        return self.productions[key]


# def findProduction(name):
#     for o in ProList:
#         if o.lSide == name:
#             return o