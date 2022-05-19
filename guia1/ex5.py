from operator import truediv


palabra = str(input("escriba una poalabra para saber si es palindrome o no: "))
if str(palabra) == str(palabra)[::-1] :
    print(palabra," es ",True)
else:
    print(palabra," es ",False)