from pico2d import *
import game_world
import framework
import character
from state_machine import*

PIXEL_PER_METER = (10.0 / 0.4)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Zombie1:
    def __init__(self):
        self.x, self.y = random.randint(1500, 1700), 400
        self.state = 0  # 충돌 = 0 , 충돌 아닌 상황 = 1
        self.iscollision = 0
        self.frame = 0
        self.image = load_image('resource/enemy/zombie1.png')
        self.font = load_font('ENCR10B.TTF', 40)
        self.stamina = 50
        self.time = 0.0