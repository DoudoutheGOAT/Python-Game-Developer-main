import pgzrun
import random
WIDTH=750
HEIGHT=500
DoudoutheGOAT=Actor("netherite_noob")
DoudoutheGOAT.x=100
DoudoutheGOAT.y=300
FreshLOL=Actor("freshlol")
FreshLOL.x=100
FreshLOL.y=100
def draw():
    screen.fill("light blue")
    FreshLOL.draw()
    DoudoutheGOAT.draw()
def on_mouse_down(pos):
    if FreshLOL.collidepoint(pos):
        FreshLOL.x=random.randint(50,700)
        FreshLOL.y=random.randint(50,450)
pgzrun.go()