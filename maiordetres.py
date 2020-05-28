a = int(input('Número: '))
b = int(input('Número: '))
c = int(input('Número: '))


maior=0
meio=0
menor=0

if(a>b):
    if(a>c):
        maior=a
        if(b>c):
            meio=b
            menor=c
        else:
            meio=c
            menor=b
    else:
        maior=c
        meio=a
        menor=b
elif(b>c):
    maior=b
    if(c>a):
        meio=c
        menor=a
    else:
        meio=a
        menor=c  
else:
    maior=c
    if(b>a):
        meio=b
        menor=a
    else:
        meio=a
        menor=b
if(maior==menor==meio):
    print("Números iguais")
print(maior,meio,menor)