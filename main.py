from pico2d import*
import game_intro
import game_state

open_canvas(1060,800)
intro = load_image('resource\screen\intro.png')

while True:
    clear_canvas()
    intro.draw(530, 400)
    update_canvas()

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            close_canvas()
            exit()
