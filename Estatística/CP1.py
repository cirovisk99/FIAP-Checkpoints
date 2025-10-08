'''
# Estatística - CP1
Conceito: O sistema armazena uma lista de produtos e suas quantidades. 
O usuário pode adicionar um produto, atualizar a quantidade de um item existente ou listar 
todos os produtos que estão abaixo de um nível mínimo de estoque.
'''

import os

estoque = [{'produto':'Televisão', 'categoria':'eletrônicos', 'quantidade':3, 'estoque_minimo':5},
           {'produto':'Geladeira', 'categoria':'eletrodomésticos', 'quantidade':5, 'estoque_minimo':2},
           {'produto':'Smartphone', 'categoria':'eletrônicos', 'quantidade':9 , 'estoque_minimo':10},
           {'produto':'Micro-ondas', 'categoria':'eletrodomésticos', 'quantidade':8 ,'estoque_minimo':3},
           {'produto':'Fone de ouvido', 'categoria':'eletrônicos', 'quantidade':20 ,'estoque_minimo':5}]

          
def exibir_nome_programa():
    print("""

░██████╗████████╗░█████╗░░█████╗░██╗░░██╗  ███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗██████╗░
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝  ████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝██╔══██╗
╚█████╗░░░░██║░░░██║░░██║██║░░╚═╝█████═╝░  ██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██████╔╝
░╚═══██╗░░░██║░░░██║░░██║██║░░██╗██╔═██╗░  ██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██╔══██╗
██████╔╝░░░██║░░░╚█████╔╝╚█████╔╝██║░╚██╗  ██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░░██║
╚═════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝

""")         

def exibir_opcoes():
    print('1. Adicionar ou atualizar produtos no estoque')
    print('2. Ver estoque')
    print('3. Ver produtos com estoque baixo')
    print('4. Sair\n')
    
def opcao_invalida():
    print('Opção inválida\n')
    #input('Digite uma tecla para voltar ao menu principal ')  
    voltar_ao_menu_principal()

def finalizar_app():
    exibir_subtitulo('Finalizando app')

def voltar_ao_menu_principal():
    input('\nDigite qualquer tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(f'{texto}\n')    
    print(linha)
    
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            adicionar_produto()
        elif opcao_escolhida == 2:
            ver_estoque()
        elif opcao_escolhida == 3:
            listar_produtos_estoque_baixo()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()    
        
def adicionar_produto():
    exibir_subtitulo('Adicionar ou atualizar produtos no estoque')
    '''
    função serve para adicionar um novo produto ao estoque ou atualizar a quantidade de um produto existente.
    '''
    nome_do_produto = input('Digite o nome do produto que deseja atualizar: ')
    
    #verifica se o produto já existe no estoque
    flag_produto_existe = False
    
    for item in estoque:
        if item['produto'].lower() == nome_do_produto.lower():
            flag_produto_existe = True
            break
            
    if flag_produto_existe:
        print(f'O produto {nome_do_produto} já existe no estoque.')
        quantidade_atual = item['quantidade']
        print(f'A quantidade atual do produto {nome_do_produto} é {quantidade_atual}.')
        try:
            nova_quantidade = int(input(f'Digite a nova quantidade para o produto {nome_do_produto}: '))
            if nova_quantidade < 0:
                print('A quantidade não pode ser negativa. Operação cancelada.')
            else:
                item['quantidade'] = nova_quantidade
                print(f'A quantidade do produto {nome_do_produto} foi atualizada para {nova_quantidade}.')
        except ValueError:
            print('Entrada inválida. A quantidade deve ser um número inteiro. Operação cancelada.')
    else:
        print(f'O produto {nome_do_produto} não existe no estoque. Vamos adicioná-lo.')
        categoria = input(f'Digite a categoria do produto {nome_do_produto}: ')
        try:
            quantidade = int(input(f'Digite a quantidade inicial do produto {nome_do_produto}: '))
            if quantidade < 0:
                print('A quantidade não pode ser negativa. Operação cancelada.')
                voltar_ao_menu_principal()
                return
            estoque_minimo = int(input(f'Digite o estoque mínimo para o produto {nome_do_produto}: '))
            if estoque_minimo < 0:
                print('O estoque mínimo não pode ser negativo. Operação cancelada.')
                voltar_ao_menu_principal()
                return
            novo_item = {'produto': nome_do_produto, 'categoria': categoria, 'quantidade': quantidade, 'estoque_minimo': estoque_minimo}
            estoque.append(novo_item)
            print(f'O produto {nome_do_produto} foi adicionado ao estoque com sucesso.')
        except ValueError:
            print('Entrada inválida. A quantidade e o estoque mínimo devem ser números inteiros. Operação cancelada.')
        
    voltar_ao_menu_principal()
    
def ver_estoque():
    exibir_subtitulo('Ver estoque')
    cab_1 = 'Produto'
    cab_2 = 'Categoria'
    cab_3 = 'Estoque'
    cab_4 = 'Estoque Mínimo'
    
    print(f'{cab_1.ljust(20)} | {cab_2.ljust(20)} | {cab_3.ljust(10)} | {cab_4}\n')
    
    for produto in estoque:
        nome_produto = produto['produto']
        categoria = produto['categoria']
        quantidade = produto['quantidade']
        estoque_minimo = produto['estoque_minimo']

        print(f'{nome_produto.ljust(20)} | {categoria.ljust(20)} | {str(quantidade).ljust(10)} | {estoque_minimo}')    
  
    voltar_ao_menu_principal()

def listar_produtos_estoque_baixo():
    exibir_subtitulo('Produtos com estoque baixo')
    cab_1 = 'Produto'
    cab_2 = 'Categoria'
    cab_3 = 'Estoque'
    cab_4 = 'Estoque Mínimo'
    
    print(f'{cab_1.ljust(20)} | {cab_2.ljust(20)} | {cab_3.ljust(10)} | {cab_4}\n')
    
    for produto in estoque:
        nome_produto = produto['produto']
        categoria = produto['categoria']
        quantidade = produto['quantidade']
        estoque_minimo = produto['estoque_minimo']
        
        if quantidade < estoque_minimo:
            print(f'{nome_produto.ljust(20)} | {categoria.ljust(20)} | {str(quantidade).ljust(10)} | {estoque_minimo}')    
        else:
            continue
    
    voltar_ao_menu_principal()
        
def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__' :
    main()


