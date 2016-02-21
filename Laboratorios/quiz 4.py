class Perro:
    def __init__(self,puntos_vida=0,puntos_alegria=0):
        self.puntos_vida = puntos_vida
        self.puntos_alegria = puntos_alegria

    def caminar(self):
        self.puntos_vida-=2
        self.puntos_alegria+=1

    def correr (self):
        self.puntos_vida-=4
        self.puntos_alegria+=3

    def dormir(self):
        self.puntos_vida+=1
        self.puntos_alegria+=3

    def jugar (self):
        self.puntos_vida-=3
        self.puntos_alegria+=4

    def comer(self):
        self.puntos_vida+=5
        self.puntos_alegria+=1

contador=0
lassie=Perro(5,5)
while contador!=10:
    lassie.dormir()
    if lassie.puntos_vida==0:
        print("murio")
        break
    else:
        contador+=1

    lassie.jugar()
    if lassie.puntos_vida==0:
        print("murio")
        break
    else:
        contador+=1
    lassie.comer()
    if lassie.puntos_vida==0:
        print("murio")
        break
    else:
        contador=+1
    lassie.jugar()
    if lassie.puntos_vida==0:
        print("murio")
        break
    else:
        contador=+1
    lassie.caminar()
    if lassie.puntos_vida==0:
        print("murio")
        break
    else:
        contador=+1
    lassie.dormir()
    if lassie.puntos_vida==0:
        print("murio")
        break
    else:
        contador=+1
    lassie.correr()
    if lassie.puntos_vida==0:
        print("murio")
        break
    else:
        contador=+1
    lassie.dormir()
    if lassie.puntos_vida==0:
        print("murio")
        break
    else:
        contador=+1
    lassie.dormir()
    if lassie.puntos_vida==0:
        print("murio")
        break
    else:
        contador=+1
    lassie.comer()
    if lassie.puntos_vida==0:
        print("murio")
        break
    else:
        contador=+1
if contador==10:
    print("vive lassie")
else:
    print("lamentablemente murio lassie")




