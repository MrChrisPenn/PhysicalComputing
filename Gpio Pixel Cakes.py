
from mcpi.minecraft import Minecraft
import time
from gpiozero import Button

#Written By Chris Penn updated to work with gpio zero 04/18
#Adapted parts from Kari Lawlor

mc = Minecraft.create()

# wool colours 
O = 1 # Orange
S = 6 # Pink / Skin
G = 5 # Green
W = 0 # White
R = 14 # Red
SB = 9# Sky blue / cyan
B = 12# Brown
DG = 13 # DARK GREEN
BL = 15 # Black
B1 = 0
B2 = 1
# No Block = -1, White = 0, Orange = 1, Magenta = 2, Light Blue = 3,
# Yellow = 4, Lime = 5, Pink = 6, Grey = 7, Light Grey = 8,
# Cyan = 9, Purple = 10, Blue = 11, Brown = 12, Green = 13, Red = 14, Black = 15


#initilise button
Switch = Button(3)




#by @ChrisPenn84
Cake1 = [
[B,  R,  B,  R,  B, R,  B,  B],
[B,  SB,  B,  SB,  B, SB,  B,  B],    
[B,  SB,  B,  SB,  B, SB,  B,  B],
[B,  SB,  B,  SB,  B,SB , B,  B],
[W,  W,  W,   W,  W,  W,  W,  W],
[W,  W,  W,   W,  W,  W,  W,  W],
[W,  W,  W,   W,  W,  W,  W, W],
[R,  R,  R,   R,  R,  R,  R, R],
[W,  W,  W,   W,  W,  W,  W, W],
[W,  W,  W,   W,  W,  W,  W, W],
[W,  W,  W,   W,  W,  W,  W, W],
[W,  W,  W,   W,  W,  W,  W,  W],
]
#by @ChrisPenn84 
Cake2 = [
[B,  O,  B,  O,  B, O,  B,  B],
[B,  SB,  B,  SB,  B, SB,  B,  B],    
[B,  SB,  B,  SB,  B, SB,  B,  B],
[B,  SB,  B,  SB,  B,SB , B,  B],
[W,  W,  W,   W,  W,  W,  W,  W],
[W,  W,  W,   W,  W,  W,  W,  W],
[W,  W,  W,   W,  W,  W,  W, W],
[R,  R,  R,   R,  R,  R,  R, R],
[W,  W,  W,   W,  W,  W,  W, W],
[W,  W,  W,   W,  W,  W,  W, W],
[W,  W,  W,   W,  W,  W,  W, W],
[W,  W,  W,   W,  W,  W,  W,  W],
]


#By @KariLawler (Twitter)
#by @ChrisPenn84 
Creeper1 = [
[B,  R,  B,  R,  B, R,  B,  B],
[B,  SB,  B,  SB,  B, SB,  B,  B],    
[B,  SB,  B,  SB,  B, SB,  B,  B],
[B,  SB,  B,  SB,  B,SB , B,  B],
[DG, DG, DG, DG, DG, DG, DG, DG],
[DG, BL, BL, DG, DG, BL, BL, DG],
[DG, BL, BL, DG, DG, BL, BL, DG],
[DG, DG, DG, BL, BL, DG, DG, DG],
[DG, DG, BL, BL, BL, BL, DG, DG],
[DG, DG, BL, BL, BL, BL, DG, DG],
[DG, DG, BL, DG, DG, BL, DG, DG],
[DG, DG, DG, DG, DG, DG, DG, DG],
]


#By @KariLawler (Twitter)
#by @ChrisPenn84 
Creeper2 = [
[B,  O,  B,  O,  B, O,  B,  B],
[B,  SB,  B,  SB,  B, SB,  B,  B],    
[B,  SB,  B,  SB,  B, SB,  B,  B],
[B,  SB,  B,  SB,  B,SB , B,  B],
[DG, DG, DG, DG, DG, DG, DG, DG],
[DG, BL, BL, DG, DG, BL, BL, DG],
[DG, BL, BL, DG, DG, BL, BL, DG],
[DG, DG, DG, BL, BL, DG, DG, DG],
[DG, DG, BL, BL, BL, BL, DG, DG],
[DG, DG, BL, BL, BL, BL, DG, DG],
[DG, DG, BL, DG, DG, BL, DG, DG],
[DG, DG, DG, DG, DG, DG, DG, DG],
]



#@KariLawler (Twitter)
Pig1 = [
[B,  R,  B,  R,  B, R,  B,  B],
[B,  SB,  B,  SB,  B, SB,  B,  B],    
[B,  SB,  B,  SB,  B, SB,  B,  B],
[B,  SB,  B,  SB,  B,SB , B,  B],
[S, S, S, S, S, S, S, S],
[S, S, S, S, S, S, S, S],
[S, S, S, S, S, S, S, S],
[BL, W, S, S, S, S, W, BL],
[S, S, W, W, W, W, S, S],
[S, S, R, S, S, R, S, S],
[S, S, W, W, W, W, S, S],
[S, S, S, S, S, S, S, S],
]

#@KariLawler (Twitter)

Pig2 = [
[B,  O,  B,  O,  B, O,  B,  B],
[B,  SB,  B,  SB,  B, SB,  B,  B],    
[B,  SB,  B,  SB,  B, SB,  B,  B],
[B,  SB,  B,  SB,  B,SB , B,  B],
[S, S, S, S, S, S, S, S],
[S, S, S, S, S, S, S, S],
[S, S, S, S, S, S, S, S],
[BL, W, S, S, S, S, W, BL],
[S, S, W, W, W, W, S, S],
[S, S, R, S, S, R, S, S],
[S, S, W, W, W, W, S, S],
[S, S, S, S, S, S, S, S],
]


