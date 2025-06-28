# main.py
import time
import test

def main():
    print("=== TESTE DE CONHECIMENTOS EM PYTHON ===\n")
    nome = input("Digite seu nome: ").strip()
    print(f"\nOlá, {nome}! Você responderá 10 perguntas de escolha múltipla.\n")

    input("Pressione Enter para iniciar o teste...")
    inicio = time.time()

    resultado = test.aplicar_teste()

    fim = time.time()
    tempo_total = fim - inicio

    texto_resultado, acertos = test.avaliar_respostas(resultado)
    print(texto_resultado)
    print(f"\nTempo total: {tempo_total:.2f} segundos")
    print(f"Obrigado por participar, {nome}!")


main()
