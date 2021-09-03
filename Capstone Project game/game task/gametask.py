import pygame
# pygame setup and startup
pygame.init()

# screen display
width = 950
height = 700
screen = pygame.display.set_mode((width,height))

# images used as objects in the game
player = pygame.image.load("hero.png")
enemy1 = pygame.image.load("evil.png")
enemy3 = pygame.image.load("evil2.png")
enemy2 = pygame.image.load("evil3.png")
prize= pygame.image.load("win.png")

# game object height and width
player_height = player.get_height()
player_width = player.get_width()
enemy_height = enemy1.get_height()
enemy_width = enemy1.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

# prize position
prizex = 800
prizey  = 300

# player position

playerXPosition = 100
playerYPosition = 50

# enemy positions
enemyXPosition = width
enemyYPosition = height - enemy_height
enemy2XPosition = width
enemy2YPosition = 10
enemy3XPosition = width
enemy3YPosition =  300


# stored booleans to be used in the game loop
keyUp = False
keyDown = False
keyl = False
keyR = False


# while creates main game loop
# screen.blit displays images on the display
# screen.fill clears screen so no multiples of images appear
while 1:
    screen.fill(0)
    screen.blit(player, (playerXPosition,
                         playerYPosition))
    screen.blit(enemy1, (enemyXPosition, enemyYPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizex,prizey))
#updates screen
    pygame.display.flip()

# this allows user to quit game
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
 # this event checks if the user press a key down if key is down key turns true

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_RIGHT:
                    keyR= True
            if event.key == pygame.K_LEFT:
                    keyl= True

# this event checks if the key is up if up  key will turn false

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                    keyl = False
            if event.key == pygame.K_RIGHT:
                    keyR = False

# if a key if found to be true movement will happen
# movement has a cap ensuring player dose not go off screen
    if keyUp == True:
        if playerYPosition > 0:
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < 600 :
            playerYPosition += 1
    if keyl == True:
       if playerXPosition > 0:
        playerXPosition -= 1
    if keyR == True:
        if playerXPosition < 870 :
            playerXPosition += 1


# player and prize hit boxes
    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top =prizey
    prizeBox.left = prizex


# each enemy  gets a hit box
    enemyBox = pygame.Rect(enemy1.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition


# if user hits enemy  user will lose and the game will quit
    if playerBox.colliderect(enemyBox):
        print("You lose!")
        pygame.quit()
        exit(0)
    elif playerBox.colliderect(enemy2Box):
        print("You lose!")
        pygame.quit()
        exit(0)
    elif playerBox.colliderect(enemy3Box):
        print("You lose!")
        pygame.quit()
        exit(0)

# If user reaches ship user wins the game
    if playerBox.colliderect(prizeBox):
# Display user win and quits game
        print("You have reached the ship you win!")
        pygame.quit()
        exit(0)

 # makes enemys go across the screen at different speeds
    enemyXPosition -= 0.20
    enemy2XPosition -= 0.25
    enemy3XPosition -= 0.20







