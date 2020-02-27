#!/usr/bin/python3

from include import *
from clic import *

def delete_the_song(window, name):
	myfont = pygame.font.SysFont("monospace", 34, True)
	
	pygame.draw.rect(window, back_color, (0, 0, 1920, 1080))
	
	delete_song = myfont.render("Do you want to destroy this Music ?", 1, (255,0,0))
	window.blit(delete_song, (1920 / 2 - delete_song.get_rect().width / 2, 100))
	while (1):
		for event in pygame.event.get():
			pass
		mouse_pos = pygame.mouse.get_pos()
		if (mouse_pos[0] >= 636 and mouse_pos[0] <= 930 and mouse_pos[1] >= 650 and mouse_pos[1] <= 829):
			window.blit(yes_c, (636, 650))
			window.blit(no, (990, 650))
			if (pygame.mouse.get_pressed()[0]):
				wait_mouse_up()
				break;
		elif (mouse_pos[0] >= 990 and mouse_pos[0] <= 1284 and mouse_pos[1] >= 650 and mouse_pos[1] <= 829):
			window.blit(yes, (636, 650))
			window.blit(no_c, (990, 650))
			if (pygame.mouse.get_pressed()[0]):
				wait_mouse_up()
				return
		else:
			window.blit(yes, (636, 650))
			window.blit(no, (990, 650))
		pygame.display.update()
		clockFps.tick(maxFps)
	os.remove("./song/" + name)