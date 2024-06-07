NombreUsuario = input('Un gusto en conocerte. Como te llamas? ')
edadUsuario = int(input('Cuanto años tienes? '))
edad = int(input('Ingrese la edad: '))

print(f'Encantado en conocerte {NombreUsuario}.')
print(f'El Proximo año cumpliras {edadUsuario + 1}')

if edad > edadUsuario:
    print('XDXDXDXD soy mayor que tu....')
elif edad < edadUsuario:
    print('Ohhh que lamentable... eres mayor que yo')
else:
    print('Mira que divertido tenemos la misma edad...')
