campos = ['NOMBRE', 'facilidad en publico', 'Abrirse a otros', 'Diplomacia', 'Persuasión',
          'Dirigir', 'Resposabilidad', 'Organización', 'Visión', 'Confiaza en si mismo',
          'Mentalidad independiente', 'Creatividad', 'Autonómia', 'Control del estres',
          'Reactividad', 'Paciencia', 'Respeto a la autoridad', 'Determinación', 'Ambición',
          'Esfuerzo', 'Competitividad']
cuarto = [['Isaac', 4, 5, 4, 6, 2, 7, 5, 6, 3, 7, 9, 8, 7, 4, 7, 6, 3, 5, 4, 6],
          ['Milton', 2, 5, 4, 4, 10, 8, 6, 6, 8, 4, 8, 1, 6, 3, 5, 3, 9, 4, 6, 6],
          ['Jesus', 5, 4, 8, 7, 4, 6, 5, 10, 6, 4, 6, 6, 2, 1, 5, 7, 6, 7, 4, 7],
          ['Enrique', 4, 8, 5, 7, 5, 7, 6, 8, 3, 5, 6, 2, 5, 4, 3, 7, 5, 7, 6, 4]]

segundo = [['Said', 8, 5, 5, 6, 3, 4, 8, 1, 6, 10, 5, 5, 4, 3, 7, 6, 5, 3, 6, 8],
           ['Levik', 6, 4, 4, 3, 5, 1, 3, 7, 8, 7, 8, 8, 5, 9, 7, 3, 8, 3, 7, 4],
           ['Alberto', 8, 8, 5, 5, 3, 7, 3, 4, 6, 3, 7, 2, 9, 7, 5, 4, 7, 6, 5, 7],
           ['Ricardo', 3, 3, 5, 8, 8, 4, 9, 7, 6, 7, 5, 9, 2, 4, 6, 3, 4, 4, 7, 6],
           ['Rosendo', 6, 2, 5, 4, 5, 6, 9, 6, 6, 4, 3, 3, 8, 5, 3, 7, 5, 6, 8, 7],
           ['Hiram', 8, 9, 8, 5, 3, 5, 5, 4, 3, 1, 7, 2, 6, 8, 7, 8, 5, 6, 2, 5]]


'''for a in range(4):
    for b in range(21):
        print(campos[b], ' ', cuarto[a][b])'''
cuar = 2
sega = 1
segb = 3
print(cuarto[cuar][0], ' + ', segundo[sega][0], ' + ', segundo[segb][0])
print(segundo[0][0])
for d in range(1, 20):
    total = ((cuarto[cuar][d]) + (segundo[sega][d] + segundo[segb][d]))/ 3
    print(campos[d], ' ', total)
