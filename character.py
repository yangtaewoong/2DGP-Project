from pico2d import *
import game_world
import framework
from state_machine import*

PIXEL_PER_METER = (10.0 / 0.4)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Idle:
    @staticmethod
    def enter(character, e):
        if start_event(e):
            character.action = 0
            character.face_dir = 1
        elif d_down(e) or a_up(e):
            character.action = 0
            character.face_dir = 1
        elif a_down(e) or d_up(e):
            character.action = 1
            character.face_dir = -1

        character.frame = 0

    @staticmethod
    def exit(character, e):
        pass

    @staticmethod
    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*framework.frame_time) % 8

    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frame) * 210,
                                  character.action * 120, 205, 120, character.x, character.y, 307.5,180)

class Run:
    @staticmethod
    def enter(character, e):
        if d_down(e) or a_up(e):
            character.dir,character.face_dir ,character.action = 1,1,0
        elif a_down(e) or d_up(e):
            character.dir, character.face_dir, character.action = -1, -1 ,1

    @staticmethod
    def exit(character, e):
        pass

    @staticmethod
    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * framework.frame_time) % 8
        character.x += character.dir * RUN_SPEED_PPS * framework.frame_time

    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frame) * 210,
                                  character.action * 120, 205, 120, character.x, character.y,307.5,180)

class Character:
    def __init__(self):
        self.x, self.y = 100, 380
        self.frame = 0
        self.face_dir = 1
        self.stamina = 100
        self.font = load_font('resource/ENCR10B.TTF', 30)
        self.image = load_image('resource/player/player_move.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {a_down: Run, d_down: Run, a_up: Run, d_up: Run},
                Run: {a_up: Idle, d_up: Idle, a_down: Idle, d_down: Idle},
            }
        )

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))
        pass

    def draw(self):
        self.state_machine.draw()

    def draw_at(self, screen_x, screen_y):

        self.state_machine.cur_state.draw(self)

    def get_bb(self):
        #return self.x - 20, self.y - 50, self.x + 20, self.y + 50
        pass

    def get_position(self):
        return self.x, self.y

    def handle_collision(self, group, other):
        pass