import random
palabras = ['jesus', 'maria', 'esternocleidomastoideo', 'juan', 'ajedrez', 'matematicas', 'simple', 'noche', 'dia', 'martin', 'dinosaurio', 'almendra'
, 'caballo', 'vaca', 'arte', 'universidad', 'cine']

palabra = random.choice(palabras)

n = len(palabra)

oportunidad = n+4

list_oculto = []
for z in palabra:
    list_oculto.append(z)
