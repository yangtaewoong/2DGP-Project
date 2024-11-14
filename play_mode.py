from pico2d import *
import game_world
import framework
from character import Character

class PlayState:
    def init(self):
        self.character = Character()
        #self.enemy = Enemy(300, 100)

        # 캐릭터와 적을 게임 월드에 추가
        game_world.add_object(self.character, depth=1)
        game_world.add_object(self.enemy, depth=1)

        # 충돌 그룹 등록 (캐릭터와 적)
        game_world.add_collision_pair('Character-Enemy', self.character, self.enemy)

    def finish(self):
        game_world.clear()

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                framework.quit()

    def update(self):
        game_world.update()  # 모든 객체 업데이트
        game_world.handle_collisions()  # 충돌 처리

    def draw(self):
        clear_canvas()
        game_world.render()  # 모든 객체 렌더링
        update_canvas()
