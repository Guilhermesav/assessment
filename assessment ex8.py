import pygame,random

pygame.init()
preto = (0,0,0)
amarelo = (255,255,0)
azul = (0,0,255)
branco = (255,255,255)
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
    def __str__(self):
        return f"({self.x}, {self.y})"
        
        
class Circulo():
    def __init__(self,x,y):
        self.raio = 100
        self.centerx = x
        self.centery = y
        self.center = (self.centerx,self.centery)
        self.cor = azul
    def desenha(self,tela):
        pygame.draw.circle(tela,self.cor,(self.centerx,self.centery),self.raio)
        
def Texto(texto,x,y):
    font = pygame.font.Font(None,24)
    text = font.render(texto,1,branco)
    textpos = text.get_rect(center=(x,y))
    tela.blit(text,textpos)
                
clock = pygame.time.Clock()

conta_clocks = 0
        
circulo = Circulo(400,300)
circulo.desenha(tela)
Texto("Clique!",400,100)
terminou = False
lista_de_quadrados = []
"""for i in range(0, 20):
      q = Quadrado()
      q.desenha(tela)
      lista_de_quadrados.append(q)"""
def redesenha(lista_de_quadrados):
    tela.fill(preto)
    circulo.desenha(tela)
    Texto("Clique!",400,100)
    
    for x in lista_de_quadrados:
        x.desenha(tela)
    
while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            lista_de_pos = list(pygame.mouse.get_pos())
            posx = lista_de_pos[0]
            posy = lista_de_pos[1]
            #print(posx,posy)
            if 500>=posx>=300 and 400>=posy>=200:
                quadrado = Quadrado((random.randint(0,largura_tela)),(random.randint(0,altura_tela)))
                lista_de_quadrados.append(quadrado)
                quadrado.desenha(tela)
                for i in lista_de_quadrados:
                    if quadrado.area.collidepoint(i.x,i.y) and (i is not quadrado):
                        print(i,quadrado)
                        lista_de_quadrados.remove(i)
                        redesenha(lista_de_quadrados)
                    
                            
            
                                        
                
            

    pygame.display.update()
    
    clock.tick(50)
