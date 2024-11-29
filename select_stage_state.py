from pico2d import *
import framework
import stage1

# 이미지 로드
width, height = 1060, 700
select_button_x, select_button_y,select_button_width, select_button_height = 330, 330, 100, 150

def is_inside_button(x, y, button_x, button_y, button_width, button_height):
    return (button_x - button_width // 2 <= x <= button_x + button_width // 2 and
            button_y - button_height // 2 <= y <= button_y + button_height // 2)

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
            if event.type == SDL_MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.x, height - event.y
                if is_inside_button(mouse_x, mouse_y, select_button_x, select_button_y,select_button_width, select_button_height):
                    print("Play 버튼이 클릭되었습니다! SelectStageState로 전환합니다.")
                    framework.change_mode(stage1.Stage1State())
            elif event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
                framework.quit()

    def update(self):
        pass

    def draw(self):
        clear_canvas()
        select_stage_image.draw(width // 2, height // 2, width, height)

        left = select_button_x - (select_button_width // 2)
        right = select_button_x + (select_button_width // 2)
        bottom = select_button_y - (select_button_height // 2)
        top = select_button_y + (select_button_height // 2)
        #draw_rectangle(left, bottom, right, top)

        update_canvas()
