#  Criando a cache padrão
def inicializar_cache(tamanho_cache):
    # criando um dict vazio
    cache = {}
    # adicionando o valor -1 ate o tamanho indicado na função
    for key in range(0, tamanho_cache):
        cache[key] = -1
    return cache


#  Imprimindo a cache padrão
def imprimir_cache(dict):
    # printando o dict no console
    print('Tamanho da cache: ', len(dict))
    for key, value in dict.items():
        print(f'Posição cache || Posição memoria')
        print(f'       {key}      ||       {value} ')


def calcula_posicao(tamanho_cache, pos_memoria):
    pos_cache = pos_memoria % tamanho_cache
    return pos_cache

def calcula_hit_misses(pos_memoria, valor_cache, hit, miss, status):
    if pos_memoria == valor_cache:
        hit += 1
        status = "Hit"
    else:
        miss += 1
        status = "Misses"
    return hit, miss, status


def mapeamento_direto(tamanho_cache, posicoes_memoria_acessar):
    # inicializando variaveis
    hits = 0
    misses = 0
    status = ''
    linha = 0

    # inicializando a cache
    cache = inicializar_cache(tamanho_cache)
    # imprimindo valores iniciais
    imprimir_cache(cache)

    for pos_memoria in posicoes_memoria_acessar:
        pos_cache = calcula_posicao(tamanho_cache, pos_memoria)
        valor_cache = cache[pos_cache]
        # calcula hit e misses
        hits, misses, status = calcula_hit_misses(pos_memoria, valor_cache, hits, misses, status)
        # todo só alterar se for misses
        cache[pos_cache] = pos_memoria
        # imprimindo valores
        print('-------------------------------------------')
        print('Linha ', linha, ' | posição da memoria desejada ', pos_memoria)
        print('Status: ', status)
        imprimir_cache(cache)

        linha += 1
    taxa_acerto = hits * 100 / (hits + misses)
    # informações hit e misses
    print("*-------------------------------------------*")
    print("Memórias acessadas: ", misses)
    print("Números de hits: ", hits)
    print("Números de misses: ", misses)
    print("Taxa de acertos (hits): ", taxa_acerto, "%")


def imprimir_cache_associativo(dict):
    # printando o dict no console
    print('Tamanho da cache: ', len(dict))
    for key, value in dict.items():
        print(f'Posição cache || Posição memoria')
        print(f'       {key}      ||       {value} ')


def inserir_cache_associativo(cache, tipo, pos_memoria, tamanho_conjunto):
    valores_conjunto = []
    if tipo == "FIFO":

        #armazenando valores da cache
        lista_valores = list(cache.values())

        #quantidade de linhas do conjunto
        conjunto = int(len(lista_valores) / tamanho_conjunto)

        #verifica em qual conjunto vai ser inserido
        verifica_conjunto = pos_memoria % 2

        if verifica_conjunto == 0:
            num_inicio = 0

            for num in range(num_inicio, tamanho_conjunto):
                valores_conjunto.append(lista_valores[num])
        else:
            num_inicio = tamanho_conjunto

            for num in range(num_inicio, len(lista_valores)):
                valores_conjunto.append(lista_valores[num])

        if -1 not in valores_conjunto:
            #retirando o primeiro que foi adicionado e adicionando novo valor na ultima posição
            lista_valores.insert(num_inicio+tamanho_conjunto, pos_memoria)
            lista_valores.pop(num_inicio)
            pos_cache = num_inicio

        else:
            #procurar valores vazios e inserir na posição vazia
            index = 0

            for novos_valores in valores_conjunto:
                if novos_valores == -1:
                    lista_valores[index+num_inicio] = pos_memoria
                    pos_cache = index+num_inicio
                    break
                index += 1

        # inserindo valores novos na cache
        index = 0
        for novos_valores in lista_valores:
            cache[index] = novos_valores
            index +=1

    elif tipo == "LRU":

        #armazenando valores da cache
        lista_valores = list(cache.values())

        #quantidade de linhas do conjunto
        conjunto = int(len(lista_valores) / tamanho_conjunto)

        #verifica em qual conjunto vai ser inserido
        verifica_conjunto = pos_memoria % 2

        if verifica_conjunto == 0:
            num_inicio = 0

            for num in range(num_inicio, tamanho_conjunto):
                valores_conjunto.append(lista_valores[num])
        else:
            num_inicio = tamanho_conjunto

            for num in range(num_inicio, len(lista_valores)):
                valores_conjunto.append(lista_valores[num])


    return cache,pos_cache


def mapeamento_associativo_por_conjunto(tamanho_cache, posicoes_memoria_acessar,tipo,tamanho_conjunto):
    # inicializando variaveis
    hits = 0
    misses = 0
    status = ''
    linha = 0


    # inicializando a cache
    cache = inicializar_cache(tamanho_cache)
    # imprimindo valores iniciais
    print('mapeamento associativo')
    imprimir_cache_associativo(cache)

    for pos_memoria in posicoes_memoria_acessar:

        cache,pos_cache = inserir_cache_associativo(cache,tipo,pos_memoria,tamanho_conjunto)

        valor_cache = cache[pos_cache]
        # calcula hit e misses
        hits, misses, status = calcula_hit_misses(pos_memoria, valor_cache, hits, misses, status)

        # imprimindo valores
        print('-------------------------------------------')
        print('Linha ', linha, ' | posição da memoria desejada ', pos_memoria)
        print('Status: ', status)
        imprimir_cache(cache)


def retorna_tamanho_conjunto():
    tamanho_conjunto = 0
    dict_opcoes = {
        1: 1,
        2: 2,
        3: 4,
        4: 8,
        5: 16
    }
    print("================================================================")
    print("Selecione a opção de quantos blocos (tamanho) terá no conjunto!")
    print("(1) 1 bloco | (2) 2 blocos | (3) 4 blocos | (4) 8 blocos | (5) 16 blocos")
    while tamanho_conjunto not in dict_opcoes.values():
        try:
            tamanho_conjunto = dict_opcoes[int(input("Digite a opção que deseja: "))]
        except:
            continue

    print(f'Tamanho selecionado: {tamanho_conjunto} blocos')

    return tamanho_conjunto


def retorna_tecnica_substituicao():
    tecnica_substituicao = 0
    dict_opcoes = {
        1: "LRU",
        2: "LFU",
        3: "FIFO"
    }
    print("================================================================")
    print("Agora, selecione a opção da técnica de substituição que deseja!")
    print("(1) LRU | (2) LFU | (3) FIFO")
    while tecnica_substituicao not in dict_opcoes.values():
        try:
            tecnica_substituicao = dict_opcoes[int(input("Digite a opção que deseja: "))]
        except:
            continue

    print(f'Técnica selecionada: {tecnica_substituicao}')

    return tecnica_substituicao


def main():
    # variaveis
    tamanho_cache = 5
    posicoes_memoria_acessar = [2,7,2,12,2,17,2,22,2,27]
    tamanho_conjunto = retorna_tamanho_conjunto()
    tipo = retorna_tecnica_substituicao()

    # chamando função mapeamento direto
    # mapeamento_direto(tamanho_cache, posicoes_memoria_acessar)

    # chamando função mapeamento associativo por conjunto
    mapeamento_associativo_por_conjunto(tamanho_cache, posicoes_memoria_acessar, tipo, tamanho_conjunto)


if __name__ == '__main__':
    main()
