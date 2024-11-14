from pico2d import *
import framework
import intro_state
import select_stage_state

open_canvas(1060, 800)
framework.run(intro_state.IntroState())
close_canvas()
