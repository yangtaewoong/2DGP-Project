from pico2d import *
import framework

# 이미지 로드
width, height = 1060, 800

class Stage1State:
    def init(self):
        global stage1_image
        stage1_image = load_image('resource/background1.png')
        print("Stage1: 첫 번째 스테이지 화면입니다.")

    def finish(self):
        global stage1_image
        del stage1_image
        print("Stage: 종료합니다.")

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
                framework.quit()

    def update(self):
        pass

    def draw(self):
        clear_canvas()
        stage1_image.draw(width // 2, height // 2, width, height)
        update_canvas()
