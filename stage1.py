from pico2d import *
from character import Character
import framework

# 이미지 로드
width, height = 1060, 800

class Stage1State:
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
        pass

    def draw(self):
        clear_canvas()
        stage1_image.draw(width // 2, height // 2, width, height)
        character.draw()
        update_canvas()
