import string


nf = int(input("filas: "))
nc = int(input("columnas: "))
ca = str(input("coloque con que caracter quiere hacerlo: "))


for i in range (1,nf+1):
    for j in range (1,nc+1):
        print(ca,end=" ")
    print(" ")    