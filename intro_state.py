from pico2d import *
import framework
import select_stage_state  # 상태 전환을 위해 SelectStageState 모듈을 가져옴
# 이미지 로드
width, height = 1060, 700

# Play 버튼 위치 및 크기
play_button_x, play_button_y, play_button_width, play_button_height = 180, 100, 250, 180

def is_inside_button(x, y, button_x, button_y, button_width, button_height):
    return (button_x - button_width // 2 <= x <= button_x + button_width // 2 and
            button_y - button_height // 2 <= y <= button_y + button_height // 2)

class IntroState:
    def init(self):
        global intro_image
        intro_image = load_image('resource/screen/intro.png')
        print("IntroState: 시작 화면입니다.")

    def finish(self):
        global intro_image
        del intro_image
        print("IntroState: 종료합니다.")

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.x, height - event.y
                if is_inside_button(mouse_x, mouse_y, play_button_x, play_button_y, play_button_width, play_button_height):
                    #print("Play 버튼이 클릭되었습니다! SelectStageState로 전환합니다.")
                    framework.change_mode(select_stage_state.SelectStageState())
            elif event.type == SDL_QUIT:
                framework.quit()

    def update(self):
        pass

    def draw(self):
        clear_canvas()
        intro_image.draw(width // 2, height // 2, width, height)

        left = play_button_x - (play_button_width // 2)
        right = play_button_x + (play_button_width // 2)
        bottom = play_button_y - (play_button_height // 2)
        top = play_button_y + (play_button_height // 2)
        #draw_rectangle(left, bottom, right, top)

        update_canvas()
