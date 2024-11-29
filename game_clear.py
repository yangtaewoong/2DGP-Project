from pico2d import *
import framework
import select_stage_state

# 이미지 로드
width, height = 1060, 700

class Gameclear:
    def init(self):
        global game_clear_image
        game_clear_image = load_image('resource/screen/game_clear.png')
        print("Stage1State: 게임 클리어! 클리어 화면으로 이동합니다.")
        
    def update(self):
        pass

    def finish(self):
        global game_clear_image
        del game_clear_image

    def draw(self):
        clear_canvas()
        game_clear_image.draw(width // 2, height // 2, width, height)

        update_canvas()

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN:
                framework.change_mode(select_stage_state.SelectStageState())
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                print("Gameclear: ESC 키를 눌러 게임을 종료합니다.")
                framework.quit()


