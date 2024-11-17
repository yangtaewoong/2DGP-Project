from pico2d import *
import game_world
import framework
import character
from state_machine import*

PIXEL_PER_METER = (10.0 / 0.4)
RUN_SPEED_KMPH = 10.0
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
        self.font = load_font('resource/ENCR10B.TTF', 20) # 폰트 로드
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
            if self.time > 1.0:  # 공격 타이밍
                self.time = 0

    def draw(self):
        if self.stamina > 0:
            if self.state == 0:
                self.image.clip_draw(int(self.frame) * 170, 0, 170, 170, self.x, self.y, 200, 200)
            elif self.state == 1:
                self.image.clip_draw(int(self.frame) * 170, 170, 170, 170, self.x, self.y, 200, 200)
            self.font.draw(self.x, self.y + 65, f'{self.stamina}', (255, 255, 255))
            draw_rectangle(*self.get_bb())

        # 죽음 상태에서 드래곤을 그리지 않거나 다른 처리를 할 수 있음
        if self.state == 2:  # 죽음 상태에서 드래곤을 그리지 않거나 다른 애니메이션 추가
            pass



    def get_bb(self):
        # 충돌 박스 반환
        return self.x - 85, self.y - 85, self.x + 85, self.y + 85

    def handle_collision(self, group,other):
        if group == "dragon:enemy":
            self.iscollision = True
            self.state = 1  # 공격 상태로 전환
            other.state = 1  # 좀비도 공격 상태로 전환
            self.stamina -= 1
            other.stamina -= 1
            if self.stamina <= 0:
                self.state = 2  # 체력이 0 이하일 때 죽음 상태로 전환
                self.stamina = 0  # 체력은 0으로 설정

    def set_collision(self, input):
        self.iscollision = input
        pass
