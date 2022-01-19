def mult (n) :
      return lambda x : x * n

x = mult(3)
print(x(4))