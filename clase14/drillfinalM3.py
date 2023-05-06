nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking","Messi", "Teller", "Einstein", "Pele", "Juanes"]
magos = []
cientificos = []
otros = []


for nombre in nombres  :
    if nombre == 'Harry Houdini' or nombre == 'David Blaine' or nombre == 'Teller':
        magos.append(nombre)
    elif nombre == 'Newton' or nombre == 'Hawking' or nombre == 'Einstein':
        cientificos.append(nombre)
    else:
        otros.append(nombre)

def imprime_listas (nombres, magos,cientificos, otros):
    imprimir_nombres(nombres)
    print("Magos: ", end="\n")
    for mago in magos:        
        print(mago, end="\n")
    print("Cientificos:", end="\n")
    for x in cientificos:        
        print(x, end="\n")
    print("Otros:", end="\n")
    for y in otros:        
        print(y, end="\n")
    

def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre, end="\n")

 
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]
        continue
    print(magos, end="\n")




imprimir_nombres(nombres)
print("################")
imprime_listas(nombres, magos, cientificos, otros)
print("################")
hacer_grandioso(magos)