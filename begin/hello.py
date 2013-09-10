def imprimir(a):
    print a
    print a[0:4]
    #Espera presionar tecla
    raw_input()

def lista():
    l = ["a", "b", 2, [1, 2]]
    print l[0]
    print l[3][0]

def dic():
    d = { 1 : "Nayda",
          2 : "Carol",
          3 : "Carlos"}
    print d[2]
    k = d.keys()
    for item in k:
        print d[item]

def bucles():
    while True:
        entrada = raw_input("> ")
        if entrada == "adios":
            break
        else:
            print entrada

    secuencia = ["uno", "dos", "tres"]
    for elemento in secuencia:
        print elemento

def imp(texto, veces = 1):
    print veces * texto

def sumar(x, y):
    return x + y

def varios(param1, param2, *otros):
    for val in otros:
        print val
    varios(1, 2)
    varios(1, 2, 3)
    varios(1, 2, 3, 4)
