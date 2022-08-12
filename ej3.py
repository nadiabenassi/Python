#3)Con uso de ciclos de repeticion, imprimir los siguientes patrones:

"""a)

5 4 3 2 1
4 4 3 2 1
3 3 3 2 1
2 2 2 2 1
1 1 1 1 1"""
#No logro que me quede a la inversa...

rows = 5
for i in range(0, 5):
    for j in range(0, 5):
        if i > j:
            print(j+1, end=' ')
        else:
            print(i+1, end=' ')
    print("\r")

"""#b)
*
# #
* * *
# # # #
* * * * *"""
#no sale como esperaba

cant = 5
for i in range(0,5):
   print("*"*(i+1))
   print("#"*(i+1))

