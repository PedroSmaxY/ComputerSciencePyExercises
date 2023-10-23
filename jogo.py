import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definição das cores
COR_FUNDO = (255, 255, 255)  # Branco
COR_LINHAS = (128, 128, 128)  # Cinza
COR_JOGADOR1 = (106, 90, 205)  # Azul-ardósia
COR_JOGADOR2 = (138, 43, 226)  # Azul-violeta
COR_TEXTO = (0, 0, 0)  # Preto

# Definição das dimensões da janela do jogo
largura_janela = 400
altura_janela = 450

# Definição das dimensões do tabuleiro
largura_tabuleiro = largura_janela - 40
altura_tabuleiro = altura_janela - 140

# Definição das dimensões das células
largura_celula = largura_tabuleiro / 3
altura_celula = altura_tabuleiro / 3

# Definição das dimensões do placar
largura_placar = largura_janela
altura_placar = 50

# Definição das dimensões do menu
largura_menu = largura_janela
altura_menu = altura_janela

# Criação da janela do jogo
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Jogo da Velha")

# Fonte do texto
fonte = pygame.font.Font(None, 28)

# Variáveis do placar
pontos_jogador1 = 0
pontos_jogador2 = 0

# Função para desenhar o tabuleiro
def desenhar_tabuleiro():
    janela.fill(COR_FUNDO)
    pygame.draw.line(janela, COR_LINHAS, (largura_celula, altura_placar), (largura_celula, altura_janela - 90), 4)
    pygame.draw.line(janela, COR_LINHAS, (2 * largura_celula, altura_placar), (2 * largura_celula, altura_janela - 90), 4)
    pygame.draw.line(janela, COR_LINHAS, (0, altura_celula + altura_placar), (largura_tabuleiro, altura_celula + altura_placar), 4)
    pygame.draw.line(janela, COR_LINHAS, (0, 2 * altura_celula + altura_placar), (largura_tabuleiro, 2 * altura_celula + altura_placar), 4)

# Função para desenhar os símbolos no tabuleiro
def desenhar_simbolos(tabuleiro):
    for linha in range(3):
        for coluna in range(3):
            x = coluna * largura_celula + largura_celula // 2
            y = linha * altura_celula + altura_celula // 2 + altura_placar
            if tabuleiro[linha][coluna] == 'X':
                pygame.draw.line(janela, COR_JOGADOR1, (x - 50, y - 50), (x + 50, y + 50), 4)
                pygame.draw.line(janela, COR_JOGADOR1, (x + 50, y - 50), (x - 50, y + 50), 4)
            elif tabuleiro[linha][coluna] == 'O':
                pygame.draw.circle(janela, COR_JOGADOR2, (x, y), 50, 4)

# Função para verificar o estado do jogo
def verificar_estado(tabuleiro):
    # Verificar linhas
    for linha in range(3):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] != ' ':
            return tabuleiro[linha][0]

    # Verificar colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != ' ':
            return tabuleiro[0][coluna]

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
        return tabuleiro[0][2]

    # Verificar empate
    if all(tabuleiro[linha][coluna] != ' ' for linha in range(3) for coluna in range(3)):
        return 'Empate'

    return None

# Função para exibir o menu de nomes dos jogadores
def exibir_menu_nomes():
    nome_jogador1 = ""
    nome_jogador2 = ""

    input_box1 = pygame.Rect(50, 100, 300, 50)
    input_box2 = pygame.Rect(50, 200, 300, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color1 = color_inactive
    color2 = color_inactive
    active1 = False
    active2 = False

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box1.collidepoint(event.pos):
                    active1 = not active1
                else:
                    active1 = False
                if input_box2.collidepoint(event.pos):
                    active2 = not active2
                else:
                    active2 = False
                color1 = color_active if active1 else color_inactive
                color2 = color_active if active2 else color_inactive
            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        nome_jogador1 = nome_jogador1[:-1]
                    else:
                        nome_jogador1 += event.unicode
                if active2:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        nome_jogador2 = nome_jogador2[:-1]
                    else:
                        nome_jogador2 += event.unicode

        janela.fill(COR_FUNDO)
        txt_surface1 = fonte.render(nome_jogador1, True, color1)
        txt_surface2 = fonte.render(nome_jogador2, True, color2)
        width1 = max(300, txt_surface1.get_width() + 10)
        width2 = max(300, txt_surface2.get_width() + 10)
        input_box1.w = width1
        input_box2.w = width2
        janela.blit(txt_surface1, (input_box1.x + 5, input_box1.y + 5))
        janela.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))
        pygame.draw.rect(janela, color1, input_box1, 2)
        pygame.draw.rect(janela, color2, input_box2, 2)
        pygame.display.flip()

    return nome_jogador1, nome_jogador2

# Função para exibir o placar
def exibir_placar():
    texto_jogador1 = fonte.render(f"{nome_jogador1}: {pontos_jogador1}", True, COR_TEXTO)
    texto_jogador2 = fonte.render(f"{nome_jogador2}: {pontos_jogador2}", True, COR_TEXTO)
    janela.blit(texto_jogador1, (20, 20))
    janela.blit(texto_jogador2, (largura_janela - texto_jogador2.get_width() - 20, 20))

# Função principal do jogo
def jogar_jogo():
    global nome_jogador1, nome_jogador2, pontos_jogador1, pontos_jogador2

    nome_jogador1, nome_jogador2 = exibir_menu_nomes()

    tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    jogador_atual = 1
    jogo_terminado = False

    while not jogo_terminado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and jogador_atual == 1:
                pos = pygame.mouse.get_pos()
                coluna = pos[0] // largura_celula
                linha = (pos[1] - altura_placar) // altura_celula
                if tabuleiro[linha][coluna] == ' ':
                    tabuleiro[linha][coluna] = 'X'
                    jogador_atual = 2
            elif event.type == pygame.KEYDOWN and jogador_atual == 2:
                if event.key == pygame.K_SPACE:
                    jogador_atual = 1

        estado = verificar_estado(tabuleiro)
        if estado is not None:
            jogo_terminado = True
            if estado == 'Empate':
                mensagem = "Empate!"
            elif estado == 'X':
                mensagem = f"{nome_jogador1} venceu!"
                pontos_jogador1 += 1
            elif estado == 'O':
                mensagem = f"{nome_jogador2} venceu!"
                pontos_jogador2 += 1

        desenhar_tabuleiro()
        desenhar_simbolos(tabuleiro)
        exibir_placar()
        pygame.display.flip()

        if jogo_terminado:
            pygame.time.wait(3000)
            tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            jogador_atual = 1
            jogo_terminado = False

# Execução do jogo
jogar_jogo()
