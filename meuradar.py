vel = int(input('Velocidade registrada: '))
velMax = 80

if vel <= velMax:
    print('Não houve multa')
elif vel <= (velMax+10):
    print('Multado infração leve')
elif vel <= (velMax+20): # Funciona igual a vel > (velMax+11) and vel <= (velMax+20):
    print('Multado infração grave')
else:
    print('Multado infração gravissima')
