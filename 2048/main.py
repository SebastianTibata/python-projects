import random
import pygame
import constantes
import sys

# Inicializar pygame
pygame.init()
screen = pygame.display.set_mode((constantes.screen_width, constantes.screen_height))

# Titulo del juego

pygame.display.set_caption("2048")


# Matriz que representa el trablero

board = [[0] * 4 for _ in range(4)]

# Estado del juego

game_over = False
game_won = False

# Funciones necesarias para el juego


def drawscreen():
    screen.fill(constantes.White)
    font = pygame.font.Font(None, 40)
    message_font = pygame.font.Font(None, 30)

    for i in range(4):
        for j in range(4):
            value = board[i][j]
            color = constantes.colors.get(value, constantes.colors[0])
            pygame.draw.rect(
                screen,
                color,
                (
                    j * constantes.cell_size,
                    i * constantes.cell_size,
                    constantes.cell_size,
                    constantes.cell_size,
                ),
                0,
            )
            if value != 0:
                text = font.render(str(value), True, constantes.Black)
                text_rect = text.get_rect(
                    center=(
                        j * constantes.cell_size + constantes.cell_size // 2,
                        i * constantes.cell_size + constantes.cell_size // 2,
                    )
                )
                screen.blit(text, text_rect)
    if game_won:
        text = message_font.render(
            "Felicitaciones has ganado!! Preciona R para reiniciar",
            True,
            constantes.Red,
        )
        screen.blit(text, (50, constantes.screen_height // 2 - 20))
    elif game_over:
        text = message_font.render(
            "Has perdido :(, Preciona R para reiniciar", True, constantes.Red
        )
        screen.blit(text, (20, constantes.screen_height // 2 - 20))


def generate_new_number():
    empty = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty:
        i, j = random.choice(empty)
        board[i][j] = random.choice([2, 4])


def compress(nums):
    new_nums = [num for num in nums if num != 0]
    nums[:] = new_nums + [0] * (4 - len(new_nums))


def merge(nums):
    for i in range(3):
        if nums[i] == nums[i + 1] and nums[i] != 0:
            nums[i] *= 2
            nums[i + 1] = 0


def move_left():
    moved = False
    for i in range(4):
        original = board[i][:]
        compress(board[i])
        merge(board[i])
        compress(board[i])
        if original != board[i]:
            moved = True
    return moved


def move_right():

    moved = False
    for i in range(4):
        original = board[i][:]
        board[i].reverse()
        compress(board[i])
        merge(board[i])
        compress(board[i])
        board[i].reverse()
        if original != board[i]:
            moved = True
    return moved


def move_up():
    moved = False
    for j in range(4):
        column = [board[i][j] for i in range(4)]
        original = column[:]
        compress(column)
        merge(column)
        compress(column)
        for i in range(4):
            board[i][j] = column[i]
        if original != board[i]:
            moved = True
    return moved


def move_down():
    moved = False
    for j in range(4):
        column = [board[i][j] for i in range(4)]
        original = column[:]
        column.reverse()
        compress(column)
        merge(column)
        compress(column)
        column.reverse()
        for i in range(4):
            board[i][j] = column[i]
        if original != board[i]:
            moved = True
    return moved


def check_win():
    return any(2048 in row for row in board)


def check_lose():
    if any(0 in row for row in board):
        return False
    for i in range(4):
        for j in range(4):
            if board[i][j] == board[i][j + 1] or board[j][i] == board[j + 1][i]:
                return False
    return True


def reset_game():
    global board, game_over, game_won
    board = [[0] * 4 for _ in range(4)]
    game_over = False
    game_won = False
    generate_new_number()
    generate_new_number()


reset_game()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
            if not game_over and not game_won:
                moved = False
                if event.key == pygame.K_LEFT:
                    moved = move_left()
                elif event.key == pygame.K_RIGHT:
                    moved = move_right()
                elif event.key == pygame.K_UP:
                    moved = move_up()
                elif event.key == pygame.K_DOWN:
                    moved = move_down()
            if moved:
                generate_new_number()
                if check_win():
                    game_won = True
                elif check_lose():
                    game_over = True

    drawscreen()
    pygame.display.flip()
