# A estafuncion se le ingresa una lista de puntos en el plano y devuelve una lista de puntos que forman un poligono convexo con úntos en sentido horario
def graham(l):
  l.sort()
  Lupper = l[0:2]
  n = len(l)
  for i in range(2,n):
    Lupper.append(l[i])
    while (len(Lupper)>2 and turn(Lupper[-3],Lupper[-2],Lupper[-1]) != 'R'):
      Lupper.pop(-2)
    Llower = [l[-1],l[-2]]
  for i in range(-3,-n-1):
    Llower.append(l[i])
    while (len(Llower)>2 and turn(Llower[-3],Llower[-2],Llower[-1]) != 'R'):
      Llower.pop(-2)
  L = Lupper + Llower[1:-1]
  return L
