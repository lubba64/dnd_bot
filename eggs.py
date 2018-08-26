#imports

import sys, pygame
import time
import os
#pygame setup

size = width, height =  840, 440
screen = pygame.display.set_mode(size)
black=0,0,0

#tiles load

#classes

class Tile_screen():
    def __init__(self,x,y,imagenum,c):
        self.x=x
        self.y=y
        self.imnum=int(imagenum)
        self.image=Tiles[self.imnum][1]+".png"
        self.a=pygame.image.load(self.image)
        self.c=c
        self.rect=self.a.get_rect()
        self.rect.top=y
        self.rect.left=x
    def setanimation(self,e,i):
        if Tiles[e][0]==None:
            print(e)
            tile[i].image=Tiles[e][1]+".png"
        else:
            print(e)
            tile[int(i)].image=Tiles[int(e)][Tiles[0][int(e+1)]]+".png"

#Tiles 2 perameters "e" and Tiles 2 perameters: 

    def __str__(self):
        return"""
        {0}
        {1}
        {2}
        {3}
        """.format(self.x,self.y,self.image,self.c)

#vars

cpuspeed=.01
spawnpoint=1
coorscanned=1
scanned_screen=spawnpoint
player_in_room=True
load_iterator=-1
water_clock=0
animation_speed=10

#lists
#sort at the end
Tiles=(
[water_clock,"water1","water2","water3","water4"],
[None,"brick_azure"],
[None,"brick_black"],
[None,"brick_blue"],
[None,"brick_brown"],
[None,"brick_chartreuse"],
[None,"brick_cyan"],
[None,"brick_gray"],
[None,"brick_green"],
[None,"brick_mint"],
[None,"brick_orange"],
[None,"brick_pink"],
[None,"brick_red"],
[None,"brick_rose"],
[None,"brick_sand"],
[None,"brick_violate"],
[None,"brick_white"],
[None,"brick_yellow"],
[None,"dirt"],
[None,"grass_flux"],
[None,"grass_slime"],
[None,"grass"],
[None,"log"],
[None,"path_stone"],
[None,"pillar_marble_bottom"],
[None,"pillar_marble_center"],
[None,"pillar_marble_top"],
[None,"sand"],
[None,"stone_black"],
[None,"stone_brown"],
[None,"stone_frost"],
[None,"stone_magma"],
[None,"stone_pink"],
[None,"stone_sand"],
[None,"stone"],
[None,"tile_marble"],
[None,"wall_stone_bottom"],
[None,"wall_stone_bottomleft"],
[None,"wall_stone_bottomright"],
[None,"wall_stone_center"],
[None,"wall_stone_left"],
[None,"wall_stone_right"],
[None,"wall_stone_top"],
[None,"wall_stone_topleft"],
[None,"wall_stone_topright"],
[None,"wall_wood_bottom"],
[None,"wall_wood_bottomleft"],
[None,"wall_wood_bottomright"],
[None,"wall_wood_center"],
[None,"wall_wood_left"],
[None,"wall_wood_right"],
[None,"wall_wood_top"],
[None,"wall_wood_topleft"],
[None,"wall_wood_topright"],
[None,"Null"])

tile=[]
Row_Scanned=[]
#functions

def Set_clocks():
    global water_clock,animation_speed
    animation_speed+=1
    if animation_speed>10:
        animation_speed=0
    if animation_speed==10:
        water_clock+=1
    
    if water_clock>3:
        water_clock=0

#screen main

screen.fill(black)
for i in range(0,11):
    for e in range(0,21):
        tile.append(Tile_screen(e*40,i*40,54,spawnpoint))
        tile[-1].image = "Null.png"
        tile[-1].a = pygame.image.load(tile[-1].image)
        tile[-1].a = pygame.transform.scale(tile[-1].a,(40,40))
        screen.blit(tile[-1].a,tile[-1].rect)
