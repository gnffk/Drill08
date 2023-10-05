from pico2d import *
import random
# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)
    def update(self): pass
class Boy:
    def __init__(self):
        self.x ,self.y = random.randint(100,700),90
        self.speed = random.randint(0,10)
        self.frame =0
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame +1)%8
        self.x +=5
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)
class Boal:
    def __init__(self):
        self.x , self.y = random.randint(50,750),599
        self.size = random.randint(0,1)
        if self.size == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
    def update(self):
        self.speed = random.randint(0, 10)
        self.y -= self.speed

        if self.size == 0:
            if self.y <= 90:
                self.y = 60
        else:
            if self.y <= 80:
                self.y = 75

    def draw(self):
        if self.size == 0:
            self.image.clip_draw(0,0,21,21,self.x,self.y)
        else:
            self.image.clip_draw(0,0,44,44,self.x,self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
running = True


def reset_world():
    global running
    global grass
    global team
    global world
    global boals
    running = True
    world = []

    grass = Grass()

    world.append(grass)

    team = [Boy() for i in range(10)]

    boals = [Boal() for i in range(20)]

    world+=team
    world+=boals
def update_world():
    for o in world:
        o.update()
    pass


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()



open_canvas()
reset_world()
# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code

close_canvas()
