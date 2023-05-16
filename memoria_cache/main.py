#  Criando a cache padrão
def inicializar_cache(tamanho_cache):
    #criando um dict vazio
    cache = {}
    #adicionando o valor -1 ate o tamanho indicado na função
    for key in range(0, tamanho_cache):
        cache[key] = -1

    return cache
#  Imprimindo a cache padrão
def imprimir_cache(dict):
    #printando o dict no console
    print('Tamanho da cache: ', len(dict))
    for key, value in dict.items():
        print(f'Posição cache || Posição memoria')
        print(f'       {key}      ||       {value} ')


def calcula_posicao(tamanho_cache, pos_memoria):
    pos_cache = pos_memoria % tamanho_cache
    return pos_cache

def calcula_hit_misses(pos_memoria, valor_cache, hit, misses, status):
    if pos_memoria == valor_cache:
        hit += 1
        status = 'Hit'
    else:
        misses += 1
        status = "Misses"
    return hit, misses, status


def mapeamento_direto(tamanho_cache, posicoes_memoria_acessar):
    #inicializando variaveis
    hits = 0
    misses = 0
    status = ''
    linha = 0

    #inicializando a cache
    cache = inicializar_cache(tamanho_cache)
    # imprimindo valores iniciais
    imprimir_cache(cache)

    for pos_memoria in posicoes_memoria_acessar:
        pos_cache = calcula_posicao(tamanho_cache, pos_memoria)
        valor_cache = cache[pos_cache]
        #calcula hit e misses
        hits, misses, status = calcula_hit_misses(pos_memoria, valor_cache, hits, misses, status)
        # todo só alterar se for misses
        cache[pos_cache] = pos_memoria
        # imprimindo valores
        print('-------------------------------------------')
        print('Linha ',linha, ' | posição da memoria desejada ', pos_memoria)
        print('Status: ', status)
        imprimir_cache(cache)

        linha += 1
    taxa_acerto = hits*100/(hits+misses)
    #informações hit e misses
    print("*-------------------------------------------*")
    print("Memórias acessadas: ", misses)
    print("Números de hits: ", hits)
    print("Números de misses: ", misses)
    print("Taxa de acertos (hits): ", taxa_acerto, "%")
    


#  ------------------------------------ codigo para mapeamento associativo por conjunto ------------------------------------ #

# def fifo(primeira_linha, tamanho_cache, pos_memoria):

#     linha_subs = calcula_posicao(tamanho_cache, pos_memoria)
#     return linha_subs


# def lru(ultimo_uso, tamanho_cache, pos_memoria):

#     linha_subs = calcula_posicao(tamanho_cache, pos_memoria)
#     return linha_subs


# def lfu(memoria_cache, qtd_conjuntos, posicao_memoria):

#   num_conjunto = int(posicao_memoria)%int(qtd_conjuntos)
#   lista_posicoes = get_lista_posicoes_cache_conjunto(memoria_cache,num_conjunto, qtd_conjuntos)

#   # descobrir dentro do conjunto qual posição da cache tem menos acesso
#   posicao_substituir = 0
#   if len(lista_posicoes) > 1:

#     if debug:
#       imprimir_contador_lfu()

#     # descobrir qual das posições é menos usada
#     lista_qtd_acessos = []
#     for qtd_acessos in lista_posicoes:
#       lista_qtd_acessos.append(contador_lfu[qtd_acessos])

#     posicoes_com_menos_acesso = min(lista_qtd_acessos)
#     candidatos_lfu = []

#     for qtd_acessos in lista_posicoes:
#       if contador_lfu[qtd_acessos] == posicoes_com_menos_acesso:
#         candidatos_lfu.append(qtd_acessos)

#     # para garantir ordem aleatória de escolha caso duas ou mais posições
#     # tenham o mesmo número de acessos
#     posicao_substituir = random.choice(candidatos_lfu)

#   # zera o número de acessos a posição que foi substituida
#   contador_lfu[posicao_substituir] = 0

#   # altera a posição de memória que está na cache
#   memoria_cache[posicao_substituir] = posicao_memoria


def chama_subs(tec_subs, tamanho_cache, pos_memoria, ultimo_uso, primeira_linha):
    if tec_subs == 1:
        fifo = fifo(primeira_linha, tamanho_cache, pos_memoria)
        return fifo
    if tec_subs == 2:
        lru = lru(ultimo_uso, tamanho_cache, pos_memoria)
        return lru
    if tec_subs == 3:
        lfu = lfu(tamanho_cache, pos_memoria)
        return lfu


# Criando a cache para o conjunto
def inicializar_cache_associativo(tamanho_cache, tamanho_bloco):
    #criando um dict vazio
    cache = {}
    #adicionando o valor -1 ate o tamanho indicado na função
    for key in range(0, tamanho_cache):
        cache[key] = -1

    return cache

#  Imprimindo a cache pro conjunto
def imprimir_cache_associativo(dict):
    #printando o dict no console
    print('Tamanho da cache: ', len(dict))
    for key, value in dict.items():
        print(f'Posição cache || Posição memoria')
        print(f'       {key}      ||       {value} ')


def mapeamento_associativo_por_conjunto(tamanho_cache, posicoes_memoria_acessar, tamanho_bloco, tec_subs):
    #inicializando variaveis
    hits = 0
    misses = 0
    status = ''
    linha = 0


    #inicializando a cache
    cache = inicializar_cache_associativo(tamanho_cache, tamanho_bloco)
    # imprimindo valores iniciais
    imprimir_cache_associativo(cache)

def retorna_tamanho_bloco():
    tamanho_bloco = 0
    dict_opcoes ={
        1: 1,
        2: 2,
        3: 4,
        4: 8,
        5: 16
    }
    print("Selecione a opção do tamanho do conjunto!")
    print("(1) 1 bloco | (2) 2 blocos | (3) 4 blocos | (4) 8 blocos | (5) 16 blocos")
    while tamanho_bloco not in dict_opcoes.values():
        try:
            tamanho_bloco = dict_opcoes[int(input("Digite a opção que deseja: "))]
        except:
            continue

    print(f'Tamanho selecionado: {tamanho_bloco} blocos')

    return tamanho_bloco

def retorna_tecnica_substituicao():
    tecnica_substituicao = 0
    dict_opcoes ={
        1: "LRU",
        2: "LFU",
        3: "FIFO"
    }
    print("Agora, selecione a opção da técnica de substituição que dejesa!")
    print("(1) LRU | (2) LFU | (3) FIFO")
    while tecnica_substituicao not in dict_opcoes.values():
        try:
            tecnica_substituicao = dict_opcoes[int(input("Digite a opção que deseja: "))]
        except:
            continue

    print(f'Técnica selecionada: {tecnica_substituicao}')

    return tecnica_substituicao

def main():
    #variaveis
    tamanho_cache = 5
    #lista com as posições que queremos acessar
    posicoes_memoria_acessar = [0,1,2,2,22,32,42,20,1,10,11,12,13]

    #tamanho do conjunto
    tamanho_bloco = retorna_tamanho_bloco()

    tecnica_substituicao = retorna_tecnica_substituicao()

    #chamando função mapeamento direto
    mapeamento_direto(tamanho_cache, posicoes_memoria_acessar)

    mapeamento_associativo_por_conjunto(tamanho_cache, posicoes_memoria_acessar, tamanho_bloco, tec_subs)

if __name__ == '__main__':
    main()