#============================================================== The initilization of the library and setting of the display dimensions
import pygame
import random
pygame.init() #always the first step, initializing the library

width = 1000
height = 700
win = pygame.display.set_mode((width,height))
pygame.display.set_caption('Snake')

#--------------------------------------------------------------- end

#============================================================== Character
class Snake(pygame.sprite.Sprite):
    def __init__(self,width,height,x,y,vel): 
        pygame.sprite.Sprite.__init__(self)
        self.bodyArray = []
        self.widthBody = width
        self.heightBody = height
        self.xBody = x
        self.yBody = y

        self.xHead = x
        self.yHead = y
        self.widthHead = width
        self.heightHead = height
        
        self.vel = vel
        
        
    def makeHead(self):
        self.headBlock = pygame.Rect(self.xHead,self.yHead,self.widthHead,self.heightHead)    

    def makeBody(self):
        self.bodyBlock = pygame.Rect(self.xBody,self.yBody,self.widthBody,self.heightBody)
        
        
    
    def pushBody(self):
        
        self.bodyArray.append(self.bodyBlock)
        
        

    def drawHead(self,window):
        pygame.draw.rect(window,(0,255,0),(self.headBlock))    

    def drawBody(self,window):
        pygame.draw.rect(window,(255,255,12),(self.bodyBlock))



class Food():
    def __init__(self,radius):
        self.radius = radius
        



    def newPosition(self): 
                
            self.xCircle = random.randrange(100,900,1)
            self.yCircle = random.randrange(100,600,1)

            return self.xCircle, self.yCircle


    def draw(self,window,x,y):    
        self.x = x
        self.y = y

        pygame.draw.circle(window,(0,255,0),(self.x,self.y),5)

         

#--------------------------------------------------------------- end

#============================================================== Main loop
        
eaten = False
foodX, foodY = 450, 450

run = True
snakePlayer = Snake(20,20,50,50,10)
foodOrb = Food(5)
eatCount = 0
while run:
    pygame.time.delay(100) #100 milliseconds -> 0.1 second
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snakePlayer.xBody -= snakePlayer.vel
        snakePlayer.xHead -= snakePlayer.vel        
    if keys[pygame.K_RIGHT]:
        snakePlayer.xBody += snakePlayer.vel
        snakePlayer.xHead += snakePlayer.vel
    if keys[pygame.K_UP]:
        snakePlayer.yBody -= snakePlayer.vel
        snakePlayer.yHead -= snakePlayer.vel
    if keys[pygame.K_DOWN]:
        snakePlayer.yBody += snakePlayer.vel
        snakePlayer.yHead += snakePlayer.vel
    #if snakePlayer.x < snakePlayer.path [1]: 
    #else:
        #snakePlayer.xHead -= snakePlayer.vel
   
    win.fill((0,0,0))
  
    

    snakeRect = pygame.Rect(snakePlayer.xBody,snakePlayer.yBody,snakePlayer.widthBody,snakePlayer.heightBody)

    snakePlayer.makeHead()
   
    
    
    if eaten is True:
        foodX, foodY = foodOrb.newPosition()
        snakePlayer.drawHead(win)
        
        eatCount += 1
        if eatCount >= 1:
            for i in range(eatCount):
                snakePlayer.drawHead(win)
                snakePlayer.xHead += 20
                print(eatCount)


 
    
    foodRect = pygame.Rect(foodX,foodY,5,5)
    
    foodOrb.draw(win,foodX,foodY)

    #snakePlayer.drawBody(win)
    snakePlayer.drawHead(win)

    #Collision check
    eaten = pygame.Rect.colliderect(snakeRect, foodRect)
    print(eaten)
 
  

    pygame.display.update()
    


pygame.quit()


#--------------------------------------------------------------- end


