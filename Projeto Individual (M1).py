# Dicionários para armazenar os resultados e candidatos
resultados = {}
candidatos = {}

# Funções para adicionar candidatos e resultados
def adicionar_candidato(candidatos, nome, notas):
    candidatos[nome] = notas

def adicionar_resultado(resultados, nome, resultado):
    resultados[nome] = resultado

# Menu principal
print('Verificar se candidato atende aos critérios')
print('\n')
print('Escolha uma opção abaixo: ')
print('\n')
opcao = input(' 1 - Cadastrar Candidato \n 2 - Exibir Nota \n 3 - Sair\n' )
print('\n\n')

while opcao in ['1', '2']:
    if opcao == '1':
        N = int(input("Quantos candidatos você deseja adicionar? "))
        print('\n\n')

        for i in range(N):
            nome = input(f"Digite o nome do candidato {i+1}: ")
            notas = []
            resultado = 'eX_tX_pX_sX'
            etapas = ['E(Entrevista)', 'T(Teste Teórico)', 'P(Teste Prático)', 'S(Avaliação de Soft Skill)']

            for j, etapa in enumerate(etapas):
                nota = input(f"Digite a nota da etapa {etapa}: ")
                notas.append(nota)
                resultado = resultado.replace('X', nota, 1)

            print('\n\n')
            adicionar_candidato(candidatos, nome, notas)
            adicionar_resultado(resultados, nome, resultado)

            for candidato, notas in candidatos.items():
                print(f' {candidato}: {notas}')
            print('\n\n')
        opcao = input(' 1 - Cadastrar Candidato \n 2 - Exibir Nota \n 3 - Sair \n \n' )

    elif opcao == '2':
        print('Informe a nota mínima para fazer a busca: ')
        E = int(input('Informe a nota da etapa de Entrevista: '))
        T = int(input('Informe a nota da etapa de Teste Teórico: '))
        P = int(input('Informe a nota da etapa de Teste Prático: '))
        S = int(input('Informe a nota da etapa de Avaliação de Soft Skill: '))
        print('\n\n')

        encontrou_candidato = False

        for candidato, notas in candidatos.items():
            notas_int = [int(nota) for nota in notas]
            if notas_int[0] >= E and notas_int[1] >= T and notas_int[2] >= P and notas_int[3] >= S:
                print(f'{candidato}: {resultados[candidato]}')
                encontrou_candidato = True

        print('\n\n')
        if not encontrou_candidato:
            print(' NADA ENCONTRADO, TENTE CADASTRAR UM ALUNO')
        opcao = input(' 1 - Cadastrar Candidato \n 2 - Exibir Nota \n 3 - Sair \n \n' )

print('CONSULTA ENCERRADA ')
