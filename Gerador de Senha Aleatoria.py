#GERADOR DE SENHA ALEATÓRIA

from MinhasFunções.texto import titulo,linha,cronometro,alfabeto
from random import randint
titulo('GERADOR DE SENHAS ALEATORIA','\033[1;93m')


#PERGUNTAR QUANTOS CARACTERES O USUARIO QUER
qnt = int(input('\033[1;97mDESEJA GERAR UMA SENHA COM QUANTOS CARACTERES: \033[m'))
linha('\033[1;93m',20)

#PERGUNTAR E VERIFICAR SE ELE DESEJA TER NUMEROS EM SUA SENHA,VERIFICAR SE CONTÉM A RESPOSTA INSERIDA
n = str(input('DESEJA TER \033[1;93mNUMEROS\033[m'
              ' EM SUA SENHA: \033[1;93m[S/N]\033[m: ')).upper()[0]
cronometro(6,'RESPOSTA VERIFICADA!!','\033[1;93m')
#TEMPOZINHO PARA DA AQUELE CHARME

#VERIFICAR SE A RESPOSTA FOI INSERIDA CORRETAMENTE
if n not in 'SN':
    while n not in 'SN': #LOOP PARA RECEBER APENAS RESPOSTAS CORRETAS
        print(f'\033[1;91mERRO!! VERIFIQUE A RESPOSTA (S/N) E TENTE NOVAMENTE!!\033[m')
        n = str(input('DESEJA TER \033[1;93mNUMEROS\033[m'
                      ' EM SUA SENHA: \033[1;93m[S/N]\033[m: ')).upper()[0]
print(f'\033[1;92mRESPOSTA ENVIADA COM SUCESSO!!!')
linha('\033[1;92m',20)

#VERIFICAR SE O USUARIO DESEJA TER STRINGS EM SUA SENHA
string = str(input('DESEJA TER \033[1;93mLETRAS\033[m EM SUA SENHA: \033[1;93m[S/N]\033[m: ')).upper()[0]
cronometro(6,'RESPOSTA VERIFICADA!!','\033[1;93m')

#VERIFICAR SE FOI INSERIDA UMA RESPOSTA CORRETA
if string not in 'SN':
    while string not in 'SN': #LOOP PARA RECEBER APENAS RESPOSTAS CORRETAS
        print(f'\033[1;91mERRO!! VERIFIQUE A RESPOSTA (S/N) E TENTE NOVAMENTE!!\033[m')
        string = str(input('DESEJA TER \033[1;93mLETRAS\033[m'
                           ' EM SUA SENHA: \033[1;93m[S/N]\033[m: ')).upper()[0]
print(f'\033[1;92mRESPOSTA ENVIADA COM SUCESSO!!!')
linha('\033[1;92m',20)

#IMPORTEI UMA LISTA DA FUNÇÃO "ALFABETO"
alfabet = alfabeto()

#CRIEI UMA LISTA GLOBAL DA NOSSA SENHA
senhaList = []

#CASO O USUARIO NÃO DESEJE NENHUMA SENHA
if n in 'N' and string in 'N':
    print(f'\033[1;34mVOCÊ NÃO DESEJA NENHUMA SENHA? QUE PENA!!!\033[m')

#CRIANDO SENHA COM AMBOS OS 2 ('NUMEROS E LETRAS')
elif n in 'S' and string in 'S':
    for c in range(1,qnt+1): #COLOCAR OS CARACTERES DE ACORDO COM A QUANTIDADE PEDIDA
        randN = randint(0,9)
        randS = randint(0,25)

        if len(senhaList) == 0:#CRIEI UMA VARIAVEL PARA OBTER UMA POSIÇÃO RANDOM
            posRandom = 0
        else:
            posRandom = randint(0,len(senhaList) - 1)

        letra = alfabet[randS] #PEGUEI UMA POSIÇÃO ALEATÓRIA PARA A LISTA "ALFABETO"
        senhaList.insert(posRandom,randN)
        if len(senhaList) < qnt: #USEI ESSA CONDIÇÃO PARA NÃO PASSAR OS CARACTERES
            senhaList.insert(posRandom,letra)
        else:
            break

#CRIANDO SENHA COM APENAS NUMEROS
elif n in 'S' and string in 'N':
    for c in range(1,qnt+1):
        randN = randint(0,9)
        if len(senhaList) == 0:  # CRIEI UMA VARIAVEL PARA OBTER UMA POSIÇÃO RANDOM
            posRandom = 0
        else:
            posRandom = randint(0, len(senhaList) - 1)
        senhaList.insert(posRandom,randN)

#CRIANDO SENHA COM APENAS LETRAS
else:
    for c in range(1,qnt+1):
        randS = randint(0,25)
        letraAleatoria = alfabet[randS] #VARIAVEL DE LETRA ALEATORIA

        if len(senhaList) == 0:  # CRIEI UMA VARIAVEL PARA OBTER UMA POSIÇÃO RANDOM
            posRandom = 0
        else:
            posRandom = randint(0, len(senhaList) - 1)
        senhaList.insert(posRandom,letraAleatoria)

linha('\033[1;93m',20)
#CRIANDO UMA VARIAVEL PARA NOSSA SENHA APENAS PARA AS REPOSTAS QUE NÃO TEVE OS 2 NÃOS
if n in 'S' or string in 'S':
    cronometro(5, 'SENHA CRIADA COM SUCESSO!!!', '\033[1;97m')
    print(f'\033[1;93mSUA SENHA ALEATÓRIA É : ', end='')
    for c in senhaList:
        print(c,end='')
    print()



#DESPEDIDA E AGRADECIMENTO
titulo(f'MUITO OBRIGADO!!! ATÉ A PROXIMA','\033[1;93m')

