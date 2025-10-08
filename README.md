# FIAP-Checkpoints
Pasta para arquivos de checkpoints
Sistema Simples de Controle de Estoque (Área: Logística/Administração)
Um sistema de linha de comando para gerenciar o estoque de produtos de uma pequena loja.

Conceito: O sistema armazena uma lista de produtos e suas quantidades. O usuário pode adicionar um produto, atualizar a quantidade de um item existente ou listar todos os produtos que estão abaixo de um nível mínimo de estoque.

Como cumpre os requisitos:

a) Declaração de variáveis:

estoque (um dicionário em Python ou uma lista nomeada/data frame em R para guardar o nome do produto e a quantidade).

produto_nome (texto)

quantidade (inteiro)

estoque_minimo (inteiro, ex: 10)

b) Estruturas lógicas:

A verificação se um produto já existe no estoque antes de adicioná-lo.

A comparação da quantidade de um item com o estoque_minimo.

c) Estruturas condicionais:

Um if-else para verificar se um produto já está no estoque ao tentar adicioná-lo. Se sim, atualiza a quantidade; se não, cria um novo item.

Dentro da função de listagem, um if para checar se a quantidade do produto é menor que o estoque_minimo e, só então, exibi-lo.

d) Estruturas de repetição:

Um laço while para o menu principal do sistema, que fica ativo até o usuário escolher a opção "Sair". As opções seriam: 1. Adicionar/Atualizar produto, 2. Listar itens com estoque baixo, 3. Sair.

Um laço for para percorrer todos os itens do estoque na hora de listar os produtos com estoque baixo.

e) Funções:

adicionar_produto(estoque, nome, qtd): Adiciona ou atualiza um produto no estoque.

verificar_estoque_baixo(estoque, minimo): Percorre o estoque e imprime os produtos que estão abaixo do nível mínimo.