#!/usr/bin/python3

from include import *

def display_parameters(window):
	myfont = pygame.font.SysFont("monospace", 25, True)

	pygame.draw.rect(window, back_color, (0, 0, 1920, 1080))
	window.blit(myfont.render("FpsMax: " + str(maxFps), 1, (255,0,0)), (50, 100))

	pygame.display.update()	

def parameters_start(window):
	while (1):
		for event in pygame.event.get():
			if (event.type == QUIT):
				return (False)
			if (event.type == KEYDOWN):
				if (event.key == K_ESCAPE):
					return (True)
				if (event.key == K_f):
					pygame.display.toggle_fullscreen()
		display_parameters(window)
		clockFps.tick(maxFps)