import pygame
from pygame.locals import *

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))

clock = pygame.time.Clock()
fps = 144

images = {
    "enemies" : {
        "sprite" : pygame.image.load("enemysprite.png")
        },
    
    
    "ground" : pygame.image.load("sandbox.png")
    
}

class Ground():
    def __init__(self, pos, dir):
        self.image = images["ground"]
        self.rect = self.image.get_rect(topleft = pos)
        self.dir = dir
        
    def update(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos,enemy, time_to_start, speed, hp):
        pygame.sprite.Sprite.__init__(self)
        self.image = images["enemies"][enemy]
        self.rect = self.image.get_rect(center = pos)
        self.delay = time_to_start
        self.speed, self.hp = speed, hp
        
        self.x,self.y = pos
        
        self.goal = 0
    
    def update(self, ground_list):
        self.calc_pos(ground_list)
        #self.rect.x += self.speed
        
    def calc_pos(self, ground_list):
        s = ["left", "right"]
        u = ["top", "down"]
        
        max_goal = len(ground_list)
        
        self.str_goal = ground_list[self.goal].dir
        
        if ground_list[self.goal].dir in s:
            self.goal_x = ground_list[self.goal].rect.x 
            self.goal_y = ground_list[self.goal].rect.y 
            # if self.goal_x > self.rect.x:
            #     self.rect.x += self.speed
            # if self.goal_x < self.rect.x:
            #     self.rect.x -= self.speed
        elif ground_list[self.goal].dir in u:
            self.goal_y = ground_list[self.goal].rect.y 
            self.goal_x = ground_list[self.goal].rect.x
            # if self.goal_y > self.rect.y:
            #     self.rect.y += self.speed
            # if self.goal_y < self.rect.y:
            #     self.rect.y -= self.speed
                
        self.check_reached_goal()
                
    def check_reached_goal(self):
        
        if self.str_goal == "right":
            if not self.rect.x <= self.goal_x:
                self.goal += 1
                print("reached right" , self.goal -1)
            else:
                self.rect.x += self.speed
        if self.str_goal == "left":
            if not self.rect.x >= self.goal_x:
                self.goal += 1
                print("reached left", self.goal -1)
            else:
                self.rect.x -= self.speed
                
        if self.str_goal == "bottom":
            if not self.rect.y >= self.goal_y:
                self.goal += 1
                print("reached bottom" , self.goal -1)
            else:
                self.rect.y += self.speed
                
        if self.str_goal == "top":
            if not self.rect.y <= self.goal_y:
                self.goal += 1
                print("reached top" , self.goal -1)
            else:
                self.rect.y -= self.speed
        
class Level():
    def __init__(self):
        self.stuff = {
            1: {
            
            "grounds" : [Ground((0, 100), "right"),
                         Ground((100, 100), "right"),
                         Ground((200, 100), "right"),
                         Ground((200, 200), "down"),
                         Ground((300, 200), "right"),
                         ],
            "enemies" : [Enemy((0,150),"sprite", 0, 2, 100)],
            },
            
            
            2: {
            
            "grounds" : [Ground((0, 100), "right"),
                         Ground((0, 200), "down"),
                         Ground((0, 300), "down"),
                         Ground((100, 300), "right"),
                         Ground((200, 300), "right"),
                         ],
            "enemies" : [Enemy((0,150),"sprite", 0, 2, 100)],
            },
        }
        
        
    def update_level(self, level):
        global ground_list, enemy_list, enemy_group
        ground_list = self.stuff[level]["grounds"]
        enemy_list = self.stuff[level]["enemies"]
        
        for enemy in enemy_list:
            enemy_group.add(enemy)
            enemy_list.remove(enemy)
        
lvl = Level()

ground_list = []
enemy_list = []
enemy_group = pygame.sprite.Group()

lvl_on = 1

sand_box_colour = (194, 178, 128)
sand_colour = (177,157,94)

def render():
    screen.fill(sand_colour)
    
    for ground in ground_list:
        ground.update()
        
    enemy_group.update(ground_list)
    enemy_group.draw(screen)

run = True
while run:
    clock.tick(fps)
    
    render()
    #lvl.update_level()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            
        if event.type == KEYDOWN:
            lvl.update_level(1)
            print(ground_list)
            
    pygame.display.update()
            
            
quit()