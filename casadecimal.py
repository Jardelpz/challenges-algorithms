n = input('Número: ')

tam = len(n)
uni =0 
dez= 0
cent=0
mil=0

if(tam<2):
    uni=n
else:
    uni=n[-1]
    if (tam<3):
        dez=n[-2]
    else:
        dez=n[-2]
        if(tam<4):
            cent=n[-3]
        else:
            cent=n[-3] 
            if(tam<5):
                mil=n[-4]
#also works
# if(tam<2):
#     uni=n
# elif (tam<3):
#     uni=n[-1]
#     dez=n[-2]
# elif (tam <4):
#     uni=n[-1]
#     dez=n[-2]
#     cent=n[-3]
# elif (tam <5):
#     uni=n[-1]
#     dez=n[-2]
#     cent=n[-3]
#     mil=n[-4]


print(f'Unidade: {uni} \n Dezena: {dez} \n Centena: {cent} \n Unidade de Milhar: {mil}')