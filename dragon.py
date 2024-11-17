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

class Dragon:
    def __init__(self):
        self.x, self.y = 100, 400
        self.iscollision = False  # 충돌 여부
        self.state = 0  # 0: walk, 1: attack, 2: die
        self.frame = 0
        self.image = load_image('resource/player_unit/dragon.png')  # 드래곤 이미지 로드
        self.font = load_font('ENCR10B.TTF', 16) # 폰트 로드
        self.stamina = 40  # 체력
        self.time = 0.0  # 타이머

    def update(self):
        # 프레임 업데이트
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * framework.frame_time) % 5

        if self.state == 0 and not self.iscollision:
            self.x += RUN_SPEED_PPS * framework.frame_time
            self.x = min(self.x, 1700)  # 오른쪽 경계 제한
        elif self.state == 1:  # Attack 상태
            self.time += framework.frame_time
        elif self.state == 2:  # Die 상태
            if self.stamina <= 0:
                game_world.remove_object(self)  # 체력이 0 이하일 때 제거

    def draw(self):
        if self.stamina < 0:
            game_world.remove_object(self)
        elif self.stamina > 0:
            if self.state == 0:
                self.image.clip_draw(int(self.frame) * 170, 0, 170, 170, self.x, self.y, 200, 200)
            #self.font.draw(self.x, self.y + 85, f'{self.stamina}', (255, 255, 255))
            draw_rectangle(*self.get_bb())

    def get_bb(self):
        # 충돌 박스 반환
        return self.x - 85, self.y - 85, self.x + 85, self.y + 85

    def handle_collision(self, other):
        # 충돌 처리 로직
        if not self.iscollision:
            self.iscollision = True
            self.state = 1  # Attack 상태
            self.stamina -= 10  # 체력 감소



