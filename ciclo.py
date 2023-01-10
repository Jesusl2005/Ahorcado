import datos

def evaluacion(palabra, list_oculto):
    oportunidad = datos.oportunidad
    
    list_resultado = []
    for i in list_oculto:
        list_resultado.append('_')

    while (oportunidad != 0):
        resultado=''
        for n in list_resultado:
            resultado = resultado + n
        
        print(' ')
        print(f'Tienes {oportunidad} oportunidades para adivinar la palabra')
        print(' ')
        print(resultado)
        print(' ')

        eleccion_letra = input('Escoge una letra: ')
        eleccion_letra = eleccion_letra.lower()
        print(' ')
        print('*'*50)

        for i in range(0,len(palabra)):
            if eleccion_letra == list_oculto[i]:
                list_resultado[i] = list_oculto[i]
       
        oportunidad += -1
         
        if list_resultado == list_oculto:
            msj = True
            break
        else:
            msj = False 
    
    if msj == True:
        print(' ')
        print(f'CORRECTO LA PALABRA ES: {palabra}')
        print(' ')
        print('FELICIDADES GANASTE LA PARTIDA :)')
        print(' ')
        print('*'*50)
    else:
        print(' ')
        print('PERDISTE, VUELVE A INTENTARLO')
        print(' ')
        print(f'LA RESPUESTA ES: {palabra}')
        print(' ')
        print('*'*50)

