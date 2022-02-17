import math
def score(x, y):
    radius = math.sqrt(x*x + y*y)
    if radius<=1:
        score=10
    elif radius<=5:
        score=5
    elif radius<=10:
        score=1
    else:
        score=0
        return score
  
 