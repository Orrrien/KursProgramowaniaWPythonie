from random import random as r

punkty_w_kole = 0
wszystkie_punkty = 1000000

for i in range(wszystkie_punkty):
    x = r()
    y = r()
    suma_kw = x*x + y*y
    if suma_kw <= 1:
        punkty_w_kole += 1

pi = 4*punkty_w_kole/wszystkie_punkty
print(pi)