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

class Mouse:
    def __init__(self,x,y):
        self.x, self.y = x,y
        self.state = 0  # 0: walk, 1: attack, 2: die
        self.frame = 0
        self.image = load_image('resource/player_unit/mouse.png')
        self.font = load_font('resource/ENCR10B.TTF', 20)
        self.stamina = 30
        self.time = 0.0
        self.is_removed = False

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * framework.frame_time) % 6
        if self.state == 0:
            self.x += 1 * RUN_SPEED_PPS * framework.frame_time
        if self.state == 2 and not self.is_removed:
            game_world.remove_object(self)
            self.is_removed = True

    def draw(self):
        if self.stamina>0:
            if self.state == 0:
                self.image.clip_draw(int(self.frame) * 57, 0, 57, 51, self.x, self.y, 100, 120)
                self.font.draw(self.x - 20, self.y + 51, f'{self.stamina}', (255, 255, 255))
                draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 50, self.x + 30, self.y + 50

    def handle_collision(self, other, group):
        if group == 'mouse:enemy':
            if self.time >= 3.0:
                self.time = 0.0
                other.stamina -= 5
            if self.stamina <= 0:
                self.state = 2