
import pygame
import sys
import math

#FY
g=10
#time
fps=60
clock = pygame.time.Clock()
#colours:
BLUE=(0,0,255)
WHITE=(255,255,255)
#screen:
SIRKA=1200
VYSKA=800
screen = pygame.display.set_mode((SIRKA,VYSKA))

TIME=False
def time_switch():
    global TIME
    TIME=not TIME

class Button: # Třída pro tlačítko

    def __init__(self, x, y, width, height, color, button_press):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.button_press=button_press#jestli je tlacitko zmacknuto jenom ednou nebo je holdenej left click
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
    #chekuje zda myš.pos=button.pos    
    def zmacknuto(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)    
class Object:#class pro obejct/cirle

    def __init__(self, x, y, polomer, color, weight,):
        self.x = x
        self.y = y
        self.polomer =polomer
        self.color = color
        self.weight = weight
        self.obem=self.polomer*self.polomer*3.14
        self.hustota=self.weight/self.obem
        self.gravity_speed=0
        self.polomer_distance= math.sqrt((pygame.mouse.get_pos()[0] - self.x)**2 + (pygame.mouse.get_pos()[1] - self.y)**2)
        self.up_speed=0
        self.down_speed=0
        self.left_speed=0
        self.right_speed=0


    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.polomer)

    def gravity_move(self):
        #if self.x - self.polomer < 0 or self.x + self.polomer > SIRKA:
        if  self.y + self.polomer > VYSKA :  
            self.gravity_speed_reset()
        else:
            self.y +=self.gravity_speed
            self.gravity_speed+=g/fps  
    def gravity_speed_reset(self):
        self.gravity_speed=0     

    def move_duraction(self):
        duraction=  pygame.Rect(self.x, self.y, 20, 60)




circle=Object(300,400,20,BLUE,1000)
time_button=Button(SIRKA-50,25,30,30,BLUE,True)


# Hlavní loop
running = True
while running:
    # vypnutí programu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #chek time_button zda je zmackly a switch TIME TRUE/FALSE
    if time_button.button_press==True:
        if  pygame.mouse.get_pressed()[0]==True and time_button.zmacknuto(event.pos) or pygame.key.get_pressed()[pygame.K_SPACE]:
            time_button.button_press=False
            time_switch()
    elif time_button.button_press==False and pygame.mouse.get_pressed()[0]==False and pygame.key.get_pressed()[pygame.K_SPACE]==False:
        time_button.button_press=True

    # oladaní pohyb na zklade casu + pohyb obejctu pomocí myši
    if TIME==True: 
        circle.gravity_move()
    else:
        #pohyb circle myš
        if pygame.mouse.get_pressed()[0]==True and circle.polomer_distance >= circle.polomer and time_button.zmacknuto(event.pos)==False :
            circle.x=pygame.mouse.get_pos()[0]
            circle.y=pygame.mouse.get_pos()[1]
            circle.gravity_speed_reset()
        elif pygame.mouse.get_pressed()[2]==True and circle.polomer_distance >= circle.polomer and time_button.zmacknuto(event.pos)==False :
            circle.gravity_speed_reset()
            circle.move_duraction()
            
    # Vykreslení
    screen.fill(WHITE)
    circle.draw(screen)
    time_button.draw(screen)
    pygame.display.flip()
   
    # time/FPS
    clock.tick(fps)

# Ukončení Pygame
pygame.quit()
sys.exit()














