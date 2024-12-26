import pygame
from constants import *

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  dt = 0
  clock = pygame.time.Clock()
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    screen.fill((0, 0, 0))
    dt = clock.tick(60) / 1000
    pygame.display.flip()
  
if __name__ == "__main__":
  main()