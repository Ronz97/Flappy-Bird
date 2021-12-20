import pygame #bilbioteca para jogos
import os #integrar codigos com os arquivos do pc
import random #Gerar Numeros aleatorios 

TELA_LARGURA = 500
TELA_ALTURA = 800
#carregando as imagens
IMAGEN_CANO = pygame.transform.pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','pipe.png')))
IMAGEN_CHAO = pygame.transform.pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','base.png')))
IMAGEN_BACKGROUND = pygame.transform.pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bg.png')))
IMAGENS_PASSARO = [
    pygame.transform.pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird1.png'))),
    pygame.transform.pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird2.png'))),
    pygame.transform.pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird3.png'))),
]
#Tipo de letra para marcar pontos
pygame.font.init()
FONTES_PONTOS = pygame.font.pygame.font.SysFont('arial', 50, bold=False, italic=False)

#Classes do passaro , chão e cano 

class passaro:
    imgs = IMAGENS_PASSARO
    #Animações de Rotação 
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagen = self.IMGS[0]
    #pular no eixo y 
    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y
    
    def mover(self):
        #calcular o deslocamento 
        self.tempo +=1 #cada segundo vai executando a função
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo
        #restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -=2
            
        self.y +=deslocamento
        #Angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO
    def desenhar(self, tela):
        #defenir qual image utilizar
        self.contagem_imagem +=1
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagen = self.IMGS[0]
        elif self.contagem_imag < self.TEMPO_ANIMACAO*2:
            self.imagen = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
            self.imagen = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
            self.imagen = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO*4+1:
            self.imagen = self.IMGS[0]
            self.contagem_imagem = 0
            
        
        #se o passaro tiver caindo não bater asas
        if self.angulo <= -80:
            self.imagen = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO+2
        
        #desenhar image
        imagen_rotacionada = pygame.transform.rotate(self.imagen, self.angulo)
        posicao_centro_imagen = self.imagen.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagen_rotacionada.get_rect(center=posicao_centro_imagen)
        tela.blit(imagen_rotacionada, retangulo.topleft)

    def get_mask(self):
        pygame.mask.from_surface(self.imagen)
        
        
        
    
    
    

class chao:
    pass

class cano:
    pass


