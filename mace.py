from pico2d import *
import game_world
import framework


PIXEL_PER_METER = (10.0 / 0.4)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Mace1:
    def __init__(self, x , y ):
        self.x, self.y,  = x,y
        self.frame = 0
        self.is_removed = False
        self.image = load_image('resource/mace/mace1_effect.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * framework.frame_time) % 5
        self.x += 1 * RUN_SPEED_PPS * framework.frame_time / 0.3
        if self.x > 1100 and not self.is_removed:
            game_world.remove_object(self)
            self.is_removed = True

    def draw(self):
        if self.x < 1000:
            self.image.clip_draw(int(self.frame) * 65, 0, 65, 57, self.x, self.y, 131.6, 114)


    def get_bb(self):
        return self.x - 40, self.y-60, self.x+40, self.y+60

    def handle_collision(self, other, group):
        if group == 'mace:enemy' or group == 'mace:enemy2':
            other.state = 2
            other.stamina = 0

