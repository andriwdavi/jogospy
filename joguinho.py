import pygame

pygame.init()
larguraJan = 640
alturaJan = 480
tamanhoFig = 30
screen = pygame.display.set_mode((larguraJan, alturaJan))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
running = True
direita = True
x = 47
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill((255, 255, 255))

  figura = pygame.Surface([tamanhoFig, tamanhoFig])
  figura.fill((0, 0, 0)) 
  screen.blit(figura, (x, 200))
  if direita == True and x < 610:
      x += 3
      if x >= 610:
        direita = False
  else:
      x -= 3
      if x == 0:
        direita = True
  print("direita:", direita)
  print("x:", x)
  
  

    


  pygame.display.flip() 
  clock.tick(60)

pygame.quit()
