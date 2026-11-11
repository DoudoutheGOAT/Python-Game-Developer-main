import pgzrun
import random

WIDTH=1000
HEIGHT=667

online=True

gorilla_alive=True
freshlol_alive=True

freshlol=Actor("freshlol.png")
blue=Actor("blue_skin.png")
creeper=Actor("formal_creeper_skin.png")
funny=Actor("funny_skin.png")
gorilla=Actor("gorilla.png")
moss=Actor("moss_skin.png")
duck=Actor("duck_skin.png")
fireball=Actor("fireball.png")
earth=Actor("earth.png")

enemies=[blue,creeper,funny,moss,duck]

fbactive=False
earth_active=False

freshlol_health=10000
gorilla_health=15000
blue_health=3000
duck_health=5000
creeper_health=10000
funny_health=5000
moss_health=5000





gorilla.x=100
gorilla.y=500
freshlol.x=100
freshlol.y=250
blue.x=900
blue.y=100
duck.x=900
duck.y=250
creeper.x=750
creeper.y=300
funny.x=900
funny.y=400
moss.y=550
moss.x=900


def draw():
    screen.blit("clouds.webp",(0,0))
    gorilla.draw()
    freshlol.draw()
    blue.draw()
    creeper.draw()
    funny.draw()
    moss.draw()
    duck.draw()
    screen.draw.text(f'remaining health:{freshlol_health}',(freshlol.x,freshlol.y-50))
    screen.draw.text(f'remaining health:{gorilla_health}',(gorilla.x,gorilla.y-50))
    if fbactive:
        fireball.draw()
        
    #if earth_active:
        #earth.draw()

def update():
    global freshlol_health
    global gorilla_health
    global freshlol_alive
    global gorilla_alive
    global fbactive
    global earth_active

    if freshlol_alive==True:
        if keyboard.s:
            freshlol.y+=3
        if keyboard.w:
            freshlol.y-=3
        if keyboard.d:
            freshlol.x+=3
        if keyboard.a:
            freshlol.x-=3
        if keyboard.f:
            fbactive=True
            spawn_fireball()
        if keyboard.e:
            earth_active=True

    if gorilla_alive==True:
        if keyboard.down:
            gorilla.y+=2.5
        if keyboard.up:
            gorilla.y-=2.5
        if keyboard.right:
            gorilla.x+=2.5
        if keyboard.left:
            gorilla.x-=2.5
    
    if freshlol.colliderect(creeper):
        freshlol_health-=1000
        creepermovement()
    if freshlol.colliderect(blue):
        freshlol_health-=300
        bluemovement()
    if freshlol.colliderect(duck):
        freshlol_health-=500
        duckmovement()
    if freshlol.colliderect(funny):
        freshlol_health-=500
        funnymovement()
    if freshlol.colliderect(moss):
        freshlol_health-=500
        mossmovement()
    if freshlol_health<=0:
        freshlol_alive=False

    if gorilla.colliderect(creeper):
        gorilla_health-=1000
        creepermovement()
    if gorilla.colliderect(blue):
        gorilla_health-=300
        bluemovement()
    if gorilla.colliderect(duck):
        gorilla_health-=500
        duckmovement()
    if gorilla.colliderect(funny):
        gorilla_health-=500
        funnymovement()
    if gorilla.colliderect(moss):
        gorilla_health-=500
        mossmovement()
    if gorilla_health<=0:
        gorilla_alive=False

def spawn_fireball():
    global fbactive
    global enemies
    global blue_health,duck_health,creeper_health,funny_health,moss_health
    if fbactive==True:
        fireball.x=freshlol.x
        fireball.y=freshlol.y
        distance=1000
        target=None
        for enemy in enemies:
            d=freshlol.distance_to(enemy)
            if d<distance:
                distance=d
                target=enemy
        if target:
            animate(fireball, pos=(target.x,target.y), duration=0.75)
            if fireball.colliderect(target):
                if target==blue:
                    blue_health-=750
                elif target==duck:
                    duck_health-=1000
                elif target==creeper:
                    creeper_health-=1250
                elif target==funny:
                    funny_health-=1000
                elif target==moss:
                    moss_health-=1000
                target.x=random.randint(50,900)
                target.y=random.randint(50,600)
                fbactive=False
def fresh_healing():
    global freshlol_health
    freshlol_health+=500
def gorilla_healing():
    global gorilla_health
    gorilla_health+=500
clock.schedule_interval(fresh_healing,3)
clock.schedule_interval(gorilla_healing,3.5)

def creepermovement():
    global online
    if online==True:
        creeper.x=random.randint(50,900)
        creeper.y=random.randint(50,600)
clock.schedule_interval(creepermovement,3)

def bluemovement():
    global online
    if online==True:
        blue.x=random.randint(50,900)
        blue.y=random.randint(50,600)
clock.schedule_interval(bluemovement,1.5)

def duckmovement():
    global online
    if online==True:
        duck.x=random.randint(50,900)
        duck.y=random.randint(50,600)
clock.schedule_interval(duckmovement,2)

def funnymovement():
    global online
    if online==True:
        funny.x=random.randint(50,900)
        funny.y=random.randint(50,600)
clock.schedule_interval(funnymovement,2)

def mossmovement():
    global online
    if online==True:
        moss.x=random.randint(50,900)
        moss.y=random.randint(50,600)
clock.schedule_interval(mossmovement,2)





pgzrun.go()