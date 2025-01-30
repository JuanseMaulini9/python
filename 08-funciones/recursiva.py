print("*** Funcion recursiva ***")

def recursiva(n):
  if n == 1 : 
    print(n)
  else:
    recursiva(n-1)
    print(n)
  
recursiva(5)