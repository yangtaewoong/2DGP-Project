from pico2d import *
import framework
import intro_state
import play_mode
import play_mode as stage1

open_canvas(1060, 800)
framework.run(intro_state.IntroState())
close_canvas()
