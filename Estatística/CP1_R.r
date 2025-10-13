# Estatística - CP1
# Conceito: O sistema armazena uma lista de produtos e suas quantidades.  # nolint
# O usuário pode adicionar um produto, atualizar a quantidade de um item existente ou listar  # nolint
# todos os produtos que estão abaixo de um nível mínimo de estoque.

# --- Estrutura de Dados Inicial (Equivalente à lista de dicionários em Python) --- # nolint: line_length_linter.
# Em R, um data.frame é a estrutura ideal para dados tabulares como este.
estoque <- data.frame(
  produto = c("Televisão", "Geladeira", "Smartphone", "Micro-ondas", "Fone de ouvido"), # nolint: line_length_linter.
  categoria = c("eletrônicos", "eletrodomésticos", "eletrônicos", "eletrodomésticos", "eletrônicos"), # nolint
  quantidade = c(3, 5, 9, 8, 20),
  estoque_minimo = c(5, 2, 10, 3, 5),
  stringsAsFactors = FALSE # Importante para evitar que strings se tornem fatores # nolint: line_length_linter.
)

# --- Funções Auxiliares ---

exibir_nome_programa <- function() {
  cat("

░██████╗████████╗░█████╗░░█████╗░██╗░░██╗  ███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗██████╗░
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝  ████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝██╔══██╗
╚█████╗░░░░██║░░░██║░░██║██║░░╚═╝█████═╝░  ██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██████╔╝
░╚═══██╗░░░██║░░░██║░░██║██║░░██╗██╔═██╗░  ██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██╔══██╗
██████╔╝░░░██║░░░╚█████╔╝╚█████╔╝██║░╚██╗  ██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░░██║
╚═════╝░░░░╚═╝░░░░╚═╝░░░░╚════╝░░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝

\n\n")
}

exibir_opcoes <- function() {
  cat("1. Adicionar ou atualizar produtos no estoque\n")
  cat("2. Ver estoque\n")
  cat("3. Ver produtos com estoque baixo\n")
  cat("4. Sair\n\n")
}

exibir_subtitulo <- function(texto) {
  # Limpa o console (funciona no RStudio)
  cat("\014")  # nolint: trailing_whitespace_linter.
  linha <- paste(rep("*", nchar(texto)), collapse = "")
  cat(linha, "\n")
  cat(texto, "\n")
  cat(linha, "\n\n")
}

voltar_ao_menu_principal <- function() {
  cat("\nDigite [Enter] para voltar ao menu principal...")
  readline() # Pausa e espera o usuário pressionar Enter
}

# --- Funções Principais ---

adicionar_produto <- function() {
  exibir_subtitulo("Adicionar ou atualizar produtos no estoque")
  nome_do_produto <- readline("Digite o nome do produto que deseja adicionar/atualizar: ") # nolint
  
  # Encontra o índice do produto no data.frame (ignorando maiúsculas/minúsculas)
  indice_produto <- which(tolower(estoque$produto) == tolower(nome_do_produto))



  # a) Estrutura condicional (if/else) para verificar se o produto existe
  if (length(indice_produto) > 0) {
    # Produto existe, então vamos atualizar
    cat("O produto '", nome_do_produto, "' já existe no estoque.\n")
    quantidade_atual <- estoque$quantidade[indice_produto]
    cat("A quantidade atual é ", quantidade_atual, ".\n")
    
    nova_quantidade_str <- readline(paste("Digite a nova quantidade para o produto '", nome_do_produto, "': "))
    nova_quantidade <- suppressWarnings(as.integer(nova_quantidade_str))
    
    if (is.na(nova_quantidade) || nova_quantidade < 0) {
      cat("Entrada inválida. A quantidade deve ser um número inteiro positivo. Operação cancelada.\n")
    } else {
      # Atualiza a quantidade no data.frame original usando o super-assignment operator <<-
      estoque$quantidade[indice_produto] <<- nova_quantidade
      cat("A quantidade do produto '", nome_do_produto, "' foi atualizada para ", nova_quantidade, ".\n")
    }
    
  } else {
    # Produto não existe, vamos adicionar
    cat("O produto '", nome_do_produto, "' não existe no estoque. Vamos adicioná-lo.\n")
    categoria <- readline(paste("Digite a categoria do produto '", nome_do_produto, "': "))
    
    quantidade_str <- readline(paste("Digite a quantidade inicial do produto '", nome_do_produto, "': "))
    quantidade <- suppressWarnings(as.integer(quantidade_str))
    
    estoque_minimo_str <- readline(paste("Digite o estoque mínimo para o produto '", nome_do_produto, "': "))
    estoque_minimo <- suppressWarnings(as.integer(estoque_minimo_str))
    
    if (is.na(quantidade) || is.na(estoque_minimo) || quantidade < 0 || estoque_minimo < 0) { # nolint
      cat("Entrada inválida. Quantidade e estoque mínimo devem ser números inteiros positivos. Operação cancelada.\n") # nolint
    } else {
      novo_item <- data.frame(
        produto = nome_do_produto,
        categoria = categoria,
        quantidade = quantidade,
        estoque_minimo = estoque_minimo
      )
      # Adiciona a nova linha ao data.frame original com o super-assignment operator <<-
      estoque <<- rbind(estoque, novo_item)
      cat("O produto '", nome_do_produto, "' foi adicionado ao estoque com sucesso.\n")
    }
  }
  
  voltar_ao_menu_principal()
}

ver_estoque <- function() {
  exibir_subtitulo("Ver estoque")
  
  # A função print() em R já formata o data.frame de forma legível
  print(estoque)
  
  voltar_ao_menu_principal()
}

listar_produtos_estoque_baixo <- function() {
  exibir_subtitulo("Produtos com estoque baixo")
  
  # b) Estrutura lógica para filtrar o data.frame
  produtos_baixo_estoque <- estoque[estoque$quantidade < estoque$estoque_minimo, ]
  
  if (nrow(produtos_baixo_estoque) > 0) {
    print(produtos_baixo_estoque)
  } else {
    cat("Nenhum produto com estoque baixo encontrado.\n")
  }
  
  voltar_ao_menu_principal()
}

# --- Loop Principal do Programa ---
main <- function() {
  # c) Estrutura de repetição (while) para o menu principal
  while (TRUE) {
    cat("\014") # Limpa a tela
    exibir_nome_programa()
    exibir_opcoes()
    
    opcao_escolhida_str <- readline("Escolha uma opção: ")
    opcao_escolhida <- suppressWarnings(as.integer(opcao_escolhida_str))
    
    if (is.na(opcao_escolhida)) {
      cat("Opção inválida. Por favor, digite um número.\n")
      voltar_ao_menu_principal()
      next # Continua para a próxima iteração do loop
    }
    
    # d) Estrutura condicional para tratar a escolha
    if (opcao_escolhida == 1) {
      adicionar_produto()
    } else if (opcao_escolhida == 2) {
      ver_estoque()
    } else if (opcao_escolhida == 3) {
      listar_produtos_estoque_baixo()
    } else if (opcao_escolhida == 4) {
      cat("Finalizando o app...\n")
      break # Encerra o loop while
    } else {
      cat("Opção inválida.\n")
      voltar_ao_menu_principal()
    }
  }
}

# --- Ponto de Entrada do Script ---
# Verifica se o script está sendo executado diretamente e chama a função principal # nolint
if (interactive()) {
  main()
}
