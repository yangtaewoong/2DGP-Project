from pico2d import *
import game_world
import framework
from character import Character


def handle_events(self):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            framework.quit()
        else:
            character.handle_event(event)

def init(self):
    global character

    character = Character()

    #충돌 정보를 등록


def finish(self):
    game_world.clear()



def update(self):
    game_world.update()  # 모든 객체 업데이트
    game_world.handle_collisions()  # 충돌 처리


def draw(self):
    clear_canvas()
    game_world.render()  # 모든 객체 렌더링
    update_canvas()

def pause():
    pass

def resume():
    pass