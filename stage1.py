from pico2d import *
from character import Character
import framework

width, height = 1060,510

class Stage1State:
    def __init__(self):
        self.x_offset = 0  # 화면의 x 오프셋
        self.y_offset = 500  # 화면의 y 오프셋
        self.scroll_speed = 5 # 스크롤 속도
        self.bg_width = 3257  # 배경 이미지의 너비
        self.bg_height = 578  # 배경 이미지의 높이

    def init(self):
        global stage1_image, character
        stage1_image = load_image('resource/background1.png')
        character = Character()
        print("Stage1: 첫 번째 스테이지 화면입니다.")

    def finish(self):
        global stage1_image, character
        del stage1_image
        del character
        print("Stage: 종료합니다.")

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
                framework.quit()
            elif event.type == SDL_KEYDOWN:
                character.handle_event(event)

    def update(self):
        character.update()

        char_x, char_y = character.get_position()

        scroll_start = width // 5
        if char_x > scroll_start:
            self.x_offset = char_x - scroll_start
            self.x_offset = max(0, min(self.x_offset, self.bg_width - width))

    def draw(self):
        clear_canvas()

        # 배경 이미지를 스크롤된 위치에 맞게 그리기
        stage1_image.draw(-self.x_offset, self.y_offset, self.bg_width, self.bg_height)  # 배경 크기 설정

        # 캐릭터 그리기
        char_x, char_y = character.get_position()
        character.draw()

        update_canvas()
