from pico2d import *
from character import Character
from dragon import Dragon
from mouse import Mouse
from enemy import Enemy
from enemy2 import Enemy2
from mace import Mace1
from mace_2 import Mace2
import framework
import game_world

PIXEL_PER_METER = (10.0 / 0.4)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

width, height = 1060, 510

class BG:
    def __init__(self, image_path):
        self.image = load_image(image_path)
        self.width = 3257
        self.height = 578

    def draw(self, x_offset, y_offset):
        self.image.draw(width // 2 - x_offset, y_offset, self.width, self.height)

class UI:
    def __init__(self):
        self.image = load_image('resource/ui.png')

    def draw(self):
        self.image.draw(530,155)

class Mana:
    def __init__(self):
        self.mana = 0
        self.x = 860  # 마나 바의 중심 x 좌표
        self.y = 250 # 마나 바의 중심 y 좌표
        self.width = width  # 마나 바의 전체 너비
        self.height = height  # 마나 바의 전체 높이
        self.mana_timer = 0
        self.food = 0
        self.image = load_image('resource/mana_bar.png')
        self.font = load_font('resource/ENCR10B.TTF', 30)

    def update(self):
        if self.mana_timer > 5.0:
            if self.mana < 100:
                self.mana += 1
            self.mana_timer = 0

    def draw_mana_bar(self):
        self.font.draw(860, 260, f'{self.mana}', (255, 255, 255))

        # 채워진 마나 바 그리기
        mana_ratio = self.mana / 40
        fill_width = width *
        self.image.clip_draw_to_origin(
            0, 0, int(fill_width), self.height,  # 이미지에서 그릴 부분 (너비는 비율에 따라 조절)
            self.x - self.width // 2, self.y - self.height // 2  # 화면에 그릴 위치
        )




class Stage1State:
    def __init__(self):
        self.x_offset = 0
        self.y_offset = 500
        self.scroll_speed = 5
        self.bg = None
        self.character = None
        self.enemies = []
        self.enemies2 = []
        self.maces = []
        self.maces2 =[]
        self.dragons = []
        self.mouses =[]
        self.ui = None
        self.font = load_font('resource/ENCR10B.TTF', 30)


    def init(self):
        self.bg = BG('resource/background1.png')
        self.character = Character()
        self.ui = UI()
        self.mana =Mana()
        self.enemies = [Enemy() for _ in range(3)]
        self.enemies2 = [Enemy2() for _ in range(3)]
        game_world.add_object(self.character, 1)

        for dragon in self.dragons:
            game_world.add_object(dragon, 1)

        for mouse in self.mouses:
            game_world.add_object(mouse, 1)

        for enemy in self.enemies:
            game_world.add_object(enemy,1)

        for enemy2 in self.enemies2:
            game_world.add_object(enemy2,1)

        for mace in self.maces:
            game_world.add_object(mace, 1)

        for mace2 in self.maces2:
            game_world.add_object(mace2, 1)

    def finish(self):
        game_world.remove_object(self.character)
        for enemy in self.enemies:
            if not enemy.is_removed:
                game_world.remove_object(enemy)
        for mace in self.maces:
            if not mace.is_removed:
                game_world.remove_object(mace)
        for mace2 in self.maces2:
            if not mace2.is_removed:
                game_world.remove_object(mace2)

        for mouse in self.mouses:
            if not mouse.is_removed:
                game_world.remove_object(mouse)

        for dragon in self.dragons:
            if not dragon.is_removed:
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
                if event.key == SDLK_j and self.mana >= 90:
                    self.mana -= 90
                    new_mace = Mace1( self.character.x - self.x_offset, self.character.y)
                    self.maces.append(new_mace)
                    game_world.add_object(new_mace, 1)
                    game_world.add_collision_pair('mace:enemy', [new_mace], self.enemies)
                    game_world.add_collision_pair('mace:enemy2', [new_mace], self.enemies2)

                if event.key == SDLK_k and self.mana >= 30:
                    self.mana -= 30
                    new_mace2 = Mace2(self.character.x - self.x_offset + 100, self.character.y)
                    self.maces.append(new_mace2)
                    game_world.add_object(new_mace2, 1)
                    game_world.add_collision_pair('mace2:enemy', [new_mace2], self.enemies)
                    game_world.add_collision_pair('mace2:enemy2', [new_mace2], self.enemies2)

                if event.key == SDLK_1 and self.food >=10:
                    self.food -= 10
                    new_mouse = Mouse(self.character.x - self.x_offset, self.character.y)
                    self.mouses.append(new_mouse)
                    game_world.add_object(new_mouse, 1)
                    game_world.add_collision_pair('mouse:enemy', [new_mouse], self.enemies)
                    game_world.add_collision_pair('mouse:enemy2', [new_mouse], self.enemies2)

                if event.key == SDLK_2 and self.food >= 20:
                    self.food -= 20
                    new_dragon = Dragon(self.character.x - self.x_offset, self.character.y)
                    self.dragons.append(new_dragon)
                    game_world.add_object(new_dragon, 1)
                    game_world.add_collision_pair('dragon:enemy', [new_dragon], self.enemies)
                    game_world.add_collision_pair('dragon:enemy2', [new_dragon], self.enemies2)

    def update(self):
        self.character.update()

        for dragon in self.dragons:
            dragon.update()

        for mouse in self.mouses:
            mouse.update()

        for enemy in self.enemies:
            enemy.update()

        for enemy2 in self.enemies2:
            enemy2.update()

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

        # 타이머 증가
        self.food_timer += ACTION_PER_TIME / FRAMES_PER_ACTION
        self.mana_timer += ACTION_PER_TIME / FRAMES_PER_ACTION

        if self.food_timer > 3.0:
            if self.food < 40:
                self.food += 1
            self.food_timer = 0



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

        for mouse in self.mouses:
            mouse.draw()

        for enemy in self.enemies:
            enemy.draw()

        for enemy2 in self.enemies2:
            enemy2.draw()

        for mace in self.maces:
            mace.draw()

        for mace2 in self.maces2:
            mace2.draw()

        self.ui.draw()
        self.font.draw(120, 260, f'{self.food}', (255, 255, 255))

        self.font.draw(700, 25, f'{0}', (255, 255, 255))
        update_canvas()








