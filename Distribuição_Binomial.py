# by Gabriel Aristimunho
# UFMS 06/04/2022
# desconsiderem meu erros de portugues, to fazendo Biologia, não Letras

import time
import os
import random

#Lista de frases para a mensagem de Erro
print("by gabriel aristimunho \n"
      "\n"
      "Distribuição Binomial\n"
      "esse programa possui algumas regras bem elegantes:\n"
      "1° regra: os valores devem ser digitados corretamente, sem espaços\n"
      "2° regra: nos valores decimais, substitua a vírgula ( , ) por ponto ( . )\n"
      "3° regra: se o programa perguntar como a guerra nuclear de 2043 se iniciou,\n"
      "feche-o e queime seu computador imediatamente\n"
      "\n"
      "lembre-se:\n"
      "N: números de tentativas\n"
      "K: números de sucesso da amostra\n"
      "Ps: probabilidade de sucesso, no qual deve ser preenchido em forma de fração. ex:\n"
      "    20%  >>  1/5    ou   75% >> 6/8   etc.. \n"
      "    o preenchimento terá o campo para o numerador e o denominador;\n"
      "Pi: probabilidade de insucesso ((1-Ps) elevado a K):\n"
      "    é algo bem simples também, se por exemplo Ps = ¼ , então Pi = ¾\n"
      "    o preenchimento terá o campo para o numerador e o denominador;\n"
      "\n"
      "os resultados irão mostrar parte do processo de cálculo além do resultado final em porcentagem\n")
time.sleep(0.3)
print('_____________________________________________________________________________________________')
time.sleep(0.3)
input('|Pressione Enter para continuar|')

def inicio():
    while True:
        try:
            print('\nAdicione os valores')
            N = float(input('N: '))
            K = float(input('K: '))

            # valores de Ps (Sucesso)

            print('Digite os valores de Ps:')
            numeradorPs = int(input('numerador:   '))
            print('          --------')
            denominadorPs = int(input('denominador: '))
            Ps = numeradorPs / denominadorPs
            print('Ps:', numeradorPs, '/', denominadorPs)

            # valores de Pi (Inssucesso)
            print('\nAgora digite os valor de Pi:')
            numeradorPi = int(input('numerador:   '))
            print('          --------')
            denominadorPi = int(input('denominador: '))
            Pi = numeradorPi / denominadorPi
            print('Pi:', numeradorPi, '/', denominadorPi)


            def factorial(n):
                return 1 if (n == 1 or n == 0) else n * factorial(n - 1)

            N_fatorial = N
            print("{}! é igual a: ".format(N), factorial(N_fatorial))

            K_fatorial = K
            print("{}! é igual a: ".format(K), factorial(K_fatorial))

            #montagem da formula
            n_k = N - K
            trecho_1 = factorial(N_fatorial) / (factorial(K_fatorial) * factorial(n_k))
            print('\n        {}!'.format(N))
            print('___________________')
            print(K,'! x (', N,'-',K,')!\n')
            print(trecho_1)
            trecho_2 = Ps ** K
            print('\nPs: {:.4f}'.format(trecho_2))
            trecho_3 = Pi ** n_k
            print('Pi: {:.4f}'.format(trecho_3))
            resultado = trecho_1 * trecho_2 * trecho_3
            print('Resultado: {:.4f}\n'.format(resultado))
            print('Percentual: {:.4f}'.format(resultado * 100))
            time.sleep(1)
            print('\n_____________________________________________________________________________________________')

            pergunta = input('Tentar novamente? S/N\n:').upper()

            if pergunta == 'N' or pergunta == 'NAO' or pergunta == 'NãO':
                time.sleep(1)
                break
            elif pergunta == 'S' or pergunta == 'SIM':
                print('\nReiniciando...')
                time.sleep(1)
                os.system('cls')
                inicio()
                continue

        except ValueError:
            n = random.randint(1, 5)
            if n == 1:
                print("Acho que vc digitou errado, vai de novo")
            elif n == 2:
                print("Calma, respira, voce colocou alguma coisa errada")
            elif n == 3:
                print("O valor que vc digitou é invalido, tenta de novo")
            elif n == 4:
                print("Cuidado na hora de digitar, tenta de novo")
            elif n == 5:
                print("Tenta digitar com calma, vc colocou algo errado")

inicio()
#feito com Python 3.8
# pyinstaller --onefile .\PycharmProjects\Base004\Estudos\Distribuição_Binomial.py