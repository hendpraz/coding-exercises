from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return { 'name' : self.name, 'score' : self.score }
        
    def comparator(a, b):
        if(b.score == a.score):
            if(a.name > b.name):
                return 1
            else:
                return -1
        else:
            if(a.score > b.score):
                return -1
            else:
                return 1

