import sys

def sair():
    print("Obrigado por jogar! Até a próxima.")
    sys.exit(0)

def jogo_de_perguntas():
    pontuacao = 0

    # Defina suas perguntas e respostas corretas
    perguntas = [
        {
            "pergunta": "Qual é a capital do Brasil?",
            "opcoes": ["a) São Paulo", "b) Rio de Janeiro", "c) Brasília"],
            "resposta": "c"
        },
        {
            "pergunta": "Qual é o maior planeta do Sistema Solar?",
            "opcoes": ["a) Júpiter", "b) Saturno", "c) Terra"],
            "resposta": "a"
        },
        {
            "pergunta": "Quem pintou a Mona Lisa?",
            "opcoes": ["a) Leonardo da Vinci", "b) Vincent van Gogh", "c) Pablo Picasso"],
            "resposta": "a"
        }
    ]

    # Itera sobre as perguntas
    for pergunta in perguntas:
        print(pergunta["pergunta"])
        for opcao in pergunta["opcoes"]:
            print(opcao)

        resposta = input("Digite a letra correspondente à sua resposta: ")

        if resposta.lower() == pergunta["resposta"]:
            print("Resposta correta!")
            pontuacao += 1
        else:
            print("Resposta incorreta!")

    print("Fim do jogo!")
    print("Pontuação final:", pontuacao)

while True:
    print("Bem-vindo ao Jogo de Perguntas!")
    print("1. Iniciar jogo")
    print("2. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        jogo_de_perguntas()
    elif opcao == "2":
        sair()
    else:
        print("Opção inválida. Tente novamente.\n")
