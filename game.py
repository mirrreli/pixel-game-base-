import pygame
pygame.init()
win = pygame.display.set_mode((1000,600))

pygame.display.set_caption('Cubes Game')

walkRight = [pygame.image.load('right_1.png'),
pygame.image.load('right_2.png'),pygame.image.load('right_3.png'),
pygame.image.load('right_4.png')]

walkLeft = [pygame.image.load('left_1.png'),
pygame.image.load('left_2.png'), pygame.image.load('left_3.png'),
pygame.image.load('left_4.png')]

playerStand = pygame.image.load('idle.png')
back = pygame.image.load('back.jpg')


clock = pygame.time.Clock()

x,y = 50,519
width,height = 58,71
speed = 8
isJump = False
jumpCount = 10

left = False

animCount = 0
lastMove = 'right'
class snaryad():
    def __init__(self, x,y,radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10*facing
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)




def drawWindow():
    global animCount
    win.blit(back,(0,0))  
    
    if animCount + 1>=20:
        animCount = 0 
    if left:
        win.blit(walkLeft[animCount // 5], (x,y))
        animCount+=1
    elif not left:
        win.blit(walkRight[animCount // 5], (x,y))
        animCount+=1
    else:
        win.blit(playerStand,(x,y))

     
    pygame.display.update()    


run = True
while run:
    clock.tick(30)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_f]:
        if lastMove == 'right':
            facing = 1
        else:
            facing = -1
                
    if keys[pygame.K_LEFT] and x > 5:
        x-=speed
        left = True
        lastMove = 'left'
    elif keys[pygame.K_RIGHT] and x < 1000 - width - 5:
        x+=speed   
        left = False
        lastMove = 'right'
    else:
        animCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount>=-10:
            if jumpCount<= 0:
                y+=(jumpCount**2)/2
            else:
                y-=(jumpCount**2)/2
            jumpCount-=1
        else:
            isJump = False
            jumpCount = 10
    
    drawWindow()
    
    
    
            
            
            
pygame.quit()