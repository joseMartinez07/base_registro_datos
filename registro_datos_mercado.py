def AGREGAR(pa, cod, nom, pre, inv):
    if cod in pa:
        print("ERROR")
    else:
        pa[cod] = [nom, pre, inv]
        complemento(pa)
    return pa

def ACTUALIZAR(pa, cod, nom, pre, inv):
    if cod in pa:
        pa[cod] = [nom, pre, inv]
        complemento(pa)
    else:
        print("ERROR")

    return pa

def BORRAR(pa, cod, nom, pre, inv):
    if cod in pa:
        del(pa[cod])
        complemento(pa)
    else:
        print("ERROR")
    return pa

def complemento(pa):
    c = len(pa)
    valm = 0
    nvalm = ""
    valc = pa[1][1]
    nvalc = ""
    valpro = 0
    valinv = 0
    for articulo in pa:
        if valm >= pa[articulo][1]:
            valm = valm
        else:
            valm = pa[articulo][1]
            nvalm = pa[articulo][0]
        if valc <= pa[articulo][1]:
            valc = valc
        else:
            valc = pa[articulo][1]
            nvalc = pa[articulo][0]
        valpro = valpro + pa[articulo][1]
        valinv = valinv + ((pa[articulo][1]) * (pa[articulo][2]))
    valpro = (valpro / (c))
    valpro = round(valpro, 1)
    print(nvalm, nvalc, valpro, valinv)
    return

pa = {1: ['Manzanas', 6000, 25],
      2: ['Limones', 2500, 15],
      3: ['Peras', 2700, 33],
      4: ['Arandanos', 9300, 34],
      5: ['Tomates', 2100, 42],
      6: ['Fresas', 4100.0, 10],
      7: ['Helado',4500, 41],
      8: ['Galletas', 500, 8],
      9: ['Chocolates', 4500, 80],
      10: ['Jamon', 15000, 10]}

a = input()
b = input()
dato = b.split()

if a == 'AGREGAR':
    AGREGAR(pa, int(dato[0]), dato[1], int(dato[2]), int(dato[3]))

elif a == 'ACTUALIZAR':
    ACTUALIZAR(pa, int(dato[0]), dato[1], int(dato[2]), int(dato[3]))

elif a == 'BORRAR':
    BORRAR(pa, int(dato[0]), dato[1], int(dato[2]), int(dato[3]))
