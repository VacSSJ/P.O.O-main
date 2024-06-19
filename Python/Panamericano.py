medallas = {}
for i in range(10):
    pais = input(f'Coloque el país {i + 1}: ')
    medallas[pais] = {'oro': 0, 'plata': 0, 'bronce': 0}

for pais, medallasPais in medallas.items():
    for medalla in ['oro', 'plata', 'bronce']:
        cantidad = int(input(f'País {pais} medallas {medalla}: '))
        medallasPais[medalla] = cantidad

    totalPais = sum(medallasPais.values())
    print(f'País {pais} medallas: {medallasPais}')
    print(f'Total de medallas para el país {pais}: {totalPais}')
    print()

totalMedallas = sum(sum(medallasPais.values()) for medallasPais in medallas.values())
print(f'Total de medallas entregadas: {totalMedallas}')