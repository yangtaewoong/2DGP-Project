from pico2d import*
import intro_state
import game_state

width, height = 1060, 800

open_canvas(width,height)
intro = load_image('resource\screen\intro.png')

while True:
    clear_canvas()
    intro.draw(width//2, height//2, width, height)
    update_canvas()

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()
