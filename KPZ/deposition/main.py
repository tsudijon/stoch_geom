import pygame 
from pygame.locals import *
from simulation import Board
from constants import *




if __name__ == "__main__":
    pygame.init()

    # Define some colors
    box_size = 5
    game_size = (100,200)
    size = ((game_size[1])*box_size, (game_size[0])*box_size)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Tetris Deposition Model")

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()
    fps = 10000
    game = Board(game_size)
    counter = 0

    pressing_down = False

    while not done:
        counter += 1
        if counter > 100000:
            counter = 0

        game.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_UP:
                #     game.rotate()
                if event.key == pygame.K_DOWN:
                    pressing_down = True
                # if event.key == pygame.K_LEFT:
                #     game.go_side(-1)
                # if event.key == pygame.K_RIGHT:
                #     game.go_side(1)
                # if event.key == pygame.K_SPACE:
                #     game.go_space()
                # if event.key == pygame.K_ESCAPE:
                #     game.__init__(20, 10)

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pressing_down = False

        screen.fill(WHITE)

        ### draw board
        # for i in range(game._size[1]):
        #     for j in range(game._size[0]):
        #         pygame.draw.rect(screen, WHITE, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)


        ### draw dead squares
        for coord in game._used_indices:
            pygame.draw.rect(screen, GRAY,
                            [box_size*coord[1], box_size*coord[0], box_size, box_size])           

        ### draw current shapes
        for piece in game._pieces:
            for coord in piece.get_indices():
                pygame.draw.rect(screen, piece.color,
                                [box_size* coord[1],
                                box_size* coord[0],
                                box_size,
                                box_size])                   


        font = pygame.font.SysFont('Calibri', 25, True, False)
        font1 = pygame.font.SysFont('Calibri', 65, True, False)
        text_game_over = font1.render("Game Over", True, (255, 125, 0))
        text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

        # screen.blit(text, [0, 0])
        # if game.state == "gameover":
        #     screen.blit(text_game_over, [20, 200])
        #     screen.blit(text_game_over1, [25, 265])

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()