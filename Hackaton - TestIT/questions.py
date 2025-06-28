perguntas = [
    "Qual a função usada para exibir algo na tela em Python?",
    "Como se comenta uma linha de código em Python?",
    "Qual palavra-chave define uma função em Python?",
    "Como você importa um módulo chamado 'math'?",
    "Qual a função do módulo 'time' que pausa a execução?",
    "Como gerar um número inteiro aleatório entre 1 e 10 com o módulo random?",
    "Qual função retorna o tamanho de uma lista em Python?",
    "Qual operador é usado para comparação de igualdade?",
    "Como obter o horário atual com o módulo time?",
    "Qual tipo de dado representa valores como True ou False?"
]

opcoes = [
    ["show", "echo", "print", "write"],                 # correta: 2
    ["--", "/* */", "#", "//"],                         # correta: 2
    ["function", "def", "define", "func"],              # correta: 1
    ["require math", "using math", "include math", "import math"],  # correta: 3
    ["pause()", "sleep()", "wait()", "delay()"],          # correta: 1
    ["choice(1, 10)", "range(1, 10)", "randint(1, 10)", "random(1, 10)"],     # correta: 2
    ["size()", "length()", "len()", "count()"],           # correta: 2
    ["=", "==", "===", "!="],                           # correta: 1
    ["localtime()", "datetime()", "clock()", "now()"],    # correta: 0
    ["int", "list", "bool", "str"]                      # correta: 2
]

respostas_certas = [2, 2, 1, 3, 1, 2, 2, 1, 0, 2]