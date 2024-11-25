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

class Mace2:
    def __init__(self, x , y ):
        self.x, self.y,  = x,y
        self.frame = 0
        self.is_removed = False
        self.iscollision = 1
        self.image = load_image('resource/mace/mace2_effect.png')
        self.elapsed_time = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * framework.frame_time) % 3
        self.elapsed_time+= 0.01
        if self.elapsed_time >= 3.0 and not self.is_removed:
            game_world.remove_object(self)
            self.is_removed = True

    def draw(self):
        if not self.is_removed:
            self.image.clip_draw(int(self.frame) * 161, 0, 161, 71, self.x + 230, self.y - 50, 330, 228)
            draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y-60, self.x+40, self.y+60
        pass

    def handle_collision(self, other, group):
        if group == 'enemy:mace2':
            other.state =2