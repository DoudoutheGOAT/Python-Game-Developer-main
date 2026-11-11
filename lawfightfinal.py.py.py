import pgzrun
import random
WIDTH=1000
HEIGHT=750
gorilla=Actor("gorilla.png")
freshlol=Actor("freshlol.png")
noob=Actor("netherite_god.png")
gorilla.x=100
gorilla.y=300
freshlol.x=100
freshlol.y=100
noob.x=100
noob.y=500
online=True
endpoint=999
player=[gorilla,freshlol,noob]
winner=""
def draw():
    screen.fill("gold")
    gorilla.draw()
    freshlol.draw()
    noob.draw()
    if online==False:
        screen.draw.text("Congratulations "+winner.image,(200,300))
def update():
    global online,winner
    if online==True:
        if keyboard.s:
            noob.y+=0.8
        if keyboard.w:
            noob.y-=0.8
        if keyboard.d:
            noob.x+=0.8
        if keyboard.a:
            noob.x-=0.8
        for plr in player:
            if plr.x>=endpoint:
                winner=plr
                #print("Congratulations! You have won!")
                online=False
def freshmovement():
    global online
    if online==True:
        freshlol.x+=random.randint(10,50)
        freshlol.y=random.randint(10,150)
clock.schedule_interval(freshmovement,0.669)
def gorillamovement():
    global online
    if online==True:
        gorilla.x+=random.randint(10,50)
        gorilla.y=random.randint(150,200)
clock.schedule_interval(gorillamovement,0.67)
pgzrun.go()