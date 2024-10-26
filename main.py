from pico2d import*

width, height = 1060, 800
play_button_x, play_button_y, play_button_width, play_button_height = 200,50,300,200
open_canvas(width,height)
intro = load_image('resource\screen\intro.png')

def is_inside_button(x, y, button_x, button_y, button_width, button_height):
    # 클릭 좌표(x, y)가 버튼 영역 안에 있는지 확인
    return (button_x - button_width // 2 <= x <= button_x + button_width // 2 and
            button_y - button_height // 2 <= y <= button_y + button_height // 2)


while True:
    clear_canvas()
    intro.draw(width//2, height//2, width, height)
    update_canvas()

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.x, height - event.y
            if is_inside_button(mouse_x, mouse_y, play_button_x, play_button_y, play_button_width, play_button_height):
                print("Play 버튼이 클릭되었습니다!")
