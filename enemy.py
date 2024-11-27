from pico2d import *
import game_world
import framework
import random
from state_machine import*

PIXEL_PER_METER = (10.0 / 0.4)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Enemy:
    def __init__(self):
        self.x, self.y = random.randint(1100, 1600), 380
        self.state = 0  # 0: walk, 1: attack, 2: die
        self.iscollision = 0
        self.is_removed = False
        self.frame = 0
        self.image = load_image('resource/enemy/zombie1.png')
        self.font = load_font('resource/ENCR10B.TTF', 20)
        self.stamina = 50
        self.time = 0.0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * framework.frame_time) % 5
        if self.iscollision == 0:
            self.x -= RUN_SPEED_PPS * framework.frame_time / 1.8
        elif self.iscollision == 1:
            self.time += 0.1

        if self.stamina <= 0:
            self.state = 2
        if self.state==2 and not self.is_removed:
            game_world.remove_object(self)
            self.is_removed = True
            self.iscollision = 0

    def draw(self):
        if self.stamina > 0:
            if self.state == 0:
                self.image.clip_draw(int(self.frame) * 50, 0, 50, 65, self.x, self.y, 100, 130)
            elif self.state == 1:
                self.image.clip_draw(int(self.frame) * 50, 65, 50, 65, self.x, self.y, 100, 130)
            self.font.draw(self.x - 10, self.y + 74, f'{self.stamina}', (255, 255, 255))
            draw_rectangle(*self.get_bb())



    def get_bb(self):
        return self.x - 40, self.y - 60, self.x + 40, self.y + 60

    def handle_collision(self, group, other):
        if self.is_removed:
            return

        if group == 'dragon:enemy' or group == 'mouse:enemy':
            self.iscollision = 1
            self.state = 1
            #other.state = 1
            if self.time >= 4.0:
                self.time = 0.0
                self.stamina -= 10
                other.stamina -= 5

            if other.stamina <= 0:
                self.state = 0
                self.iscollision = 0

        elif group == 'mace:enemy' or group == 'mace2:enemy':
            self.stamina -= 1

        elif group == 'enemy:player':
            self.iscollision = 1
            if self.time >= 6.0:
                self.time = 0.0
                self.font.draw(self.x + 10, self.y + 94, f'{-30}', (255, 255, 255))

