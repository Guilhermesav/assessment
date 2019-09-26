#Usando a biblioteca ‘pygame’, escreva um programa que desenha na tela em posição aleatória um quadrado amarelo de tamanho 50 (cinquenta),
#toda vez que a tecla espaço for pressionada ou o botão direito for clicado.
import pygame,random

pygame.init()
preto = (0,0,0)
amarelo = (255,255,0)
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela,altura_tela))

class Quadrado():
    def __init__(self,x,y):
        self.largura = 50
        self.altura = 50
        self.x = x
        self.y = y
        self.area = pygame.Rect(self.x,self.y,self.largura,self.altura)
        self.cor = amarelo
    def desenha(self,tela):
        pygame.draw.rect(tela,self.cor,self.area)
    
        
                
clock = pygame.time.Clock()

conta_clocks = 0
        
        
terminou = False


    
while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tela.fill(preto)
                quadrado = Quadrado(random.randint(0,largura_tela),random.randint(0,largura_tela))
                quadrado.desenha(tela)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                tela.fill(preto)
                quadrado = Quadrado(random.randint(0,largura_tela),random.randint(0,largura_tela))
                quadrado.desenha(tela)   
            

    pygame.display.update()
    
    clock.tick(50)
    
    



