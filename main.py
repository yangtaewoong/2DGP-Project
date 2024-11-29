from pico2d import *
import framework
import intro_state
import game_clear

open_canvas(1060, 700)
framework.run(intro_state.IntroState())
close_canvas()
