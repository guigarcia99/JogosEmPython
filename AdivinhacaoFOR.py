import random
def jogarAdivinhacao():
    print("********************************************")
    print("** Seja bem vindo ao jogo da Adivinhação! **")
    print("********************************************")

    numeroTentativas=0
    numeroSecreto = random.randrange(1, 26)

    print("Selecione seu nível de dificuldade:")
    print("(1) Fácil || (2) Médio || (3) Difícil")
    nivel=int(input("De 1 a 3, digite seu nível:"))

    if(nivel==1):
        numeroTentativas=10
    elif(nivel==2):
        numeroTentativas=5
    elif(nivel==3):
        numeroTentativas=2
    else:
        print("Por favor escolha uma opção válida.")

    #Início do laço----------------------
    for rodada in range(1,numeroTentativas+1):
        print("Tentativa {} de {} totais.".format(rodada, numeroTentativas))
        chute=int(input("Digite o seu número de 1 a 25: "))

        if(chute<1 or chute>25):
            print("Por favor, digite apenas números de 1 a 25.")
            continue

        acertou=numeroSecreto == chute
        maior=chute>numeroSecreto
        menor=chute<numeroSecreto

        if(acertou):
            print("Parabéns! Você acertou!!!")
            break
        elif(maior):
            print("Você errou! Tente um número mais baixo.")
        elif(menor):
            print("Você errou! Tente um número mais alto.")
    #Fim do laço--------------------------

    print("********************************************")
    print("******* Fim de jogo. O número era", numeroSecreto,".*******")
    print("********************************************")

if(__name__=="__main__"):
    jogarAdivinhacao()