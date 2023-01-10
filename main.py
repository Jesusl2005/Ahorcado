import datos
import ciclo
def run():
    print('*'*50)
    print(' ')
    print('JUGUEMOS AL AHORCADO')
    print(' ')
    print('*'*50)
    print(' ')
    print('ADIVINA LA PALABRA')
    print(' ')
    print('*'*50)
    ciclo.evaluacion(datos.palabra, datos.list_oculto)

if __name__ == '__main__':
    run()