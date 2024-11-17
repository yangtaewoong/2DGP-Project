from pico2d import *
from character import Character
from dragon import Dragon
from enemy import Enemy
import framework
import game_world

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
        self.enemies = []
        self.ui = None  # UI 객체

    def init(self):
        self.bg = BG('resource/background1.png')
        self.character = Character()
        self.ui = UI()
        self.dragon = Dragon()
        self.enemies = [Enemy() for _ in range(3)]

        # 충돌 그룹 추가
        game_world.add_object(self.character)
        game_world.add_object(self.dragon)
        for enemy in self.enemies:
            game_world.add_object(enemy)

        # 충돌 그룹 등록
        game_world.add_collision_pair('dragon:enemy', self.dragon, self.enemies)

        print("Stage1: 첫 번째 스테이지 화면입니다.")

    def finish(self):
        del self.bg
        del self.character
        del self.ui
        del self.dragon
        del self.enemies
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
        for enemy in self.enemies:
            enemy.update()

        char_x, char_y = self.character.get_position()

        scroll_start = 200
        max_offset = self.bg.width - 2197

        if char_x > scroll_start:
            self.x_offset = char_x - scroll_start
        else:
            self.x_offset = 0
        self.x_offset = max(0, min(self.x_offset, max_offset))

        # 충돌 처리
        game_world.handle_collisions()

    def draw(self):
        clear_canvas()

        # 배경 그리기
        self.bg.draw(self.x_offset, self.y_offset)

        screen_x = self.character.x - self.x_offset  # 화면 내 캐릭터의 X 좌표
        screen_y = self.character.y  # Y 좌표는 변하지 않음

        self.character.image.clip_draw(
            int(self.character.frame) * 210,
            self.character.action * 120,
            205, 120,
            screen_x, screen_y, 307.5, 180
        )
        self.dragon.draw()
        for enemy in self.enemies:
            enemy.draw()
        # UI 그리기
        self.ui.draw()

        update_canvas()

