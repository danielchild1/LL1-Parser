class Factor:
    def __init__(self, **kwargs):
        if 'num' in kwargs:
            self.num = kwargs['num']
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'paren' in kwargs:
            self.paren = kwargs['paren']
            

class TermP:
    def __init__(self, **kwargs):
        if 'termP' in kwargs:
            self.termP = kwargs['termP']
        if 'factor' in kwargs:
            self.factor = kwargs['factor']
        if 'sym' in kwargs:
            self.sym = kwargs['sym']

class Term:
    def __init__(self, **kwargs):
        if 'termP' in kwargs:
            self.termP = kwargs['termP']
        if 'factor' in kwargs:
            self.factor = kwargs['factor']
        if 'sym' in kwargs:
            self.sym = kwargs['sym']

class ExprP:
    def __init__(self, **kwargs):
        if 'term' in kwargs:
            self.term = kwargs['term']
        if 'exprP' in kwargs:
            self.ExprP = kwargs['exprP']

class Expr:
    def __init__(self, **kwargs):
        if 'term' in kwargs:
            self.term = kwargs['term']
        if 'exprP' in kwargs:
            self.ExprP = kwargs['exprP']