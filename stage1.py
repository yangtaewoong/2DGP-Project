from pico2d import *
from character import Character
from dragon import Dragon
import framework

width, height = 1060, 510

class BG:
    def __init__(self, image_path):
        self.image = load_image(image_path)
        self.width = 3257  # 배경 이미지의 너비
        self.height = 578  # 배경 이미지의 높이

    def draw(self, x_offset, y_offset):
        # 배경 이미지를 스크롤된 위치에 맞게 그리기
        self.image.draw(width // 2 - x_offset, y_offset, self.width, self.height)

class UI:
    def __init__(self):
        self.image = load_image('resource/ui.png')

    def draw(self):
        # 화면 상단 중앙에 UI 표시
        self.image.draw(530,155)

class Stage1State:
    def __init__(self):
        self.x_offset = 0
        self.y_offset = 500
        self.scroll_speed = 5
        self.bg = None
        self.character = None
        self.dragon = None
        self.ui = None  # UI 객체

    def init(self):
        self.bg = BG('resource/background1.png')
        self.character = Character()
        self.ui = UI()
        self.dragon = Dragon()
        print("Stage1: 첫 번째 스테이지 화면입니다.")

    def finish(self):
        del self.bg
        del self.character
        del self.ui
        print("Stage: 종료합니다.")

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
                framework.quit()
            elif event.type == SDL_KEYDOWN:
                self.character.handle_event(event)

    def update(self):
        self.character.update()
        self.dragon.update()

        # 캐릭터의 월드 좌표 가져오기
        char_x, char_y = self.character.get_position()

        # 스크롤 기준점과 한계 처리
        scroll_start = 200
        max_offset = self.bg.width - 2197

        # 스크롤 계산: 캐릭터가 기준점을 넘어가면 x_offset 변경
        if char_x > scroll_start:
            self.x_offset = char_x - scroll_start
        else:
            self.x_offset = 0

        self.x_offset = max(0, min(self.x_offset, max_offset))
        print(f"Character X: {char_x}, X Offset: {self.x_offset}, Max Offset: {max_offset}")

    def draw(self):
        clear_canvas()

        # 배경 그리기
        self.bg.draw(self.x_offset, self.y_offset)

        # 캐릭터의 화면 내 좌표 계산
        screen_x = self.character.x - self.x_offset  # 화면 내 캐릭터의 X 좌표
        screen_y = self.character.y  # Y 좌표는 변하지 않음

        # 캐릭터 그리기 (월드 좌표 대신 변환된 좌표를 넘겨줌)
        self.character.image.clip_draw(
            int(self.character.frame) * 210,
            self.character.action * 120,
            205, 120,
            screen_x, screen_y, 307.5, 180
        )
        self.dragon.draw()

        # UI 그리기
        self.ui.draw()

        update_canvas()
