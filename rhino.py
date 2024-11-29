from pico2d import *
import game_world
import framework

PIXEL_PER_METER = (10.0 / 0.4)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Rhino:
    def __init__(self,x,y):
        self.x, self.y = x, y
        self.iscollision = 0
        self.is_removed = False
        self.state = 0  # 0: walk, 1: attack, 2: die
        self.frame = 0
        self.image = load_image('resource/player_unit/rhinoceros.png')
        self.font = load_font('resource/ENCR10B.TTF', 20)
        self.stamina = 60
        self.time = 0.0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * framework.frame_time) % 4

        if self.iscollision == 0:
            self.x += RUN_SPEED_PPS * framework.frame_time
            self.x = min(self.x, 1700)
        elif self.iscollision == 1:
            self.time += 0.1

        if self.stamina <= 0:
            self.state = 2
        if self.state == 2 and not self.is_removed:
            game_world.remove_object(self)
            self.is_removed = True
            self.iscollision = 0



    def draw(self):
        if self.stamina > 0:
            if self.state == 0:
                self.image.clip_draw(int(self.frame) * 128, 0, 128, 149, self.x, self.y, 166.4, 193.7)
            elif self.state == 1:
                self.image.clip_draw(int(self.frame) * 128, 128, 128,149, self.x, self.y,166.4,193.7)
            self.font.draw(self.x, self.y + 74, f'{self.stamina}', (255, 255, 255))



    def get_bb(self):
        # 충돌 박스 반환
        return self.x-40, self.y-60,self.x+40,self.y+60

    def handle_collision(self, group,other):
        if self.is_removed:
            return

        if group == 'rhino:enemy' or 'rhino:enemy2':
            self.iscollision = 1
            self.state = 1
            other.state = 1
            if self.time >= 6.0:
                self.time = 0.0
                other.stamina -= 30
            if other.stamina <= 0:
                self.state = 0
                self.iscollision = 0