from pico2d import *

# 캔버스 설정
width, height = 1060, 800
open_canvas(width, height)

# 이미지 로드
intro_image = load_image('resource/screen/intro.png')
select_stage_image = load_image('resource/stage_select/select_map_3.png')
stage1_image = load_image('resource/stage_select/background1.png')


# Play 버튼 위치 및 크기
play_button_x, play_button_y, play_button_width, play_button_height = 200, 50, 300, 200


# 버튼 클릭 위치 확인 함수
def is_inside_button(x, y, button_x, button_y, button_width, button_height):
    return (button_x - button_width // 2 <= x <= button_x + button_width // 2 and
            button_y - button_height // 2 <= y <= button_y + button_height // 2)


# Intro 상태 클래스
class IntroState:
    def enter(self):
        print("IntroState: 시작 화면입니다.")

    def exit(self):
        print("IntroState: 종료합니다.")

    def update(self):
        clear_canvas()
        intro_image.draw(width // 2, height // 2, width, height)
        update_canvas()

    def handle_events(self, event, state_machine):
        if event.type == SDL_MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.x, height - event.y
            if is_inside_button(mouse_x, mouse_y, play_button_x, play_button_y, play_button_width, play_button_height):
                print("Play 버튼이 클릭되었습니다! 다음 상태로 전환합니다.")
                state_machine.change_state(SelectStageState())


# SelectStage 상태 클래스
class SelectStageState:
    def enter(self):
        print("SelectStageState: 스테이지 선택 화면입니다.")

    def exit(self):
        print("SelectStageState: 종료합니다.")

    def update(self):
        clear_canvas()
        select_stage_image.draw(width // 2, height // 2, width, height)
        update_canvas()

    def handle_events(self, event, state_machine):
        if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            state_machine.running = False


# 상태 머신 클래스
class StateMachine:
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.current_state.enter()
        self.running = True

    def change_state(self, new_state):
        self.current_state.exit()
        self.current_state = new_state
        self.current_state.enter()

    def update(self):
        self.current_state.update()

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self.running = False
            else:
                self.current_state.handle_events(event, self)


state_machine = StateMachine(IntroState())

while state_machine.running:
    state_machine.update()
    state_machine.handle_events()

close_canvas()
