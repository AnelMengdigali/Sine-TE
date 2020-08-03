
def sine( x ) :
   s = 0
   t = x  # current term. 
   i = 1  # index of current term

   while True:
      if s + t == s :
         return s
      s = s + t  

      t = - t * x * x / ( i + 1 ) / ( i + 2 )
      i = i + 2