#by @ChrisPenn84
Alex1 = [
[B,  R,  B,  R,  B, R,  B,  B],
[B,  SB,  B,  SB,  B, SB,  B,  B],    
[B,  SB,  B,  SB,  B, SB,  B,  B],
[B,  SB,  B,  SB,  B,SB , B,  B],
[O,  O,  O,   O,  O,  O,  O,  O],
[O,  O,  O,   O,  O,  O , O,  O],
[O,  O,  O,   O,  S,  S,  O,  O],
[O,  O,  O,   S,  S,  S,  S, S],
[S,  W,  G,   S,  S,  G,  W, S],
[S,  S,  S,   S,  S,  S,  S, ],
[S,  S,  S,   R, R,  S,  S, S],
[S,  S,  S,   S,  S,  S,  S, S],
]

#by @ChrisPenn84
Alex2 = [
[B,  O,  B,  O,  B, O,  B,  B],
[B,  SB,  B,  SB,  B, SB,  B,  B],    
[B,  SB,  B,  SB,  B, SB,  B,  B],
[B,  SB,  B,  SB,  B,SB , B,  B],
[O,  O,  O,   O,  O,  O,  O,  O],
[O,  O,  O,   O,  O,  O , O,  O],
[O,  O,  O,   O,  S,  S,  O,  O],
[O,  O,  O,   S,  S,  S,  S, S],
[S,  W,  G,   S,  S,  G,  W, S],
[S,  S,  S,   S,  S,  S,  S, ],
[S,  S,  S,   R, R,  S,  S, S],
[S,  S,  S,   S,  S,  S,  S, S],
]



#by @ChrisPenn84
Steve1 = [
[B,  R,  B,  R,  B, R,  B,  B],
[B,  SB,  B,  SB,  B, SB,  B,  B],    
[B,  SB,  B,  SB,  B, SB,  B,  B],
[B,  SB,  B,  SB,  B,SB , B,  B],
[B,  B,  B,   B,  B,  B,  B,  B],
[B,  B,  B,   B,  B,  B , B,  B],
[B,  S,  S,   S,  S,  S,  S,  B],
[S,  S,  S,   S,  S,  S,  S,  S],
[S,  W,  SB,  S,  S, SB,  W, S],
[S,  S,  S,   R,  R,  S,  S, S],
[S,  S,  B,   S,  S,  B,  S, S],
[S,  S,  B,   B,  B,  B,  S, S],
]

#by @ChrisPenn84
Steve2 = [
[B,  O,  B,  O,  B, O,  B,  B],
[B,  SB,  B,  SB,  B, SB,  B,  B],    
[B,  SB,  B,  SB,  B, SB,  B,  B],
[B,  SB,  B,  SB,  B,SB , B,  B],
[B,  B,  B,   B,  B,  B,  B,  B],
[B,  B,  B,   B,  B,  B , B,  B],
[B,  S,  S,   S,  S,  S,  S,  B],
[S,  S,  S,   S,  S,  S,  S,  S],
[S,  W,  SB,  S,  S, SB,  W, S],
[S,  S,  S,   R,  R,  S,  S, S],
[S,  S,  B,   S,  S,  B,  S, S],
[S,  S,  B,   B,  B,  B,  S, S],
]


#By @KariLawler (Twitter) # brilliantly efficient procedure which renders pixel art despite the dimensions of the array.
def print_PixelArt(List):
    block = 35 # wool
    x, y, z = mc.player.getPos()
    pixel_y = y + len(List) - 1
    pixel_z = z - 15
    for row in List:
        pixel_x = x
        for pixel in row:
            if pixel > -1:
                mc.setBlock(pixel_x, pixel_y, pixel_z, block, pixel)
            pixel_x += 1
        pixel_y -= 1


#by @ChrisPenn84
mc.postToChat("Pi Birthday 3/4th March 2018... happy Birthday RPI!")
time.sleep(1)
mc.postToChat("5")
time.sleep(1)
mc.postToChat("4")
time.sleep(1)
mc.postToChat("3")
time.sleep(1)
mc.postToChat("2")
time.sleep(1)
mc.postToChat("1")
time.sleep(1)
mc.postToChat("Go... take the two gpio wires and connect them to start the celebrations")
time.sleep(1)


#by @ChrisPenn84 
while True:

    Switch.wait_for_press()
    mc.postToChat("Happy Birthday RPI here is some pixel cakes :)")
        #candle colours alternate between orange and red
    print_PixelArt(Alex1)
    time.sleep(1)
    print_PixelArt(Alex2)
    time.sleep(1)
    print_PixelArt(Pig1)
    time.sleep(1)
    print_PixelArt(Pig2)
    time.sleep(1)
    print_PixelArt(Steve1)
    time.sleep(1)
    print_PixelArt(Steve2)
    time.sleep(1)
    print_PixelArt(Creeper1)
    time.sleep(1)
    print_PixelArt(Creeper2)
    time.sleep(1)
    print_PixelArt(Cake1)
    time.sleep(1)
    print_PixelArt(Cake2)
    time.sleep(1)
        #Final birthday message.
    mc.postToChat("Happy Birthday!!! the end")
