import math

def period(L,g):
     try:
          first= math.sqrt(L/g)
          squareroot= math.sqrt(int(first))
          tperiod= (2*math.pi*int(squareroot))
          return tperiod
     except ZeroDivisionError:
         return ('The value of gravity cannot be equal to zero.')

print(period(10,9.81))
print(period(5,0))
