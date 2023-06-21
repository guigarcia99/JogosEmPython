def escolheJogo():
    print("********************************************")
    print("*********** Escolha o seu Jogo!! ***********")
    print("********************************************")

    print("(1) Forca")
    print("(2) Adivinhação")

    jogo=int(input(("O que você deseja jogar ? ")))

    if(jogo==1):
        print("Abrindo o jogo da Forca.")
        import Forca
        Forca.jogarForca()
    elif(jogo==2):
        print("Abrindo o jogo da Adivinhação.")
        import AdivinhacaoFOR
        AdivinhacaoFOR.jogarAdivinhacao()
    else:
        print("Por favor selecione uma opção válida.")
        escolheJogo()

escolheJogo()