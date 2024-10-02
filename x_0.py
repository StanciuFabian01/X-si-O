tabla = {1: '', 2: '', 3: '', 4: 'X', 5: '', 6: '', 7: '', 8: '', 9: ''}
print(f"{tabla[1]} | {tabla[2]} | {tabla[3]}\n---------\n{tabla[4]} | {tabla[5]} | {tabla[6]}\n---------\n{tabla[7]} | {tabla[8]} | {tabla[9]}")

"""
3 functii : verificare pe linie
    verificare pe coloana
    verificare pe diagonala
"""
def loc_liber(x):
    locuri_libere = {}
    for k,v in x.items():
        if v == '':
            locuri_libere.update({k: v})
    return locuri_libere

# lista_mare = []
def lista (joc):
    lista_1 = [joc[1], joc[2], joc[3]]
    lista_2 = [joc[4], joc[5], joc[6]]
    lista_3 = [joc[7], joc[8], joc[9]]
    lista_4 = [joc[1], joc[4], joc[7]]
    lista_5 = [joc[2], joc[5], joc[8]]
    lista_6 = [joc[3], joc[6], joc[9]]
    lista_7 = [joc[1], joc[5], joc[9]]
    lista_8 = [joc[3], joc[5], joc[7]]
    lista_mare = [lista_1, lista_2, lista_3, lista_4, lista_5, lista_6, lista_7, lista_8]
    return lista_mare

def poztii_favorabile(tabla):
    for j in "51379":
        if tabla[j] =='':
            tabla[j] = '0'
            break

# print(lista(tabla))
def check(tabla,par):
    for i in tabla:
        if '' in tabla[i]:
            if tabla[i][0] == tabla[i][1] == par:
                tabla[i][2] = '0'
                return tabla
            elif tabla[i][1] == tabla[i][2] == par:
                tabla[i][0] = '0'
                return tabla
            elif tabla[i][0] == tabla[i][2] == par:
                tabla[i][1] = '0'
                return tabla
            else:
                poztii_favorabile(tabla)

while '' not in tabla.values():
    input("Alege o pozitie")
    check(tabla,'x')


# jucator = "X"
# calculator = "0"




"""
1 2 3
4 5 6
7 8 9

lista_1=('1','2','3')
lista_2=('4','5','6')
lista_3=('7','8','9')
lista_4=('1','4','7')
lista_5=('2','5','8')
lista_6=('3','6','9')
lista_7=('1','5','9')
lista_8=('3','5','7')

"""






