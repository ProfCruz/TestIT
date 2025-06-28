import questions

def aplicar_teste():
    resultado = []
    print("\nIniciando o teste...\n")
    
    i = 0
    while i < len(questions.perguntas):
        print(f"\nPergunta {i + 1}: {questions.perguntas[i]}")

        j = 0
        while j < 4:
            print(f"{j + 1}. {questions.opcoes[i][j]}")
            j += 1

        escolha = int(input("Sua resposta (1 a 4): "))  # Sem validação

        correta = (escolha - 1) == questions.respostas_certas[i]
        resposta_usuario = questions.opcoes[i][escolha - 1]
        resposta_certa = questions.opcoes[i][questions.respostas_certas[i]]

        resultado.append((questions.perguntas[i], resposta_usuario, resposta_certa, correta))
        i += 1

    return resultado

def avaliar_respostas(resultado):
    texto = "\nResultado do Teste:\n"
    corretas = 0

    i = 0
    while i < len(resultado):
        pergunta = resultado[i][0]
        resposta_usuario = resultado[i][1]
        resposta_certa = resultado[i][2]
        correto = resultado[i][3]

        if correto:
            texto += f"{i + 1}. {pergunta} - ✅ Correta\n"
            corretas += 1
        else:
            texto += f"{i + 1}. {pergunta} - ❌ Incorreta (Correta: {resposta_certa})\n"
        i += 1

    texto += f"\nTotal de acertos: {corretas} de {len(resultado)}"
    return texto, corretas
