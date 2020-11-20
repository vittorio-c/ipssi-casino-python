import pygame
from classes.BeginGame import BeginGame

pygame.init()
game=BeginGame()

#Text bienvenu 
font_text=pygame.font.SysFont("Courrier", 60 , bold=True, italic=True)
text_bienvenu=font_text.render("Bienvenu au Casino Game",True,"#A4A43D")

#Text Lancement jeu 
font_text=pygame.font.SysFont("Courrier", 70, bold=True, italic=True)
text_debutjeu=font_text.render("Press key 'S' to start the game",True,"#C5CD17")

# Notre fenetre de jeu
pygame.display.set_caption("Casino Game")
screenGame=pygame.display.set_mode((900,506))

#icon Image 
gameIcon = pygame.image.load("images/casinoIcon.jpg") 
pygame.display.set_icon(gameIcon)
#image background      
backgroundImage=pygame.image.load("images/casinoBg.jpg")                                                                                                                                                                                                                                                                               ;

running=True # fenetre en cours d'execution



while running:
    #Appliquer l'image au background
    screenGame.blit(backgroundImage,(0,0))
    screenGame.blit(text_bienvenu,(135,200))
    screenGame.blit(text_debutjeu,(35,290))
    #Mettre à jour la fenetre
    pygame.display.flip()

    #les evenements 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if (pygame.key.get_pressed()[pygame.K_q]):
                pygame.quit()
            elif (pygame.key.get_pressed()[pygame.K_s]): 
                pygame.quit()    
                game.run()
                print("fcygtvys")
                
                 


