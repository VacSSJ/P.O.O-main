
nota1 = float(input('Introdusca su nota: '))
nota2 = float(input('Introdusca su nota: '))
nota3 = float(input('Introdusca su nota: '))
nota4 = float(input('Introdusca su nota: '))
nota5 = float(input('Introdusca su nota: '))

promedio = nota1 + nota2 + nota3 + nota4 + nota5

print(f'suma total del promedio: {promedio}')

promedioFinal = promedio // 5

print({promedioFinal})

if promedioFinal >= 4.0:
    print('Usted Aprobo!!!!')
else:
    print('Usted Reprobo :C')