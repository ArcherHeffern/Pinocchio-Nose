import pygame

pygame.init()

# Set up the game window
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("My Clicker Game")

# Set up the button
button_width = 200
button_height = 100
button_x = (win_width - button_width) // 2
button_y = (win_height - button_height) // 2
button_color = (255, 255, 255)
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# Set up the font
font = pygame.font.SysFont("Arial", 32)

# Set up the score
score = 0

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                score += 1

    # Clear the screen
    win.fill((0, 0, 0))

    # Draw the button
    pygame.draw.rect(win, button_color, button_rect)

    # Draw the score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    win.blit(score_text, (20, 20))

    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()