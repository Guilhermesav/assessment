#Usando o código anterior, escreva um novo programa que, quando as teclas ‘w’, ‘a’, ‘s’ e ‘d’ forem pressionadas,
#ele movimente o círculo com o texto “clique” nas direções corretas. Caso colida com algum retângulo, o retângulo que participou da colisão deve desaparecer
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
    def __init__(self):
        self.largura = 50
        self.altura = 50
        self.x = random.randint(0, (largura_tela-self.largura))
        self.y = random.randint(50, (altura_tela-self.altura))
        self.area = pygame.Rect(self.x,self.y,self.largura,self.altura)
        self.cor = amarelo
    def desenha(self,tela):
        pygame.draw.rect(tela,self.cor,self.area)
   
        
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

    
    
while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            lista_de_pos = list(pygame.mouse.get_pos())
            posx = lista_de_pos[0]
            posy = lista_de_pos[1]
            print(posx,posy)
            if circulo.centerx+100>=posx>=circulo.centerx-100 and circulo.centery+100>=posy>=circulo.centery-100:
                quadrado = Quadrado()
                quadrado.desenha(tela)
                lista_de_quadrados.append(quadrado)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                tela.fill(preto)
                Texto("Clique!",400,100)
                circulo = Circulo(circulo.centerx-5,circulo.centery)
                circulo.desenha(tela)
                for i in lista_de_quadrados:
                    i.desenha(tela)
                if quadrado.area.collidepoint(circulo.centerx,circulo.centery):
                    lista_de_quadrados.remove(quadrado)
                    tela.fill(preto)
                    Texto("Clique!",400,100)
                    circulo.desenha(tela)
                    for i in lista_de_quadrados:
                        i.desenha(tela)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                tela.fill(preto)
                Texto("Clique!",400,100)
                circulo = Circulo(circulo.centerx+5,circulo.centery)
                circulo.desenha(tela)
                for i in lista_de_quadrados:
                    i.desenha(tela)
                    if quadrado.area.collidepoint(circulo.centerx,circulo.centery):
                        lista_de_quadrados.remove(quadrado)
                        tela.fill(preto)
                        Texto("Clique!",400,100)
                        circulo.desenha(tela)
                        for i in lista_de_quadrados:
                            i.desenha(tela)
            if event.key == pygame.K_UP or event.key == ord('w'):
                tela.fill(preto)
                Texto("Clique!",400,100)
                circulo = Circulo(circulo.centerx,circulo.centery-5)
                circulo.desenha(tela)
                for i in lista_de_quadrados:
                    i.desenha(tela)
                    if quadrado.area.collidepoint(circulo.centerx,circulo.centery):
                        lista_de_quadrados.remove(quadrado)
                        tela.fill(preto)
                        Texto("Clique!",400,100)
                        circulo.desenha(tela)
                        for i in lista_de_quadrados:
                            i.desenha(tela)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                tela.fill(preto)
                Texto("Clique!",400,100)
                circulo = Circulo(circulo.centerx,circulo.centery+5)
                circulo.desenha(tela)
                for i in lista_de_quadrados:
                    i.desenha(tela)
                    if quadrado.area.collidepoint(circulo.centerx,circulo.centery):
                        lista_de_quadrados.remove(i)
                        tela.fill(preto)
                        Texto("Clique!",400,100)
                        circulo.desenha(tela)
                    for i in lista_de_quadrados:
                        i.desenha(tela)

                                        
                
            

    pygame.display.update()
    
    clock.tick(50)
    