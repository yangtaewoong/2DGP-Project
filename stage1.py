from pico2d import *
from character import Character
from dragon import Dragon
from enemy import Enemy
from mace_1 import Mace1
from mace_2 import Mace2
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
        self.enemies = []
        self.maces = []
        self.maces2 =[]
        self.dragons = []
        self.ui = None  # UI 객체

    def init(self):
        self.bg = BG('resource/background1.png')
        self.character = Character()
        self.ui = UI()
        self.enemies = [Enemy() for _ in range(3)]

        # 충돌 그룹 추가
        game_world.add_object(self.character, 1)
        for dragon in self.dragons:
            game_world.add_object(dragon, 1)

        for enemy in self.enemies:
            game_world.add_object(enemy,1)

        # 충돌 그룹 등록
        game_world.add_collision_pair('dragon:enemy', self.dragons, None)
        for enemy in self.enemies:
            game_world.add_collision_pair('dragon:enemy', None, enemy)

        print("Stage1: 첫 번째 스테이지 화면입니다.")

    def finish(self):
        game_world.remove_object(self.character)
        game_world.remove_object(self.dragons)
        for enemy in self.enemies:
            game_world.remove_object(enemy)
        for mace in self.maces:
            game_world.remove_object(mace)
        for mace2 in self.maces2:
            game_world.remove_object(mace2)

        for dragon in self.dragons:
            game_world.remove_object(dragon)

        del self.bg
        del self.character
        del self.ui
        print("Stage: 종료합니다.")

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
                framework.quit()
            elif event.type == SDL_KEYDOWN:
                self.character.handle_event(event)
                if event.key == SDLK_j:
                    new_mace = Mace1( self.character.x - self.x_offset, self.character.y)
                    self.maces.append(new_mace)
                    game_world.add_object(new_mace, 1)
                if event.key == SDLK_k:
                    new_mace2 = Mace2(self.character.x - self.x_offset + 100, self.character.y)
                    self.maces.append(new_mace2)
                    game_world.add_object(new_mace2, 1)
                if event.key == SDLK_2:
                    new_dragon = Dragon(self.character.x - self.x_offset, self.character.y)
                    self.dragons.append(new_dragon)


    def update(self):
        self.character.update()

        for dragon in self.dragons:
            dragon.update()

        for enemy in self.enemies:
            enemy.update()

        for mace in self.maces:
            mace.update()

        for mace2 in self.maces2:
            mace2.update()

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

        self.bg.draw(self.x_offset, self.y_offset)

        screen_x = self.character.x - self.x_offset
        screen_y = self.character.y
        self.character.font.draw(screen_x-30, screen_y + 100, f'{self.character.stamina}', (255, 255, 255))
        self.character.image.clip_draw(
            int(self.character.frame) * 210,
            self.character.action * 120,
            205, 120,
            screen_x, screen_y, 307.5, 180
        )

        for dragon in self.dragons:
            dragon.draw()

        for enemy in self.enemies:
            enemy.draw()

        for mace in self.maces:
            mace.draw()

        for mace2 in self.maces2:
            mace2.draw()

        self.ui.draw()

        update_canvas()

