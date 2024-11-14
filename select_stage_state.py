from pico2d import *
import framework

# 이미지 로드
select_stage_image = None
width, height = 1060, 800

class SelectStageState:
    def init(self):
        global select_stage_image
        select_stage_image = load_image('resource/stage_select/select_map_3.png')
        print("SelectStageState: 스테이지 선택 화면입니다.")

    def finish(self):
        global select_stage_image
        del select_stage_image
        print("SelectStageState: 종료합니다.")

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
                framework.quit()

    def update(self):
        pass

    def draw(self):
        clear_canvas()
        select_stage_image.draw(width // 2, height // 2, width, height)
        update_canvas()
