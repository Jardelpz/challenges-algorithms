n = int(input('Número: '))
cont = 0
for i in range(2,n):
   if(n%i==0):
       cont+=1
else:
    if(cont>0):
        print("Não é primo") 
    else:
        print("É primo")             