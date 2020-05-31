import random, time
class Advinha:
    def __init__(self):
        self.frases = ["Sim", "Não", "Não faço ideia", "Será mesmo?!"]
       
    def Iniciar(self):
         while True:
            frase = input(str("Qual sua dúvida? "))
            print("pensando...")
            time.sleep(3)
            self.Resposta() # self.Respota(self.frases)
            continuar = input(str("Deseja realizar outra pegunta? (S/N) "))
            if(continuar == 's'):
                pass
            else:
                print("Obrigado por usar o programa")
                break

    def Resposta(self):    #def Resposta(self, frasesp)
        print(random.choice(self.frases))   #choice(frasesp)

advinha = Advinha()
advinha.Iniciar()