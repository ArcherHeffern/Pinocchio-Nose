import pygame

class Draggable:
    def __init__(self, x, y, width, height, color, win):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.dragging = False
        self.win = win

    def draw(self):
        pygame.draw.rect(self.win, self.color, self.rect)

    def update(self):
        if self.dragging:
            # Update position based on mouse movement
            self.rect.center = pygame.mouse.get_pos()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                # Start dragging
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # Stop dragging
            self.dragging = False