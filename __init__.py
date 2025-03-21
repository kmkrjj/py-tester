import pygame
import subprocess  # For launching another Python script

pygame.init()
Screen = pygame.display.set_mode((1000, 500))

class x_btn():
    # ... (x_btn class remains the same) ...
    def __init__(self, x, y, image, scale):
        x_btn_width = image.get_width()
        x_btn_height = image.get_height()
        self.image = pygame.transform.scale(image, (int(x_btn_width * scale), int(x_btn_height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw_btn(self, running):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return False
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        Screen.blit(self.image, (self.rect.x, self.rect.y))
        return running

    def handle_event(self, event, running):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return False
        return running

# class launch_btn(): #New class
#     def __init__(self, x, y, image, scale, script_path): # added script_path
#         launch_btn_width = image.get_width()
#         launch_btn_height = image.get_height()
#         self.image = pygame.transform.scale(image, (int(launch_btn_width * scale), int(launch_btn_height * scale)))
#         self.rect = self.image.get_rect()
#         self.rect.topleft = (x, y)
#         self.clicked = False
#         self.script_path = script_path # added script_path attribute

#     def draw_btn(self, running):
#         mouse_pos = pygame.mouse.get_pos()
#         if self.rect.collidepoint(mouse_pos):
#             if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
#                 self.clicked = True
#                 subprocess.Popen(["python", self.script_path]) #Launch game.py
#                 return False #End current program.
#         if pygame.mouse.get_pressed()[0] == 0:
#             self.clicked = False
#         Screen.blit(self.image, (self.rect.x, self.rect.y))
#         return running

#     def handle_event(self, event, running):
#         if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
#             return False
#         return running

'''# Example usage:
image_x = pygame.image.load("x.png")
image_game = pygame.image.load("game.png") #image for the new button.
close_button = x_btn(10, 10, image_x, 0.5)
game_button = launch_btn(100, 10, image_game, 0.5, "game.py") #game.py path.

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        running = close_button.handle_event(event, running)
        running = game_button.handle_event(event, running)

    Screen.fill((255, 255, 255))
    running = close_button.draw_btn(running)
    running = game_button.draw_btn(running)

    pygame.display.flip()

pygame.quit()'''