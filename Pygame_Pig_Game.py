import random
import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()

# Window to Display the Game and GUI
window = pygame.display.set_mode((250, 190))
pygame.display.set_caption("Pig Game")

# Colors for the Buttons and Text
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)

# Font
font = pygame.font.SysFont("Arial", 15, bold=True)

# Global variables
playerScore = 0
computerScore = 0
currentRound = 0

game_over = False

# Function to Update the Score Board
def scoreBoard():
    playerScoreLabel = font.render("Your Score: " + str(playerScore), True, BLACK)
    computerScoreLabel = font.render("Computer Score: " + str(computerScore), True, BLACK)
    currentRoundLabel = font.render("Current Round: " + str(currentRound), True, BLACK)
    
    window.blit(playerScoreLabel, (75, 0))
    window.blit(computerScoreLabel, (75, 20))
    window.blit(currentRoundLabel, (75, 40))

# Function for the User Turn
def userTurn():
    global playerScore, currentRound, game_over

    if not game_over:
        dice = random.randint(1, 6)
        if dice == 1:
            currentRound = 0
            scoreBoard()
            computerTurn()
        else:
            currentRound += dice
            scoreBoard()

# Function to Bank the Current Score
def bank():
    global playerScore, currentRound, game_over

    if not game_over:
        playerScore += currentRound
        currentRound = 0
        scoreBoard()
        computerTurn()

# Function for the Computer's Turn
def computerTurn():
    global computerScore

    currentRound = 0
    while True:
        dice = random.randint(1, 6)
        if dice == 1:
            break
        currentRound += dice
        if currentRound > 15:
            computerScore += currentRound
            break

# Function to End the Game
def endGame():
    global game_over
    game_over = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if rollButton.collidepoint(mouse_pos):
                userTurn()
            elif bankButton.collidepoint(mouse_pos):
                bank()
            elif endGameButton.collidepoint(mouse_pos):
                endGame()

    window.fill(WHITE)

    # Displaying the Buttons on the GUI
    rollButton = pygame.draw.rect(window, GOLD, (0, 90, 100, 50))
    pygame.draw.rect(window, BLACK, (0, 90, 100, 50), 2)
    rollButtonLabel = font.render("Roll", True, BLACK)
    window.blit(rollButtonLabel, (35, 105))

    bankButton = pygame.draw.rect(window, GOLD, (150, 90, 100, 50))
    pygame.draw.rect(window, BLACK, (150, 90, 100, 50), 2)
    bankButtonLabel = font.render("Bank", True, BLACK)
    window.blit(bankButtonLabel, (185, 105))

    endGameButton = pygame.draw.rect(window, GOLD, (0, 139, 250, 50))
    pygame.draw.rect(window, BLACK, (0, 139, 250, 50), 2)
    endGameButtonLabel = font.render("End Game", True, BLACK)
    window.blit(endGameButtonLabel, (95, 155))

    # Calling the Functions
    scoreBoard()

# Shows Who Won When the User Clicks on the "End Game" Button
    if game_over:
        result = "It's a draw!"
        if playerScore > computerScore:
            result = "You won!"
        elif computerScore > playerScore:
            result = "Computer won!"
        result_label = font.render(result, True, BLACK)
        window.blit(result_label, (75, 60))

    pygame.display.update()

# Quit pygame
pygame.quit()
