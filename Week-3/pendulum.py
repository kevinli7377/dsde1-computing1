import math

def period(L,g):
     #try:
          first= math.sqrt(L/g)
          tperiod= (2*math.pi*first)
          return tperiod
     #except ZeroDivisionError:
        #return ('The value of gravity cannot be equal to zero.')
     
          
print(period(3.3,9.81))
#print(period(5,0))
